# Curriculum Pipeline WORKFLOW - Inspired by autonovel
---
tracker:
  kind: local
  queue_file: data/lesson_queue.json

polling:
  interval_ms: 5000
  max_concurrent_agents: 7

workspace:
  root: workspace

agent:
  command: python3 automation/agent_runner.py
  max_concurrent_agents: 7
  max_retry_backoff_ms: 300000
  turn_timeout_ms: 600000

---

# CURRICULUM PIPELINE - AUTONOVEL STYLE

Inspired by NousResearch/autonovel: autonomous pipeline for writing, revising, and producing quality content.

## Key Principles (from autonovel)

1. **Forward progress over perfection** - Score threshold is good enough (60% = pass)
2. **Loop until quality met** - Foundation score > 7.5 equivalent
3. **Multi-persona evaluation** - Different viewpoints catch different issues
4. **Adversarial testing** - Try to break things
5. **State tracking** - Track debts and propagate changes
6. **Branch-based isolation** - Each lesson is a "branch"

---

## PHASE 0: FOUNDATION (Research + Design)

Like autonovel's foundation phase: build the world/lore before writing.

### Agent 0.1: SeedAnalyzer
Analyze the topic and grade level.
- Identify key concepts
- Map to curriculum standards
- Output: {concepts[], grade_appropriate, scope}

### Agent 0.2: WebResearchAgent
Research best practices and resources.
- Search for teaching approaches
- Find misconceptions
- Identify applications
- Output: {misconceptions[], resources[], applications[], best_practices[]}

### Agent 0.3: CurriculumResearchAgent
Map to BC + CSTA standards.
- BC Big Ideas
- CSTA standards
- Cross-curricular links
- Output: {bc_big_ideas[], bc_standards[], csta_standards[]}

### Agent 0.4: MisconceptionAgent
Identify common student misconceptions.
- Beliefs students have
- Why they believe them
- How to correct
- Output: {misconceptions[{belief, reason, correction}]}

### Agent 0.5: FoundationScore
Evaluate foundation quality.
- Score >= 7.5 equivalent to proceed
- Loop if not met
- Output: {score, issues[], recommendation}

---

## PHASE 1: DESIGN (10 Agents)

Like autonovel's outline phase: create the structure before content.

### Agent 1.1: ObjectiveDesigner
4 SMART objectives aligned to standards.
- Specific, Measurable, Achievable, Relevant, Time-bound
- Output: {objectives[{text, standard, assessment}]}

### Agent 1.2: MaterialCurator
Complete materials list.
- Teacher materials
- Student materials
- Digital resources
- Output: {materials[{item, quantity, notes}]}

### Agent 1.3: HookDesigner
Engaging 2-3 minute opener.
- Mystery or curiosity
- Connects to student lives
- Output: {hook_text, materials, timing}

### Agent 1.4: ActivityArchitect
Lesson sequence.
- Explore (15 min)
- Discover (10 min)
- Create (10 min)
- Check (5 min)
- Output: {activities[{name, duration, description}]}

### Agent 1.5: DifferentiationArchitect
3-level scaffolding.
- Level 1: Highest Support
- Level 2: Guided
- Level 3: Extension
- Output: {levels[{level, strategies[], activities[]}]}

### Agent 1.6: AssessmentDesigner
Formative + summative.
- Observation checklist
- Exit ticket
- Quiz questions
- Output: {formative[], summative{}, quiz[]}

### Agent 1.7: SystemsIntegrationAgent
Connect to Systems Literacy vision.
- Core quote
- Key metaphor
- Systems thinking
- Output: {quote, metaphor, connection}

### Agent 1.8: FirstPeoplesAgent
First Peoples Principles.
- Holistic learning
- Story and place
- Reciprocity
- Output: {principles[]}

### Agent 1.9: CrossCurricularAgent
Connect to other subjects.
- Math, LA, Arts, etc.
- Output: {connections[{subject, activities[]}]}

### Agent 1.10: RealWorldAgent
Real-world connections.
- Careers
- Applications
- Output: {careers[], applications[]}

---

## PHASE 2: CREATE (6 Agents)

Like autonovel's drafting phase: generate the actual content.

### Agent 2.1: TeacherNotesAgent
Comprehensive teacher guide.
- Timing, questions, tips
- Output: {timing{}, questions[], tips[]}

### Agent 2.2: StudentJournalAgent
Explorer's Journal prompts.
- Before/During/After
- Output: {before_prompts[], during_prompts[], after_prompts[]}

### Agent 2.3: ParentGuideAgent
Take-home guide.
- Vocabulary
- Discussion questions
- Home activities
- Output: {vocabulary[], questions[], activities[]}

### Agent 2.4: RubricDesigner
Assessment rubric.
- 4 criteria
- 4 levels
- Output: {criteria[{name, l4, l3, l2, l1}]}

### Agent 2.5: SimulationCoder
p5.js interactive simulation.
- Educational
- Interactive
- Output: {code, description}

### Agent 2.6: ExtensionArchitect
Extension activities.
- Research Challenge
- Creation Challenge
- Connection Quest
- Output: {extensions[{name, description}]}

---

## PHASE 3: EVALUATE (Like autonovel's evaluate.py)

Multi-method evaluation to ensure quality.

### Agent 3.1: StandardsValidator
Validate BC + CSTA alignment.
- All objectives map to standards
- Coverage complete
- Output: {valid, coverage_score, missing[]}

### Agent 3.2: QualityValidator
Content quality check.
- Length > 3000 chars
- All sections present
- Language appropriate
- Output: {valid, quality_score, issues[]}

### Agent 3.3: AccessibilityValidator
Accessibility check.
- Simple language
- Clear structure
- Output: {valid, score, concerns[]}

### Agent 3.4: CulturalValidator
Cultural sensitivity.
- First Peoples present
- Inclusive
- Output: {valid, score, notes}

---

## PHASE 4: TEST / QA (Like autanovel's reader_panel)

Multi-persona testing - like autonovel's 4-persona panel.

### Agent 4.1: StudentTester
Simulate student personas (5 types).
- Struggling learner
- Average student
- Advanced student
- ESL student
- Bored student
- Output: {personas[{name, issues[], score}]}

### Agent 4.2: ParentTester
Simulate parent personas (4 types).
- Reviewer (checks quality)
- Questioner (asks why)
- Comparer (vs other curricula)
- Critic (finds flaws)
- Output: {personas[{name, issues[], score}]}

### Agent 4.3: TeacherTester
Practical teacher use test.
- Can teach from this?
- Clear enough?
- Practical?
- Output: {score, issues[], suggestions[]}

### Agent 4.4: AdversarialTester (Like autonovel's adversarial_edit)
Red team - try to break things.
- Find ambiguous instructions
- Edge cases
- Common failures
- Output: {issues[], score, severity[]}

---

## PHASE 5: REVISION (Like autonovel's revision loop)

If QA fails, iterate until quality met.

### Agent 5.1: RevisionBriefGenerator
Generate revision brief from QA feedback.
- Identify top issues
- Prioritize by severity
- Output: {briefs[{issue, priority, suggested_fix}]}

### Agent 5.2: RevisionExecutor
Apply revisions.
- Fix identified issues
- Maintain what works
- Output: {changes_made, new_issues}

---

## PHASE 6: FINALIZE

### Agent 6.1: FinalAssembler
Combine all components.
- Validate all phases passed
- Check score >= 60%
- Output: {valid, lesson_file}

### Agent 6.2: GitCommitter
Commit and push.
- Proper commit message
- Tag version
- Push to remote
- Output: {commit_hash, remote_url}

---

## SCORING SYSTEM (Inspired by autonovel)

| Phase | Max Score | Threshold |
|-------|-----------|-----------|
| Foundation | 50 | 37.5 (75%) |
| Design | 100 | 75 (75%) |
| Create | 60 | 45 (75%) |
| Evaluate | 40 | 30 (75%) |
| Test/QA | 40 | 30 (75%) |
| **TOTAL** | **290** | **217.5 (75%)** |

**Forward progress over perfection: 60% = pass**

---

## ITERATION LOOPS (From autonovel)

1. **Foundation Loop**: Loop until foundation_score > 7.5
2. **Design Loop**: Loop until design complete
3. **QA Loop**: Loop until QA score >= 60%
4. **Revision Loop**: If QA fails, revision until pass

**Key autonovel insight**: "Forward progress over perfection. 6.0 is good enough."

---

## STATE TRACKING

Track in state.json:
- current_phase
- iteration
- scores per phase
- debts (propagation issues)
- retry_count

---

## OUTPUT STRUCTURE

For each lesson:
```
workspace/lesson-{id}/
├── phase0-foundation/
│   ├── seed_analyzer.json
│   ├── web_research.json
│   ├── curriculum.json
│   └── misconceptions.json
├── phase1-design/
│   ├── objectives.json
│   ├── materials.json
│   ├── hook.json
│   └── ... (10 files)
├── phase2-create/
│   ├── teacher_notes.json
│   ├── student_journal.json
│   └── ... (6 files)
├── phase3-evaluate/
│   └── ... (4 files)
├── phase4-test/
│   └── ... (4 files)
└── lesson.md (final)
```

---

## SUCCESS CRITERIA

A lesson is complete when:
1. All phases executed
2. Quality score >= 60%
3. All QA personas pass (score >= 60%)
4. Committed and pushed to GitHub

**Like autonovel: Forward progress over perfection.**
