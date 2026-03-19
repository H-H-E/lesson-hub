# Lesson Hub - Interactive Curriculum System

## Quick Start

```bash
# Start the web server
cd /root/.openclaw/workspace/lesson-hub
python3 server.py

# Access at http://localhost:8080
```

## Modes

### Student Mode
- `/student/` - Interactive lessons with p5.js/three.js simulations
- View progress, complete quizzes, earn badges
- URL: `http://localhost:8080/student/`

### Teacher Mode  
- `/teacher/` - Lesson scripts, talking points, discussion questions
- View student progress, assessment prompts
- URL: `http://localhost:8080/teacher/`

## Automation

### Run Overnight Pipeline
```bash
# Process all pending lessons
python3 automation/run_overnight.py

# Or run specific stage:
python3 automation/run_overnight.py --stage design
python3 automation/run_overnight.py --stage create
python3 automation/run_overnight.py --stage test
python3 automation/run_overnight.py --stage review
```

### Schedule (cron)
```bash
# Run every night at 6 PM
0 18 * * * cd /root/.openclaw/workspace/lesson-hub && python3 automation/run_overnight.py
```

## Project Structure

```
lesson-hub/
├── server.py              # Web server
├── index.html             # Landing page (mode selector)
├── public/
│   ├── student/          # Student mode static files
│   │   ├── index.html
│   │   ├── lesson.html
│   │   └── styles.css
│   └── teacher/          # Teacher mode static files
│       ├── index.html
│       ├── lesson-script.html
│       └── styles.css
├── scripts/              # Teacher scripts (generated)
│   └── lesson_{id}_teacher.md
├── templates/            # HTML templates
│   ├── student_lesson.html
│   └── teacher_script.html
├── data/                 # Curriculum data
│   ├── curriculum.json
│   ├── lessons.json
│   └── reviews.json
└── automation/
    ├── pipeline.py       # Main pipeline orchestrator
    ├── designers.py      # Curriculum Designer agent
    ├── creators.py       # Content Creator agent
    ├── testers.py        # Lesson Tester agent
    └── reviewers.py      # Reviewer agent
```

## Agent Team

1. **Curriculum Designer** - Creates lesson structure
2. **Content Creator** - Builds p5.js/three.js simulations
3. **Lesson Tester** - Simulates tutor/student dialogue
4. **Reviewer** - Scores and approves lessons

## Current Status

- Lessons completed: 0
- Lessons in progress: 0
- Last run: Never
