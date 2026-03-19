# Curriculum Pipeline WORKFLOW
---
tracker:
  kind: local
  queue_file: data/lesson_queue.json

polling:
  interval_ms: 10000
  max_concurrent_agents: 7

workspace:
  root: workspace

agent:
  command: python3 automation/agent_runner.py
  max_concurrent_agents: 7
  max_retry_backoff_ms: 300000
  turn_timeout_ms: 600000

hooks:
  after_create: echo "Workspace created for {issue_id}"
  before_run: echo "Starting agent for {issue_id}"
  after_run: echo "Agent completed for {issue_id}"

---

# CURRICULUM GENERATION WORKFLOW

You are orchestrating a comprehensive curriculum generation pipeline for K-12 science education. Your task is to generate high-quality, standards-aligned lessons using multiple specialized agents.

## PHASE 1: RESEARCH (3 Agents)

### Agent 1.1: WebResearchAgent
Research current best practices, educational resources, and teaching approaches for this topic.
- Search for relevant educational content
- Find common misconceptions
- Identify real-world applications
- Note: Output JSON with fields: {misconceptions[], resources[], applications[], best_practices[]}

### Agent 1.2: CurriculumResearchAgent  
Map the topic to BC (British Columbia) science curriculum and CSTA Computer Science standards.
- Identify BC Big Ideas
- List specific learning standards
- Note CSTA standards that apply
- Output: {bc_big_ideas[], bc_standards[], csta_standards[]}

### Agent 1.3: MisconceptionAgent
Research common student misconceptions for this specific topic.
- Identify 5-10 common misconceptions
- Explain why students believe these
- Provide strategies to address
- Output: {misconceptions[{belief, reason, correction}]}

## PHASE 2: DESIGN (10 Agents)

### Agent 2.1: ObjectiveDesigner
Create 4 SMART learning objectives.
- Specific, Measurable, Achievable, Relevant, Time-bound
- Align to BC curriculum big ideas
- Output: {objectives[{text, standard, assessment_method}]}

### Agent 2.2: MaterialCurator
Curate complete materials list.
- Teacher materials (with quantities)
- Student materials
- Digital resources
- Safety considerations
- Output: {materials[{item, quantity, notes}]}

### Agent 2.3: HookDesigner
Design engaging 2-3 minute opening hook.
- Mystery or curiosity hook
- Connects to student lives
- Creates genuine questions
- Output: {hook_text, materials_needed, timing}

### Agent 2.4: ActivityArchitect
Design complete lesson sequence.
- Explore (15 min): Hands-on discovery
- Discover (10 min): Discussion
- Create (10 min): Student creation
- Check (5 min): Exit ticket
- Output: {activities[{name, duration, description, materials, teacher_role, student_role}]}

### Agent 2.5: DifferentiationArchitect
Create 3-level differentiation.
- Level 1: Highest Support
- Level 2: Guided/Expected
- Level 3: Extension
- Output: {levels[{level, description, strategies[], activities[]}]}

### Agent 2.6: AssessmentDesigner
Create assessments.
- Formative: observation, exit ticket, discussion
- Summative: project option
- Quiz questions
- Output: {formative[], summative{}, quiz_questions[]}

### Agent 2.7: SystemsIntegrationAgent
Connect to Systems Literacy vision.
- Core quote integration
- Key metaphor for this topic
- Systems thinking connection
- Output: {quote, metaphor, systems_connection, thinking_questions[]}

### Agent 2.8: FirstPeoplesAgent
Integrate First Peoples Principles of Learning.
- 4-5 specific connections
- Place-based learning
- Indigenous perspectives
- Output: {principles[{name, connection, activity}]}

### Agent 2.9: CrossCurricularAgent
Map cross-curricular connections.
- Mathematics
- Language Arts
- Arts Education
- Output: {connections[{subject, activities[]}]}

### Agent 2.10: RealWorldAgent
Connect to real-world applications and careers.
- 5-6 relevant careers
- Daily life applications
- Output: {careers[], applications[]}

## PHASE 3: CREATE (6 Agents)

### Agent 3.1: TeacherNotesAgent
Create comprehensive teacher guide.
- Timing guide
- Common questions
- Tips and tricks
- Misconceptions to watch
- Output: {timing{}, questions[], tips[]}

### Agent 3.2: StudentJournalAgent
Create Explorer's Journal prompts.
- Before section
- During section
- After section
- Output: {before_prompts[], during_prompts[], after_prompts[]}

### Agent 3.3: ParentGuideAgent
Create take-home parent guide.
- Vocabulary
- Discussion questions
- Home activities
- Output: {vocabulary[], questions[], activities[]}

### Agent 3.4: RubricDesigner
Create assessment rubric.
- 4 criteria
- 4 levels (4,3,2,1)
- Output: {criteria[{name, level4, level3, level2, level1}]}

### Agent 3.5: SimulationCoder
Create p5.js interactive simulation.
- Educational and interactive
- Works in editor.p5js.org
- Commented code
- Output: {code, description, instructions}

### Agent 3.6: ExtensionArchitect
Design extension activities.
- Research Challenge
- Creation Challenge
- Connection Quest
- Output: {extensions[{name, description, output}]}

## PHASE 4: VALIDATE (4 Agents)

### Agent 4.1: StandardsValidator
Validate BC + CSTA alignment.
- Check all objectives map to standards
- Ensure coverage
- Output: {valid, coverage_score, missing[]}

### Agent 4.2: QualityValidator
Validate content quality.
- Length check (>3000 chars)
- Has all required sections
- Language appropriate
- Output: {valid, quality_score, issues[]}

### Agent 4.3: AccessibilityValidator
Validate accessibility.
- Simple language
- Clear structure
- Inclusive
- Output: {valid, score, concerns[]}

### Agent 4.4: CulturalValidator
Validate cultural sensitivity.
- First Peoples integration present
- Inclusive language
- Output: {valid, score, notes}

## PHASE 5: TEST - QA AGENTS (4 Agents)

### Agent 5.1: StudentTester
Simulate different student personas.
- Struggling learner
- Average student
- Advanced student
- ESL student
- Student with attention issues
- Output: {personas[{name, issues[], score}]}

### Agent 5.2: ParentTester
Simulate parent review.
- Reviewer: checks quality
- Questioner: asks why
- Comparer: vs other curricula
- Critic: finds flaws
- Output: {personas[{name, issues[], score}]}

### Agent 5.3: TeacherTester
Simulate teacher use.
- Can they teach from this?
- Clear enough?
- Practical?
- Output: {score, issues[], suggestions[]}

### Agent 5.4: AdversarialTester
Red team testing.
- Try to break things
- Find ambiguous instructions
- Edge cases
- Output: {issues[], score, severity[]}

## PHASE 6: DEPLOY

### Final Assembly
Combine all outputs into a single lesson file.
- Validate all phases passed
- Score >= 60 to deploy
- Git commit with proper message
- Push to remote

## SUCCESS CRITERIA

A lesson is complete when:
1. All 6 phases completed
2. Quality score >= 60
3. All validation agents pass
4. All testing agents pass (score >= 60)
5. Deployed to GitHub

## OUTPUT FORMAT

Each agent outputs JSON to their workspace file:
- Phase 1: workspace/research/{agent}.json
- Phase 2: workspace/design/{agent}.json
- Phase 3: workspace/create/{agent}.json
- Phase 4: workspace/validate/{agent}.json
- Phase 5: workspace/test/{agent}.json

Final lesson: docs/LESSON-GRADE{grade}-MODULE{module}.md
