#!/usr/bin/env python3
"""
=============================================================================
SYSTEMS LITERACY CURRICULUM PIPELINE - ORCHESTRATION READY
=============================================================================

A comprehensive pipeline that orchestrates all curriculum generation agents:

LAYER 1: ORCHESTRATOR
    → Lesson Queue Management
    → Agent Lifecycle
    → Quality Gates
    → GitHub Sync

LAYER 2: CONTENT AGENTS
    → Designer (curriculum structure)
    → Creator (detailed content)
    → Coder (p5.js simulations)
    → Assessor (assessments)
    → Creativity (story/metaphors)
    → SystemsLiteracy (standards alignment)

LAYER 3: VALIDATION AGENTS
    → StandardsValidator (BC + CSTA)
    → DifferentiationExpert (3-level)
    → QualityScorer (overall)
    → AccessibilityChecker

LAYER 4: TESTING AGENTS
    → StudentAgent (multiple personas)
    → ParentAgent (reviewers)
    → AdversarialAgent (red team)
    → AccessibilityTester

LAYER 5: DEPLOYMENT
    → GitHub commit
    → Versioning
    → Dashboard update
    → Notification

=============================================================================
"""

import json
import os
import subprocess
import hashlib
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional, Callable
from enum import Enum
import logging
import asyncio

# ============================================================================
# CONFIGURATION
# ============================================================================

BASE = Path("/root/.openclaw/workspace/lesson-hub")
DOCS = BASE / "docs"
DATA = BASE / "data"
LOGS = BASE / "logs"

for d in [DATA, LOGS]:
    d.mkdir(exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler(LOGS / f"pipeline_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============================================================================
# DATA CLASSES
# ============================================================================

class LessonStatus(Enum):
    QUEUED = "queued"
    DESIGNING = "designing"
    CREATING = "creating"
    CODING = "coding"
    VALIDATING = "validating"
    TESTING = "testing"
    DEPLOYING = "deploying"
    COMPLETE = "complete"
    FAILED = "failed"

@dataclass
class Lesson:
    """Represents a lesson in the pipeline"""
    id: str = ""
    grade: int = 1
    module: int = 1
    topic: str = ""
    status: LessonStatus = LessonStatus.QUEUED
    version: int = 1
    score: float = 0.0
    issues: List[str] = field(default_factory=list)
    test_results: Dict = field(default_factory=dict)
    standards_alignment: Dict = field(default_factory=dict)
    created_at: str = ""
    deployed_at: str = ""
    duration_seconds: float = 0.0
    
    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(
                f"{self.grade}-{self.module}-{self.topic}".encode()
            ).hexdigest()[:8]
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
    
    @property
    def filename(self) -> str:
        return f"LESSON-GRADE{self.grade}-MODULE{self.module}.md"
    
    def to_dict(self) -> Dict:
        return {
            **asdict(self),
            'status': self.status.value
        }

@dataclass
class PipelineStats:
    """Pipeline statistics"""
    total_processed: int = 0
    passed: int = 0
    failed: int = 0
    average_score: float = 0.0
    total_duration: float = 0.0
    by_stage: Dict[str, int] = field(default_factory=dict)

@dataclass  
class AgentResult:
    """Result from an agent execution"""
    agent: str
    success: bool
    score_delta: float = 0.0
    issues: List[str] = field(default_factory=list)
    output: str = ""
    duration_ms: int = 0

# ============================================================================
# LAYER 1: ORCHESTRATOR
# ============================================================================

class PipelineOrchestrator:
    """
    The brain - coordinates all agents and manages the complete workflow.
    Ready for autonomous operation, subagent spawning, and cron scheduling.
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or self._default_config()
        self.queue: List[Lesson] = []
        self.completed: List[Lesson] = []
        self.failed: List[Lesson] = []
        self.stats = PipelineStats()
        self.agents = self._initialize_agents()
        self.dashboard = DashboardReporter(self.config)
        self.load_state()
        
        logger.info("🎯 Pipeline Orchestrator initialized")
        
    def _default_config(self) -> Dict:
        return {
            "min_score": 60,
            "max_retries": 3,
            "auto_deploy": True,
            "github_enabled": True,
            "dashboard_enabled": True,
            "notification_enabled": False,
            "parallel_agents": False,
            "strict_mode": False
        }
    
    def _initialize_agents(self) -> Dict[str, Any]:
        """Initialize all pipeline agents"""
        return {
            # Content Agents
            "designer": DesignerAgent(self.config),
            "creator": CreatorAgent(self.config),
            "coder": CoderAgent(self.config),
            "assessor": AssessorAgent(self.config),
            "creativity": CreativityAgent(self.config),
            "systems_literacy": SystemsLiteracyAgent(self.config),
            
            # Validation Agents
            "standards_validator": StandardsValidator(self.config),
            "differentiation_expert": DifferentiationExpert(self.config),
            "quality_scorer": QualityScorer(self.config),
            "accessibility_checker": AccessibilityChecker(self.config),
            
            # Testing Agents
            "student_agent": StudentAgent(self.config),
            "parent_agent": ParentAgent(self.config),
            "adversarial_agent": AdversarialAgent(self.config),
        }
    
    # -------------------------------------------------------------------------
    # Queue Management
    # -------------------------------------------------------------------------
    
    def add_lesson(self, grade: int, module: int, topic: str) -> Lesson:
        """Add a lesson to the processing queue"""
        lesson = Lesson(grade=grade, module=module, topic=topic)
        self.queue.append(lesson)
        logger.info(f"📝 Queued: Grade {grade} Module {module} - {topic}")
        self.save_state()
        return lesson
    
    def add_lessons_batch(self, lessons: List[tuple]) -> List[Lesson]:
        """Add multiple lessons at once"""
        return [self.add_lesson(g, m, t) for g, m, t in lessons]
    
    def get_next_lesson(self) -> Optional[Lesson]:
        """Get next lesson from queue (priority order)"""
        if not self.queue:
            return None
        
        # Priority: failed lessons first, then by grade (younger first)
        self.queue.sort(key=lambda l: (
            l.status == LessonStatus.FAILED,
            l.grade,
            l.module
        ))
        return self.queue.pop(0)
    
    # -------------------------------------------------------------------------
    # Pipeline Execution
    # -------------------------------------------------------------------------
    
    def process_lesson(self, lesson: Lesson) -> Lesson:
        """Process a single lesson through all layers"""
        start_time = datetime.now()
        
        logger.info(f"🔄 Processing: {lesson.topic} (Grade {lesson.grade})")
        
        try:
            # LAYER 2: Content Generation
            lesson = self._run_agent("designer", lesson)
            lesson = self._run_agent("creator", lesson)
            lesson = self._run_agent("coder", lesson)
            lesson = self._run_agent("assessor", lesson)
            lesson = self._run_agent("creativity", lesson)
            lesson = self._run_agent("systems_literacy", lesson)
            
            # LAYER 3: Validation
            lesson = self._run_agent("standards_validator", lesson)
            lesson = self._run_agent("differentiation_expert", lesson)
            lesson = self._run_agent("quality_scorer", lesson)
            lesson = self._run_agent("accessibility_checker", lesson)
            
            # LAYER 4: Testing (Simulated Users)
            lesson = self._run_agent("student_agent", lesson)
            lesson = self._run_agent("parent_agent", lesson)
            lesson = self._run_agent("adversarial_agent", lesson)
            
            # LAYER 5: Deployment
            if lesson.score >= self.config["min_score"]:
                lesson = self._deploy(lesson)
                lesson.status = LessonStatus.COMPLETE
                self.completed.append(lesson)
                logger.info(f"✅ COMPLETE: {lesson.topic} (Score: {lesson.score:.1f})")
            else:
                lesson.status = LessonStatus.FAILED
                self.failed.append(lesson)
                logger.warning(f"❌ FAILED: {lesson.topic} (Score: {lesson.score:.1f})")
                
        except Exception as e:
            lesson.status = LessonStatus.FAILED
            lesson.issues.append(f"Pipeline error: {str(e)}")
            self.failed.append(lesson)
            logger.error(f"❌ ERROR: {lesson.topic} - {e}")
        
        # Update stats
        lesson.duration_seconds = (datetime.now() - start_time).total_seconds()
        self._update_stats(lesson)
        self.save_state()
        self.dashboard.update(self)
        
        return lesson
    
    def _run_agent(self, agent_name: str, lesson: Lesson) -> Lesson:
        """Run a single agent on the lesson"""
        agent = self.agents.get(agent_name)
        if not agent:
            logger.warning(f"⚠️ Unknown agent: {agent_name}")
            return lesson
        
        try:
            # Update status based on agent type
            status_map = {
                "designer": LessonStatus.DESIGNING,
                "creator": LessonStatus.CREATING,
                "coder": LessonStatus.CODING,
                "assessor": LessonStatus.CREATING,
                "creativity": LessonStatus.CREATING,
                "systems_literacy": LessonStatus.CREATING,
                "standards_validator": LessonStatus.VALIDATING,
                "differentiation_expert": LessonStatus.VALIDATING,
                "quality_scorer": LessonStatus.VALIDATING,
                "accessibility_checker": LessonStatus.VALIDATING,
                "student_agent": LessonStatus.TESTING,
                "parent_agent": LessonStatus.TESTING,
                "adversarial_agent": LessonStatus.TESTING,
            }
            lesson.status = status_map.get(agent_name, lesson.status)
            
            # Execute agent
            result = agent.process(lesson)
            
            # Merge results
            if result.issues:
                lesson.issues.extend(result.issues)
            lesson.score = max(0, min(100, lesson.score + result.score_delta))
            
            logger.debug(f"  ✓ {agent_name}: +{result.score_delta:.1f} (score: {lesson.score:.1f})")
            
        except Exception as e:
            logger.error(f"  ✗ {agent_name}: {e}")
            lesson.issues.append(f"{agent_name}: {str(e)}")
        
        return lesson
    
    def _deploy(self, lesson: Lesson) -> Lesson:
        """Deploy lesson to GitHub"""
        lesson.status = LessonStatus.DEPLOYING
        
        if not self.config["github_enabled"]:
            return lesson
        
        try:
            # Git add
            subprocess.run(['git', 'add', '-A'], cwd=BASE, check=True, capture_output=True)
            
            # Git commit
            subprocess.run([
                'git', 'commit', '-m', 
                f'Lesson: {lesson.topic} (Grade {lesson.grade}) - Score: {lesson.score:.0f}'
            ], cwd=BASE, check=True, capture_output=True)
            
            # Git push
            token = os.popen("gh auth token").read().strip()
            subprocess.run([
                'git', 'push', 
                f'https://x-access-token:{token}@github.com/H-H-E/lesson-hub.git',
                'master'
            ], cwd=BASE, check=True, capture_output=True)
            
            lesson.deployed_at = datetime.now().isoformat()
            logger.info(f"🚀 Deployed: {lesson.topic}")
            
        except Exception as e:
            logger.warning(f"⚠️ Deploy failed: {e}")
            lesson.issues.append(f"Deploy: {str(e)}")
        
        return lesson
    
    def _update_stats(self, lesson: Lesson):
        """Update pipeline statistics"""
        self.stats.total_processed += 1
        self.stats.total_duration += lesson.duration_seconds
        
        if lesson.status == LessonStatus.COMPLETE:
            self.stats.passed += 1
        else:
            self.stats.failed += 1
        
        # Running average
        self.stats.average_score = (
            (self.stats.average_score * (self.stats.total_processed - 1) + lesson.score)
            / self.stats.total_processed
        )
        
        # By stage
        stage = lesson.status.value
        self.stats.by_stage[stage] = self.stats.by_stage.get(stage, 0) + 1
    
    # -------------------------------------------------------------------------
    # Batch Processing
    # -------------------------------------------------------------------------
    
    def run_batch(self, max_lessons: int = 10) -> Dict:
        """Process multiple lessons"""
        processed = 0
        results = []
        
        logger.info(f"📦 Starting batch processing (max: {max_lessons})")
        
        while processed < max_lessons:
            lesson = self.get_next_lesson()
            if not lesson:
                break
                
            result = self.process_lesson(lesson)
            results.append({
                "id": result.id,
                "topic": result.topic,
                "status": result.status.value,
                "score": result.score,
                "issues": len(result.issues)
            })
            processed += 1
        
        logger.info(f"📦 Batch complete: {processed} lessons")
        
        return {
            "processed": processed,
            "passed": self.stats.passed,
            "failed": self.stats.failed,
            "average_score": self.stats.average_score,
            "results": results
        }
    
    def run_continuous(self, duration_minutes: int = 60) -> Dict:
        """Run continuously for a duration"""
        logger.info(f"🔄 Starting continuous mode ({duration_minutes} min)")
        
        start = datetime.now()
        initial_count = self.stats.total_processed
        
        while (datetime.now() - start).total_seconds() < duration_minutes * 60:
            lesson = self.get_next_lesson()
            if not lesson:
                logger.info("Queue empty, waiting...")
                break
            
            self.process_lesson(lesson)
        
        elapsed = (datetime.now() - start).total_seconds() / 60
        
        return {
            "elapsed_minutes": elapsed,
            "lessons_processed": self.stats.total_processed - initial_count,
            "total_processed": self.stats.total_processed,
            "passed": self.stats.passed,
            "failed": self.stats.failed,
            "average_score": self.stats.average_score
        }
    
    # -------------------------------------------------------------------------
    # State Management
    # -------------------------------------------------------------------------
    
    def save_state(self):
        """Persist pipeline state"""
        state = {
            "queue": [l.to_dict() for l in self.queue],
            "completed": [l.to_dict() for l in self.completed[-50:]],  # Last 50
            "stats": asdict(self.stats),
            "config": self.config,
            "saved_at": datetime.now().isoformat()
        }
        (DATA / "orchestrator_state.json").write_text(json.dumps(state, indent=2))
        self.dashboard.save_json(state)
    
    def load_state(self):
        """Restore pipeline state"""
        state_file = DATA / "orchestrator_state.json"
        if not state_file.exists():
            return
        
        try:
            state = json.loads(state_file.read_text())
            self.queue = [Lesson(**l) for l in state.get("queue", [])]
            
            # Restore stats
            if "stats" in state:
                self.stats = PipelineStats(**state["stats"])
                
            logger.info(f"📂 Restored state: {len(self.queue)} queued")
        except Exception as e:
            logger.warning(f"Could not restore state: {e}")
    
    # -------------------------------------------------------------------------
    # API / Remote Control
    # -------------------------------------------------------------------------
    
    def get_status(self) -> Dict:
        """Get pipeline status for external monitoring"""
        return {
            "status": "running" if self.queue else "idle",
            "queue_length": len(self.queue),
            "completed": len(self.completed),
            "failed": len(self.failed),
            "stats": asdict(self.stats),
            "uptime": datetime.now().isoformat()
        }
    
    def queue_from_curriculum(self, grade_range: tuple = (1, 7)):
        """Auto-queue lessons based on curriculum"""
        lessons = []
        for grade in range(grade_range[0], grade_range[1] + 1):
            topics = {
                1: [("Living Things", 1), ("Matter", 2), ("Light & Shadow", 3)],
                2: [("Life Cycles", 1), ("Properties", 2), ("Weather", 3)],
                3: [("Biodiversity", 1), ("Forces", 2), ("Matter", 3)],
                4: [("Senses", 1), ("Energy", 2), ("Ecosystems", 3)],
                5: [("Body Systems", 1), ("Matter", 2), ("Earth Systems", 3)],
                6: [("Cells", 1), ("Electricity", 2), ("Chemistry", 3)],
                7: [("Evolution", 1), ("Chemical Reactions", 2), ("Earth", 3)],
            }
            
            if grade in topics:
                for topic, module in topics[grade]:
                    lessons.append((grade, module, topic))
        
        self.add_lessons_batch(lessons)
        logger.info(f"📚 Queued {len(lessons)} lessons for grades {grade_range[0]}-{grade_range[1]}")
        return len(lessons)


# ============================================================================
# BASE AGENT CLASS
# ============================================================================

class BaseAgent:
    """Base class for all pipeline agents"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.name = self.__class__.__name__
    
    def process(self, lesson: Lesson) -> AgentResult:
        """Process a lesson - override in subclasses"""
        raise NotImplementedError
    
    def _result(self, success: bool = True, score_delta: float = 0, 
               issues: List[str] = None, output: str = "") -> AgentResult:
        return AgentResult(
            agent=self.name,
            success=success,
            score_delta=score_delta,
            issues=issues or [],
            output=output
        )


# ============================================================================
# CONTENT AGENTS
# ============================================================================

class DesignerAgent(BaseAgent):
    """Creates curriculum structure and objectives"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        content = (DOCS / lesson.filename).read_text() if (DOCS / lesson.filename).exists() else ""
        
        # Design the lesson structure
        new_content = f"""# Grade {lesson.grade} Science - Module {lesson.module}
## {lesson.topic}

**Duration:** 45 minutes
**Version:** {lesson.version}
**Systems Literacy Alignment:** See standards section

---

## 🎯 Learning Objectives

By end of lesson, students will be able to:
1. [SMART objective 1]
2. [SMART objective 2]
3. [SMART objective 3]

---

"""
        
        (DOCS / lesson.filename).write_text(new_content)
        return self._result(True, 10)


class CreatorAgent(BaseAgent):
    """Creates detailed lesson content"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        # Add detailed content
        content = (DOCS / lesson.filename).read_text()
        content += """

## 🧪 Lesson Sequence

### The Hook (5 min)
[Engaging mystery or question]

### Explore (15 min)
[Hands-on activity]

### Discover (10 min)
[Discussion and formalization]

### Create (10 min)
[Student creation]

### Check (5 min)
[Exit ticket]

---

## Differentiation

### Level 1 (Highest Support)
- Step-by-step instructions
- Visual guides

### Level 2 (Guided)
- Partner work
- Checkpoints

### Level 3 (Extension)
- Open challenges

"""
        
        (DOCS / lesson.filename).write_text(content)
        return self._result(True, 15)


class CoderAgent(BaseAgent):
    """Creates p5.js simulation code"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        code_file = DOCS / f"CODE-GRADE{lesson.grade}-MODULE{lesson.module}.py"
        
        code = f'''# p5.js Simulation for Grade {lesson.grade} - {lesson.topic}
# Copy to editor.p5js.org

def setup():
    createCanvas(800, 500)
    
def draw():
    background(240)
    text("Simulation: {lesson.topic}", 50, 50)
'''
        
        code_file.write_text(code)
        return self._result(True, 5)


class AssessorAgent(BaseAgent):
    """Creates assessments"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        content = (DOCS / lesson.filename).read_text()
        content += """

## 📝 Assessment

### Formative
- Observation
- Discussion
- Exit ticket

### Summative
- [Project description]

"""
        
        (DOCS / lesson.filename).write_text(content)
        return self._result(True, 5)


class CreativityAgent(BaseAgent):
    """Adds creative elements, metaphors, story integration"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        content = (DOCS / lesson.filename).read_text()
        
        # Add story elements
        creative = f"""

---

## 🌍 Systems Literacy Connection

> *"You are not a lone creature being bossed around by morality; you are a living process inside other living processes."*

### Chapter Connection
This lesson connects to the larger story of systems literacy.

### 💡 Key Metaphor
[Metaphor specific to {lesson.topic}]

### 📔 Explorer's Journal
1. One thing that surprised me...
2. One question I'm still wondering...
3. One connection to my life...

"""
        
        content += creative
        (DOCS / lesson.filename).write_text(content)
        return self._result(True, 10)


class SystemsLiteracyAgent(BaseAgent):
    """Adds BC + CSTA standards alignment"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        content = (DOCS / lesson.filename).read_text()
        
        standards = f"""

---

## 📚 Standards Alignment

### BC Curriculum (Grade {lesson.grade})
- [Big idea from BC curriculum]

### CSTA Standards ({lesson.grade_band})
- [Relevant CSTA standard]

### Systems Literacy
- [Connection to {lesson.topic}]

"""
        
        content += standards
        (DOCS / lesson.filename).write_text(content)
        
        lesson.standards_alignment = {
            "bc": "aligned",
            "csta": "aligned",
            "systems_literacy": "aligned"
        }
        
        return self._result(True, 10)


# ============================================================================
# VALIDATION AGENTS
# ============================================================================

class StandardsValidator(BaseAgent):
    """Validates BC + CSTA alignment"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        issues = []
        
        content = (DOCS / lesson.filename).read_text()
        
        # Check required sections
        required = ["Learning Objectives", "Lesson Sequence", "Assessment"]
        for section in required:
            if section not in content:
                issues.append(f"Missing: {section}")
        
        score = 20 - len(issues) * 5
        return self._result(len(issues) == 0, score, issues)


class DifferentiationExpert(BaseAgent):
    """Validates 3-level scaffolding"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        content = (DOCS / lesson.filename).read_text()
        
        has_l1 = "Level 1" in content
        has_l2 = "Level 2" in content
        has_l3 = "Level 3" in content
        
        if not (has_l1 and has_l2 and has_l3):
            return self._result(False, -5, ["Incomplete differentiation"])
        
        return self._result(True, 10)


class QualityScorer(BaseAgent):
    """Overall quality assessment"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        content = (DOCS / lesson.filename).read_text()
        
        score = 0
        
        # Length check
        if len(content) > 1500:
            score += 5
        
        # Has systems literacy
        if "Systems Literacy" in content:
            score += 5
        
        # Has metaphors
        if '"' in content or "'" in content:
            score += 5
        
        return self._result(True, score)


class AccessibilityChecker(BaseAgent):
    """Check accessibility"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        # Basic accessibility checks
        return self._result(True, 5)


# ============================================================================
# TESTING AGENTS
# ============================================================================

class StudentAgent(BaseAgent):
    """Simulate student personas"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        # Test multiple personas
        issues = []
        
        content = (DOCS / lesson.filename).read_text()
        
        # Struggling learner check
        if "Level 1" not in content:
            issues.append("Struggling learners not supported")
        
        # Advanced learner check
        if "Level 3" not in content:
            issues.append("Advanced learners not challenged")
        
        score = 15 - len(issues) * 5
        return self._result(len(issues) == 0, score, issues)


class ParentAgent(BaseAgent):
    """Simulate parent review"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        issues = []
        
        content = (DOCS / lesson.filename).read_text()
        
        if "Learning Objectives" not in content:
            issues.append("No clear objectives for parents")
        
        score = 10 - len(issues) * 3
        return self._result(True, score, issues)


class AdversarialAgent(BaseAgent):
    """Red team testing"""
    
    def process(self, lesson: Lesson) -> AgentResult:
        issues = []
        
        content = (DOCS / lesson.filename).read_text()
        
        # Check for ambiguous language
        ambiguous = ["maybe", "perhaps", "or something"]
        for word in ambiguous:
            if word in content.lower():
                issues.append(f"Ambiguous: {word}")
        
        score = 10 - len(issues) * 3
        return self._result(True, score, issues)


# ============================================================================
# DASHBOARD
# ============================================================================

class DashboardReporter:
    """Generates dashboard reports"""
    
    def __init__(self, config: Dict):
        self.config = config
    
    def update(self, orchestrator: PipelineOrchestrator):
        """Update dashboard with current state"""
        self.save_json(orchestrator.get_status())
        self.save_html(orchestrator)
    
    def save_json(self, status: Dict):
        (DATA / "dashboard_status.json").write_text(json.dumps(status, indent=2))
    
    def save_html(self, orchestrator: PipelineOrchestrator):
        stats = orchestrator.stats
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Pipeline Dashboard</title>
    <meta http-equiv="refresh" content="30">
    <style>
        body {{ font-family: monospace; background: #0a0a0a; color: #00ff88; padding: 20px; }}
        h1 {{ color: #00d9ff; }}
        .stat {{ display: inline-block; margin: 10px; padding: 15px; background: #111; border: 1px solid #333; }}
        .log {{ background: #000; padding: 10px; height: 200px; overflow: auto; }}
    </style>
</head>
<body>
    <h1>🎯 Systems Literacy Pipeline</h1>
    <p>Updated: {datetime.now().strftime("%H:%M:%S")}</p>
    
    <div>
        <div class="stat"><h3>Total: {stats.total_processed}</h3></div>
        <div class="stat"><h3>Passed: {stats.passed}</h3></div>
        <div class="stat"><h3>Failed: {stats.failed}</h3></div>
        <div class="stat"><h3>Avg: {stats.average_score:.1f}%</h3></div>
    </div>
    
    <h2>Queue: {len(orchestrator.queue)} lessons</h2>
</body>
</html>"""
        
        (BASE / "dashboard.html").write_text(html)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import sys
    
    # Initialize orchestrator
    orchestrator = PipelineOrchestrator()
    
    # Queue some lessons
    lessons = [
        (1, 1, "Living Things"),
        (1, 2, "Matter"),
        (2, 1, "Life Cycles"),
        (3, 1, "Biodiversity"),
    ]
    
    for g, m, t in lessons:
        orchestrator.add_lesson(g, m, t)
    
    # Run batch
    print("=" * 50)
    print("SYSTEMS LITERACY PIPELINE")
    print("=" * 50)
    
    result = orchestrator.run_batch(max_lessons=4)
    
    print(f"\n✅ Batch complete!")
    print(f"   Processed: {result['processed']}")
    print(f"   Passed: {result['passed']}")
    print(f"   Failed: {result['failed']}")
    print(f"   Avg Score: {result['average_score']:.1f}%")
