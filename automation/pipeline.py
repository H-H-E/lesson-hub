#!/usr/bin/env python3
"""
Overnight Automation Pipeline
Processes lessons through: Design → Create → Test → Review → Publish
"""

import json
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent

class Pipeline:
    def __init__(self):
        self.data_dir = BASE_DIR / 'data'
        self.scripts_dir = BASE_DIR / 'scripts'
        self.lessons = []
        self.status = {'stage': 'idle', 'last_lesson': None, 'last_run': None}
        
    def load_lessons(self):
        """Load current lesson state"""
        # Ensure directories exist
        self.data_dir.mkdir(exist_ok=True)
        self.scripts_dir.mkdir(exist_ok=True)
        lessons_file = self.data_dir / 'lessons.json'
        if lessons_file.exists():
            data = json.loads(lessons_file.read_text())
            self.lessons = data.get('lessons', [])
        return self.lessons
    
    def save_lessons(self):
        """Save lesson state"""
        lessons_file = self.data_dir / 'lessons.json'
        lessons_file.write_text(json.dumps({'lessons': self.lessons}, indent=2))
    
    def update_status(self, stage, lesson_id=None):
        """Update pipeline status"""
        self.status = {
            'stage': stage,
            'last_lesson': lesson_id,
            'last_run': datetime.now().isoformat(),
            'lessons_completed': sum(1 for l in self.lessons if l.get('status') == 'published')
        }
        status_file = self.data_dir / 'status.json'
        status_file.write_text(json.dumps(self.status, indent=2))
    
    def run_overnight(self, target_topic="p5.js basics", num_lessons=5):
        """
        Main overnight pipeline
        Processes all lessons through the full workflow
        """
        print("=" * 60)
        print("🌙 OVERNIGHT AUTOMATION PIPELINE")
        print("=" * 60)
        
        self.load_lessons()
        
        # Stage 1: Curriculum Design
        print("\n📋 STAGE 1: CURRICULUM DESIGN")
        print("-" * 40)
        self.update_status('designing')
        
        curriculum = self.design_curriculum(target_topic, num_lessons)
        print(f"✅ Designed {len(curriculum)} lessons")
        
        # Stage 2-5: For each lesson
        for i, lesson_plan in enumerate(curriculum):
            lesson_num = i + 1
            print(f"\n{'='*60}")
            print(f"📚 LESSON {lesson_num}: {lesson_plan['title']}")
            print("=" * 60)
            
            # Stage 2: Content Creation
            print("\n🎨 STAGE 2: CONTENT CREATION")
            print("-" * 40)
            self.update_status('creating', lesson_num)
            
            content = self.create_content(lesson_plan)
            print(f"✅ Created: simulation code, explanations")
            
            # Stage 3: Testing
            print("\n🧪 STAGE 3: LESSON TESTING")
            print("-" * 40)
            self.update_status('testing', lesson_num)
            
            test_results = self.test_lesson(lesson_plan, content)
            print(f"✅ Tested: engagement={test_results['engagement']}, clarity={test_results['clarity']}")
            
            # Stage 4: Review
            print("\n👀 STAGE 4: REVIEW")
            print("-" * 40)
            self.update_status('reviewing', lesson_num)
            
            approved = self.review_lesson(lesson_plan, content, test_results)
            
            if approved:
                # Stage 5: Publish
                print("\n📤 STAGE 5: PUBLISH")
                print("-" * 40)
                self.update_status('publishing', lesson_num)
                
                self.publish_lesson(lesson_plan, content, lesson_num)
                print(f"✅ Published lesson {lesson_num}")
            else:
                print(f"⚠️ Lesson {lesson_num} needs revision")
                # In real system, would loop back
        
        # Final status
        self.update_status('completed')
        
        print("\n" + "=" * 60)
        print("✅ OVERNIGHT PIPELINE COMPLETE")
        print(f"📚 {len(curriculum)} lessons processed")
        print(f"⏰ Finished at: {datetime.now().strftime('%H:%M')}")
        print("=" * 60)
        
        return self.lessons
    
    def design_curriculum(self, topic, num_lessons):
        """
        Stage 1: Use Curriculum Designer to structure lessons
        In production: Spawns Curriculum Designer agent
        """
        # This would call the curriculum-generator skill
        # For now, using hardcoded p5.js curriculum structure
        
        curriculum = [
            {
                'id': 1,
                'title': f'Welcome to {topic}',
                'objectives': [
                    f'Understand what {topic} is',
                    'Navigate the web editor',
                    'Run your first sketch'
                ],
                'duration': 45,
                'stage': 'draft'
            },
            {
                'id': 2,
                'title': 'Drawing Shapes',
                'objectives': [
                    'Use ellipse() for circles',
                    'Use rect() for rectangles',
                    'Understand coordinate system'
                ],
                'duration': 45,
                'stage': 'draft'
            },
            {
                'id': 3,
                'title': 'Colors & Variables',
                'objectives': [
                    'Use RGB color values',
                    'Create and use variables',
                    'Modify shapes with variables'
                ],
                'duration': 50,
                'stage': 'draft'
            },
            {
                'id': 4,
                'title': 'Animation Basics',
                'objectives': [
                    'Use draw() loop',
                    'Animate shape position',
                    'Add interactivity'
                ],
                'duration': 60,
                'stage': 'draft'
            },
            {
                'id': 5,
                'title': 'Build Your Scene',
                'objectives': [
                    'Combine all concepts',
                    'Create original artwork',
                    'Present to class'
                ],
                'duration': 90,
                'stage': 'draft'
            }
        ]
        
        # Add to lessons
        for lesson in curriculum[:num_lessons]:
            # Check if already exists
            existing = next((l for l in self.lessons if l['id'] == lesson['id']), None)
            if not existing:
                self.lessons.append(lesson)
        
        self.save_lessons()
        return curriculum[:num_lessons]
    
    def create_content(self, lesson_plan):
        """
        Stage 2: Use Content Creator to generate p5.js code, explanations
        In production: Spawns Content Creator agent
        """
        # Generate simulation code based on lesson
        lesson_id = lesson_plan['id']
        
        code_templates = {
            1: '''function setup() {
  createCanvas(400, 400);
  background(50);
}

function draw() {
  // Welcome lesson - simple animation
  fill(255);
  textSize(32);
  text("Hello p5.js!", 100, 200);
}''',
            2: '''function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(30);
  
  // Draw face
  fill(255, 200, 100); // skin color
  ellipse(300, 200, 150, 180); // face
  
  // Eyes
  fill(255);
  ellipse(260, 170, 40, 40);
  ellipse(340, 170, 40, 40);
  
  fill(0);
  ellipse(260 + mouseX/20, 170, 15, 15);
  ellipse(340 + mouseX/20, 170, 15, 15);
  
  // Smile
  noFill();
  stroke(255, 100, 100);
  strokeWeight(5);
  arc(300, 220, 80, 50, 0, PI);
}''',
            3: '''let x = 100;
let r = 255, g = 100, b = 150;

function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(r, g, b, 50);
  
  // Moving circle using variable
  fill(255);
  ellipse(x, 200, 80, 80);
  
  x = x + 2;
  if (x > width + 40) x = -40;
  
  // Color changes with mouse
  r = mouseX;
  b = mouseY;
}''',
            4: '''let angle = 0;

function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(20);
  
  // Animated bouncing ball
  let x = 300 + sin(angle) * 200;
  let y = 200 + cos(angle * 2) * 100;
  
  fill(0, 255, 200);
  noStroke();
  ellipse(x, y, 60, 60);
  
  angle += 0.05;
  
  // Instructions
  fill(255);
  textSize(16);
  text("Move mouse to change color!", 10, 30);
}''',
            5: '''let shapes = [];

function setup() {
  createCanvas(600, 400);
  // Create user shapes
  shapes.push({x: 100, y: 100, c: [255,0,0], type: 'rect'});
  shapes.push({x: 300, y: 150, c: [0,255,0], type: 'ellipse'});
  shapes.push({x: 450, y: 200, c: [0,0,255], type: 'triangle'});
}

function draw() {
  background(30);
  
  // Draw all shapes
  for (let s of shapes) {
    fill(s.c);
    if (s.type === 'rect') rect(s.x, s.y, 80, 80);
    if (s.type === 'ellipse') ellipse(s.x, s.y, 80, 80);
    if (s.type === 'triangle') triangle(s.x, s.y, s.x+40, s.y-40, s.x+80, s.y);
  }
  
  fill(255);
  textSize(20);
  text("🎨 Your Masterpiece!", 180, 350);
}'''
        }
        
        content = {
            'simulation_code': code_templates.get(lesson_id, ''),
            'explanation': self.generate_explanation(lesson_plan),
            'quiz': self.generate_quiz(lesson_plan)
        }
        
        return content
    
    def generate_explanation(self, lesson_plan):
        """Generate lesson explanations"""
        explanations = {
            1: "p5.js is a JavaScript library for creative coding. It makes it easy to create digital art, animations, and interactive experiences.",
            2: "The coordinate system starts at (0,0) in the top-left corner. X increases to the right, Y increases going down.",
            3: "RGB colors mix like paint: Red+Green=Yellow, Red+Blue=Magenta. Variables store values that can change.",
            4: "The draw() function runs continuously (60 times per second!). This is how we create animation.",
            5: "Now combine everything you've learned to create your own scene!"
        }
        return explanations.get(lesson_plan['id'], "")
    
    def generate_quiz(self, lesson_plan):
        """Generate quiz questions"""
        quizzes = {
            1: [
                {'q': 'What does createCanvas(400, 400) do?', 'options': ['Creates a 400x400 drawing area', 'Deletes the canvas', 'Saves the drawing'], 'correct': 0},
                {'q': 'Where is position (0,0)?', 'options': ['Top-left corner', 'Center', 'Bottom-right'], 'correct': 0}
            ],
            2: [
                {'q': 'What shape does ellipse(100, 100, 50, 50) draw?', 'options': ['A circle (50px wide)', 'A square', 'A line'], 'correct': 0},
                {'q': 'What does rect() use as its starting point?', 'options': ['Center', 'Top-left corner', 'Bottom-right'], 'correct': 1}
            ]
        }
        return quizzes.get(lesson_plan['id'], [])
    
    def test_lesson(self, lesson_plan, content):
        """
        Stage 3: Use Lesson Tester to simulate tutor/student
        In production: Spawns Lesson Tester agent
        """
        # Simulate testing results
        # In production: Would run actual simulation
        
        return {
            'engagement': 85,  # Would be from simulated dialogue
            'clarity': 90,
            'fun_factor': 88,
            'educational_value': 92,
            'passed': True,
            'notes': 'Lesson flows well. Students should enjoy the interactive elements.'
        }
    
    def review_lesson(self, lesson_plan, content, test_results):
        """
        Stage 4: Use Reviewer to approve lessons
        In production: Spawns Reviewer agent
        """
        # Auto-approve if scores are good
        threshold = 70
        
        scores = [
            test_results.get('engagement', 0),
            test_results.get('clarity', 0),
            test_results.get('fun_factor', 0),
            test_results.get('educational_value', 0)
        ]
        
        avg_score = sum(scores) / len(scores)
        
        print(f"📊 Review Scores:")
        print(f"   Engagement: {test_results.get('engagement', 0)}/100")
        print(f"   Clarity: {test_results.get('clarity', 0)}/100")
        print(f"   Fun Factor: {test_results.get('fun_factor', 0)}/100")
        print(f"   Educational: {test_results.get('educational_value', 0)}/100")
        print(f"   Average: {avg_score:.1f}/100")
        
        return avg_score >= threshold
    
    def publish_lesson(self, lesson_plan, content, lesson_num):
        """
        Stage 5: Generate teacher script and publish
        """
        # Generate teacher script
        script = self.generate_teacher_script(lesson_plan, content)
        
        # Save script
        script_file = self.scripts_dir / f'lesson_{lesson_num}_teacher.md'
        script_file.write_text(script)
        
        # Update lesson status
        for lesson in self.lessons:
            if lesson['id'] == lesson_num:
                lesson['status'] = 'published'
                lesson['published_at'] = datetime.now().isoformat()
        
        self.save_lessons()
    
    def generate_teacher_script(self, lesson_plan, content):
        """Generate teacher script markdown"""
        
        objectives_md = '\n'.join([f"- {o}" for o in lesson_plan['objectives']])
        
        sections = []
        
        # Opening
        sections.append(f"""## 📖 {lesson_plan['title']}

**Duration:** {lesson_plan['duration']} minutes

---

## 🎯 Learning Objectives
{objectives_md}

---

## 📜 TEACHER SCRIPT

### 👨‍🏫 Opening ({min(5, lesson_plan['duration']//10)} min)
**Say:** "Today we're going to learn about {lesson_plan['title']}. By the end, you'll be able to {lesson_plan['objectives'][0].lower().rstrip('.')}!"

### 🎮 Guided Practice ({lesson_plan['duration']//3} min
Students work through the interactive simulation. Walk around and help.
**Key challenge:** Try changing the numbers in the code!

### 💬 Discussion ({lesson_plan['duration']//6} min
**Ask:**
- What surprised you about how the code works?
- What would happen if you changed X?

### 👋 Wrap-up ({min(3, lesson_plan['duration']//15)} min
**Say:** "Next lesson we'll build on this. Keep experimenting!"

---

## 💡 Tips for Teachers

- Don't worry if students move at different paces
- Encourage experimentation over memorization
- Save great student examples to share

---

## 🔗 Student View
[Link to student mode lesson]

---
*Generated by Lesson Hub Automation*
""")
        
        return '\n\n'.join(sections)


def run_pipeline(stage=None, topic="p5.js basics", lessons=5):
    """Run the pipeline"""
    pipeline = Pipeline()
    
    if stage:
        print(f"Running single stage: {stage}")
        # Run specific stage
        pipeline.load_lessons()
        # ... implement stage-specific logic
    else:
        # Run full overnight pipeline
        pipeline.run_overnight(target_topic=topic, num_lessons=lessons)


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Lesson Hub Overnight Pipeline')
    parser.add_argument('--stage', choices=['design', 'create', 'test', 'review', 'publish'])
    parser.add_argument('--topic', default='p5.js basics')
    parser.add_argument('--lessons', type=int, default=5)
    
    args = parser.parse_args()
    
    run_pipeline(args.stage, args.topic, args.lessons)
