# The Nature of Code - Curriculum Methodology

## Overview

This curriculum is based on Daniel Shiffman's "The Nature of Code" - a book about simulating natural phenomena with code using p5.js.

## Core Philosophy

> "I want to take a look at phenomena that naturally occur in the physical world and figure out how to write code to simulate them."
> — Daniel Shiffman

### Three Parts, Three Transformations

```
┌─────────────────────────────────────────────────────────────┐
│                    THE NATURE OF CODE                        │
│                    Book Structure                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PART 1: INANIMATE OBJECTS                                  │
│  ──────────────────────────────                              │
│  Objects that move according to physics                      │
│  Randomness → Vectors → Forces → Oscillation → Particles     │
│                                                             │
│                    ↓ (add perception)                        │
│                                                             │
│  PART 2: IT'S ALIVE!                                        │
│  ──────────────────────                                      │
│  Objects that make choices                                   │
│  Autonomous Agents → Physics Libs → CA → Fractals            │
│                                                             │
│                    ↓ (add evolution)                         │
│                                                             │
│  PART 3: INTELLIGENCE                                       │
│  ─────────────────────                                       │
│  Objects that learn and adapt                                │
│  Genetic Algorithms → Neural Networks → Neuroevolution       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Pedagogical Approach

### 1. Observation Before Formalization

Every topic begins with:
- **Show** the phenomenon in nature
- **Ask** "How could we model this?"
- **Extract** the algorithmic rules
- **Implement** in code
- **Explore** variations

### 2. The Math is the Message

Don't teach math for math's sake - only introduce mathematical concepts when needed to make the simulation work. Let the code reveal the beauty.

### 3. Object-Oriented from the Start

The book (and this curriculum) assumes OOP knowledge. Each simulation is built with:
- Classes for entities
- Methods for behaviors
- Inheritance where appropriate

### 4. The Ecosystem Project

A semester-long project that integrates all concepts:
- Week 1-4: Core physics (position, velocity, acceleration)
- Week 5-8: Behaviors (steering, flocking, seeking)
- Week 9-12: Intelligence (evolution, learning)
- Week 13-14: Polish and presentation

## Lesson Structure

### Each Week Includes:

1. **Conceptual Foundation** (30 min)
   - Hook: Stunning natural example
   - Question: How to model computationally?
   - Context: History and key insights
   - Math: Just enough to implement

2. **Live Coding** (30 min)
   - Minimal working example
   - Step-by-step construction
   - Real-time Q&A

3. **Exploration** (45 min)
   - Student modifies the code
   - Tweak parameters
   - Observe changes

4. **Exercises** (ongoing)
   - Basic: Modify one thing
   - Intermediate: Add a feature
   - Challenge: Open-ended

5. **Assessment** (end of week)
   - Concept check
   - Code reading
   - Code writing

## Weekly Breakdown

| Week | Topics | Project Milestone |
|------|--------|-------------------|
| 1 | Randomness, Vectors | Create a walker |
| 2 | Forces | Add gravity/attraction |
| 3 | Oscillation | Add pendulum/spring |
| 4 | Particle Systems | Emit particles |
| 5 | Autonomous Agents | Steering behaviors |
| 6 | Physics Libraries | Integrate Matter.js |
| 7 | Cellular Automata | Conway's Game of Life |
| 8 | Fractals | Recursive trees |
| 9 | Genetic Algorithms | Evolve a creature |
| 10 | Neural Networks | Build a brain |
| 11 | Neuroevolution | Evolve behavior |
| 12 | Buffer week | Catch up |
| 13-14 | Final projects | Presentations |

## Assessment Philosophy

### What We Assess

1. **Conceptual Understanding**
   - Can explain WHY (not just WHAT)
   - Connects math to visual output
   - Predicts behavior from code

2. **Code Comprehension**
   - Read and understand sketches
   - Identify bugs
   - Trace execution

3. **Creative Application**
   - Apply concepts to new cases
   - Extend existing simulations
   - Personalize the project

4. **Technical Skill**
   - Clean, readable code
   - Proper OOP patterns
   - Working simulations

### Assessment Types

- **Concept Checks**: Multiple choice testing intuition
- **Code Reading**: Given code, predict output / find bugs
- **Code Writing**: Implement specified behavior
- **Portfolio**: Ecosystem Project with reflections

## Tools & Resources

### Primary Tools
- p5.js Web Editor (editor.p5js.org)
- Chrome DevTools
- GitHub for code sharing

### Reference
- Book: natureofcode.com
- Videos: The Coding Train (YouTube)
- Community: Coding Train Discord

### Code Style

```javascript
// Object-oriented, well-commented
class Mover {
  constructor(x, y) {
    this.position = createVector(x, y);
    this.velocity = createVector(0, 0);
    this.acceleration = createVector(0, 0);
    this.mass = 1;
  }
  
  applyForce(force) {
    this.acceleration.add(force);
  }
  
  update() {
    this.velocity.add(this.acceleration);
    this.position.add(this.velocity);
    this.acceleration.mult(0);
  }
  
  display() {
    fill(255);
    ellipse(this.position.x, this.position.y, 24);
  }
}
```

## Grading Rubric

| Category | Weight | Criteria |
|----------|--------|----------|
| Weekly Exercises | 30% | Completion + effort |
| Code Reading | 15% | Accuracy |
| Code Writing | 20% | Functionality + style |
| Ecosystem Project | 25% | Ambition + execution |
| Reflection | 10% | Depth of understanding |

## Tips for Instructors

1. **Live code** - Don't just show slides, type in front of them
2. **Embrace chaos** - Simulations are unpredictable, that's a feature
3. **Encourage play** - The best learning comes from exploration
4. **Show the art** - Nature of Code can be beautiful
5. **Connect to nature** - The math isn't abstract, it describes reality

## Ecosystem Project Examples

Past student projects have included:
- Ecosystems with predator/prey dynamics
- Evolutionary creatures that learn to walk
- Flocking simulations with emergent behavior
- Cellular automata art generators
- Neural network-controlled agents
- Fractal landscapes

The key: Student chooses their own phenomenon to model.
