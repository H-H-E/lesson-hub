#!/usr/bin/env python3
"""
Systems Literacy Curriculum Agent
==================================

This agent generates curriculum aligned with:
1. BC (British Columbia) Science Curriculum
2. CSTA K-12 Computer Science Standards
3. Systems Literacy Vision ("You Are Not An Atom")
4. First Peoples Principles of Learning

The philosophical foundation:
"You are not a lone creature being bossed around by morality; you are a 
living process inside other living processes, and learning to see that is 
both an introduction to science and an introduction to code."
"""

from pathlib import Path
from typing import Dict, List, Optional
import json
import hashlib

BASE = Path("/root/.openclaw/workspace/lesson-hub")
DOCS = BASE / "docs"

# ============================================================================
# STANDARDS ALIGNMENT
# ============================================================================

# BC Science Curriculum by Grade
BC_CURRICULUM = {
    "K": {
        "big_ideas": [
            "All living things have something in common",
            "Matter changes in different ways",
            "Light and sound have patterns",
        ],
        "core_competencies": ["Communication", "Thinking", "Personal & Social"]
    },
    "1": {
        "big_ideas": [
            "Living things have features and behaviors that help them survive",
            "Matter has measurable properties",
            "Light and sound are types of energy",
        ],
        "topics": ["Living things", "Matter", "Light and Shadow", "Sky patterns"]
    },
    "2": {
        "big_ideas": [
            "Living things have life cycles",
            "Matter has properties that can change",
            "Earth and sky change over time",
        ],
        "topics": ["Life cycles", "Properties of matter", "Climate/weather"]
    },
    "3": {
        "big_ideas": [
            "Living things are diverse, can be grouped, and interact",
            "Matter is useful because of its properties",
            "Energy can be transferred and transformed",
        ],
        "topics": ["Biodiversity", "Matter", "Energy"]
    },
    "4": {
        "big_ideas": [
            "All living things sense and respond to their environment",
            "Matter has molecular structure",
            "Energy can be converted",
        ],
        "topics": ["Senses", "Light", "Sound", "Energy"]
    },
    "5": {
        "big_ideas": [
            "Multi-cellular organisms rely on internal systems",
            "Matter is conserved",
            "Earth's systems change over time",
        ],
        "topics": ["Body systems", "Matter", "Earth systems"]
    },
    "6": {
        "big_ideas": [
            "Multi-cellular organisms have organ systems",
            "Matter is made of particles",
            "Electricity is a form of energy",
        ],
        "topics": ["Cells", "Matter", "Electricity"]
    },
    "7": {
        "big_ideas": [
            "Evolution occurs over time",
            "Matter is conserved in chemical reactions",
            "Earth's geosphere changes through cycling and energy",
        ],
        "topics": ["Evolution", "Chemistry", "Geology"]
    },
    "8": {
        "big_ideas": [
            "Cells are basic units of life",
            "Chemical reactions release energy",
            "Earth's water cycles",
        ],
        "topics": ["Cell biology", "Chemical reactions", "Water"]
    },
    "9": {
        "big_ideas": [
            "Cells come from cells",
            "Matter is transformed in chemical reactions",
            "Climate change has multiple causes",
        ],
        "topics": ["Cell division", "Chemical reactions", "Climate"]
    },
    "10": {
        "big_ideas": [
            "DNA is the basis for inheritance",
            "Chemical reactions involve electron transfer",
            "Energy conversions affect ecosystems",
        ],
        "topics": ["Genetics", "Electrochemistry", "Ecosystems"]
    }
}

# CSTA Standards by Grade Band
CSTA_STANDARDS = {
    "K-2": [
        "1A-AP-08: Model daily processes by creating algorithms",
        "1A-AP-09: Create programs using sequencing",
        "1A-AP-10: Decompose steps needed to solve problems",
        "1A-DA-06: Collect and present data in visual formats",
        "1A-DA-07: Identify patterns in data",
        "1A-CS-01: Select appropriate tools to express ideas",
        "1A-IC-13: Identify ways people use computing in daily life",
    ],
    "3-5": [
        "1B-AP-08: Create programs using loops",
        "1B-AP-09: Create programs using event detection",
        "1B-AP-11: Create programs using variables",
        "1B-DA-06: Collect, organize, represent data",
        "1B-DA-08: Identify patterns to make predictions",
        "1B-CS-01: Demonstrate how hardware and software work together",
        "1B-IC-15: Discuss computing technologies that changed the world",
    ],
    "6-8": [
        "2-AP-10: Use flowcharts for algorithm design",
        "2-AP-11: Create programs with nested loops",
        "2-AP-12: Design programs with procedures",
        "2-DA-06: Describe stored data formats",
        "2-NI-04: Model how data is routed across networks",
        "2-IC-16: Compare computing impacts across cultures",
    ],
    "9-10": [
        "3A-AP-10: Use lists to simplify solutions",
        "3A-AP-11: Evaluate algorithms for efficiency",
        "3A-DA-06: Transform data to remove noise",
        "3A-CS-01: Explain how abstractions hide details",
        "3A-IC-16: Compare beneficial and harmful effects",
    ]
}

# ============================================================================
# SYSTEMS LITERACY UNITS (from PDF vision)
# ============================================================================

SYSTEMS_UNITS = {
    1: {
        "title": "The Self Is Older Than You Think",
        "theme": "cosmic_origin",
        "topics": ["The sun as energy source", "Formation of Earth", "Deep time and scale", "Seasons and cycles"],
        "key_insight": "Your life is downstream of systems that existed long before you",
        "metaphor": "You are made of star stuff - the universe is in you"
    },
    2: {
        "title": "Life Is Organized Matter With Memory", 
        "theme": "biological_systems",
        "topics": ["What life is", "Evolution basics", "Cells as machines", "DNA as code"],
        "key_insight": "Biology is process layered on process. Life remembers what worked.",
        "metaphor": "DNA is a recipe book written by billions of years of testing"
    },
    3: {
        "title": "The Body Is Not A Thing, It's A Running Program",
        "theme": "bodily_systems",
        "topics": ["Homeostasis", "Feedback loops", "Habit formation", "Stress as signal"],
        "key_insight": "Who you are is stabilized by repeated loops. Habits are your code.",
        "metaphor": "Your body is a computer running software written by evolution"
    },
    4: {
        "title": "The Mind Is Shaped By Systems",
        "theme": "cognitive_systems",
        "topics": ["Neuroplasticity", "Social contagion", "Information environments", "Incentives"],
        "key_insight": "Your thoughts are not purely your own - they're shaped by systems",
        "metaphor": "Your brain is a village, not a king"
    },
    5: {
        "title": "Families, Communities, Institutions",
        "theme": "social_systems",
        "topics": ["Emergence", "Cultural inheritance", "Institutional feedback", "Coordination"],
        "key_insight": "You exist inside overlapping systems. Your fate is tied to others.",
        "metaphor": "Society is an organism made of organisms"
    },
    6: {
        "title": "Ecologies And Economies",
        "theme": "economic_systems",
        "topics": ["Resource flows", "Predator-prey", "Tragedy of the commons", "Networks"],
        "key_insight": "Cooperation isn't moralizing - it's engineering for survival",
        "metaphor": "The economy is an ecosystem, not a machine"
    },
    7: {
        "title": "The Computational Revelation",
        "theme": "computational_literacy",
        "topics": ["What is computation", "From analog to digital", "Simulation as understanding", "Building systems"],
        "key_insight": "Code is not a nerd priesthood - it's a language for describing process",
        "metaphor": "Programming is thinking about thinking"
    }
}

# ============================================================================
# CURRICULUM GENERATOR
# ============================================================================

class SystemsLiteracyCurriculumAgent:
    """
    Generates curriculum that aligns:
    - BC Science Standards
    - CSTA Computer Science Standards  
    - Systems Literacy Vision (the PDF)
    - First Peoples Principles of Learning
    """
    
    def __init__(self, grade: int):
        self.grade = grade
        self.grade_band = self._get_grade_band()
        self.bc_curriculum = BC_CURRICULUM.get(str(grade), BC_CURRICULUM["1"])
        self.csta_standards = self._get_csta_standards()
        self.systems_unit = self._get_systems_unit()
        
    def _get_grade_band(self) -> str:
        """Map grade to CSTA grade band"""
        if self.grade <= 2:
            return "K-2"
        elif self.grade <= 5:
            return "3-5"
        elif self.grade <= 8:
            return "6-8"
        else:
            return "9-10"
            
    def _get_csta_standards(self) -> List[str]:
        """Get CSTA standards for this grade band"""
        return CSTA_STANDARDS.get(self.grade_band, [])
        
    def _get_systems_unit(self) -> Dict:
        """Map grade to systems literacy unit"""
        # Map grades 1-12 to units 1-7 (cycling)
        unit_num = ((self.grade - 1) % 7) + 1
        return SYSTEMS_UNITS.get(unit_num, SYSTEMS_UNITS[1])
    
    def generate_lesson(self, module_num: int, topic: str) -> str:
        """Generate a complete lesson aligned to all standards"""
        
        bc_topics = self.bc_curriculum.get("topics", [])
        systems_topics = self.systems_unit.get("topics", [])
        
        # Build the lesson
        lesson = f"""# Grade {self.grade} Science - Module {module_num}
## {topic}

*Systems Literacy Curriculum - Aligned to BC & CSTA Standards*

---

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

1. [SMART objective 1 aligned to BC big ideas]
2. [SMART objective 2 aligned to CSTA standards]
3. [SMART objective 3 connected to systems thinking]

---

## 📚 Standards Alignment

### BC Curriculum (Grade {self.grade})
**Big Ideas:**
{chr(10).join(f"- {idea}" for idea in self.bc_curriculum.get("big_ideas", []))}

**Core Competencies:**
{chr(10).join(f"- {cc}" for cc in self.bc_curriculum.get("core_competencies", []))}

### CSTA Standards ({self.grade_band})
{chr(10).join(f"- {std}" for std in self.csta_standards[:3])}

---

## 🌍 Systems Literacy Connection

### Chapter {self.systems_unit.get('title', 'Systems Thinking')}

**Key Insight:** {self.systems_unit.get('key_insight', '')}

**Think About It:**
> *" {self.systems_unit.get('metaphor', '')} "*

This lesson connects to the larger story: *You are not an isolated atom — you are a process inside other processes.*

---

## 🧪 Lesson Sequence

### The Hook (5 min)
🎭 [Engaging mystery that connects to student's life]

### Explore (15 min)
🔬 [Hands-on activity where students discover patterns]

### Discover (10 min)
💡 [Students share findings, teacher formalizes the science]

### Create (10 min)
🎨 [Student expresses learning through creation]

### Check (5 min)
✅ [Exit ticket to assess understanding]

---

## 🔄 Differentiation

### Level 1 (Highest Support)
- Step-by-step instructions
- Visual guides
- Teacher proximity

### Level 2 (Guided)
- Partner work
- Checkpoints
- Choice in how to demonstrate learning

### Level 3 (Extension)
- Open challenges
- Research extension
- Peer teaching

---

## 🖥️ Computational Thinking Connection

Students will practice:
- **Decomposition:** Breaking down the topic into parts
- **Pattern Recognition:** Finding systems and cycles
- **Abstraction:** Focusing on what's important
- **Algorithm Design:** Creating step-by-step procedures

### Coding Connection
This lesson connects to CSTA standards:
```
{chr(10).join(self.csta_standards[:2])}
```

---

## 🌿 First Peoples Principles of Learning

- Learning is holistic, reflexive, reflective, experiential, and relational
- Learning involves patience and time
- Learning requires exploration of one's identity
- Learning is embedded in memory, history, and story
- Learning recognizes the role of indigenous knowledge

---

## 📝 Assessment

### Formative
- Observation during exploration
- Discussion contributions
- Exit ticket

### Summative
- [Project or presentation description]

---

## 🔗 Connections to Other Systems

This lesson connects to:
- **Your body:** [How the topic relates to personal biology]
- **Your community:** [How it relates to society]
- **The planet:** [How it relates to ecology]
- **The future:** [How it prepares students for what's next]

---

## 📔 Explorer's Journal Prompt

In your Explorer's Journal, write or draw:
1. One thing that surprised me about {topic}...
2. One question I'm still wondering...
3. One way {topic} connects to my life...

---

*Generated by Systems Literacy Curriculum Agent*
*Aligned to BC Curriculum, CSTA Standards, and Systems Literacy Vision*
"""
        
        return lesson
    
    def generate_unit_overview(self) -> str:
        """Generate a unit overview with all standards aligned"""
        
        return f"""# Grade {self.grade} Systems Literacy Unit Overview

## The Story So Far...

Welcome to Chapter **{self.systems_unit['title']}**!

You've been on an amazing journey understanding how you're connected to:
- 🌟 The cosmos (where you came from)
- 🧬 Biology (what you're made of)
- 🏠 Society (who you're with)
- 💻 Code (how you can understand it all)

## This Unit's Big Ideas

### From BC Curriculum:
{chr(10).join(f"- {idea}" for idea in self.bc_curriculum['big_ideas'])}

### From CSTA Standards:
{chr(10).join(f"- {std}" for std in self.csta_standards[:5])}

### From Systems Literacy:
**Theme:** {self.systems_unit['theme']}

**Key Insight:** {self.systems_unit['key_insight']}

## Your Journey This Unit

| Week | Topic | Systems Connection | Coding Connection |
|------|-------|-------------------|-------------------|
| 1 | [Topic 1] | {self.systems_unit['topics'][0] if len(self.systems_unit['topics']) > 0 else 'Systems basics'} | Algorithms |
| 2 | [Topic 2] | {self.systems_unit['topics'][1] if len(self.systems_unit['topics']) > 1 else 'Patterns'} | Data |
| 3 | [Topic 3] | {self.systems_unit['topics'][2] if len(self.systems_unit['topics']) > 2 else 'Connections'} | Variables |
| 4 | [Topic 4] | {self.systems_unit['topics'][3] if len(self.systems_unit['topics']) > 3 else 'Emergence'} | Loops |

## The Quest

Complete all lessons and challenges to become a Systems Explorer!

## Your Legacy

How will you use what you learn to help your community?
"""


# ============================================================================
# STANDARDS CROSSWALK
# ============================================================================

def generate_crosswalk(grade: int) -> str:
    """Generate a standards crosswalk for a grade"""
    
    agent = SystemsLiteracyCurriculumAgent(grade)
    
    crosswalk = f"""# Standards Crosswalk - Grade {grade}

## BC Science + CSTA CS + Systems Literacy

| BC Big Idea | CSTA Standard | Systems Unit | Lesson Focus |
|-------------|---------------|--------------|--------------|
"""
    
    for i, bc_idea in enumerate(agent.bc_curriculum.get('big_ideas', [])):
        csta_std = agent.csta_standards[i] if i < len(agent.csta_standards) else "TBD"
        systems_topic = agent.systems_unit.get('topics', ['N/A'])[i % 4]
        
        crosswalk += f"| {bc_idea} | {csta_std} | {systems_topic} | Module {i+1} |\n"
    
    return crosswalk


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        grade = int(sys.argv[1])
    else:
        grade = 1
        
    agent = SystemsLiteracyCurriculumAgent(grade)
    
    print(f"=== Systems Literacy Curriculum Agent ===")
    print(f"Grade: {grade}")
    print(f"Grade Band: {agent.grade_band}")
    print(f"\nSystems Unit: {agent.systems_unit['title']}")
    print(f"Key Insight: {agent.systems_unit['key_insight']}")
    print(f"\nBC Topics: {agent.bc_curriculum.get('topics', [])}")
    print(f"\nCSTA Standards ({len(agent.csta_standards)} total):")
    for std in agent.csta_standards[:3]:
        print(f"  - {std}")
