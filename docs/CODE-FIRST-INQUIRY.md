# Code-First Inquiry: A Novel Computational Science Curriculum

## The Core Insight

> Traditional approach: Learn science → Apply to code  
> **This approach**: Experiment with code → Discover science

Students don't learn science to code — they use code to see science in a way impossible without computation.

---

## Pedagogical Foundation

### The Mystery-First Method

Every lesson begins with a **puzzle**:
- "Why does this pattern emerge?"
- "What happens if I change this?"
- "Can you make it do X?"

The student explores, discovers, then learns the formal science behind what they just witnessed.

### The Three Lenses

Every phenomenon is explored through:

1. **The Simulation Lens** — What does it LOOK like?
2. **The Math Lens** — What PATTERNS emerge?
3. **The Code Lens** — How do we EXPRESS this?

### Learning Through Making

- 70% making / experimenting
- 20% reflecting / connecting
- 10% formal instruction

---

## The "Code Lab" Format

Each lesson follows this structure:

```
┌─────────────────────────────────────────────────────┐
│                   CODE LAB LESSON                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. THE HOOK (2 min)                               │
│     → A visual puzzle / demo / mystery              │
│                                                     │
│  2. THE EXPERIMENT (15 min)                        │
│     → Open-ended exploration with scaffolded       │
│       parameters                                    │
│                                                     │
│  3. THE DISCOVERY (5 min)                         │
│     → Students share what they found                │
│                                                     │
│  4. THE FORMALIZATION (10 min)                     │
│     → Here's the science behind your discovery     │
│                                                     │
│  5. THE EXTENSION (15 min)                         │
│     → Apply to new problem                         │
│                                                     │
│  6. THE QUICK CHECK (3 min)                       │
│     → 3-question comprehension check               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Sample Modules (Novel Concepts)

### Module 1: "The Gravity Illusion"

**Hook**: Two balls fall — one drops straight, one is given a tiny sideways push. Which hits first?

*Most students guess wrong. They're about to discover why.*

**Experiment**: Students adjust initial velocity in a falling simulation. They try to predict outcomes.

**Discovery**: Galileo was right — but only in a vacuum. Air resistance changes everything.

**Formalization**: Introduction to:
- Free fall equations
- Air resistance modeling
- Terminal velocity

**Extension**: Can you make a ball float?

---

### Module 2: "The Swarm Intelligence"

**Hook**: A flock of boids moves organically. No leader. No plan. Yet they coordinate.

*How does order emerge from chaos?*

**Experiment**: Students adjust alignment, cohesion, separation weights. They create patterns.

**Discovery**: Simple rules → complex behavior. This is emergence.

**Formalization**:
- Emergence
- Agent-based modeling
- Flocking algorithms

**Extension**: Add a predator. Watch the escape behaviors emerge.

---

### Module 3: "The Heat Equation"

**Hook**: Put your hand in room temperature water. It feels cold. Put it in hot water, then room temp — now it feels warm.

*Same temperature. Different sensation. Why?*

**Experiment**: Students build a temperature diffusion simulation. They control initial conditions.

**Discovery**: Heat flows from hot to cold, but never reverses spontaneously.

**Formalization**:
- The Heat Equation
- Partial differential equations (accessible version)
- Entropy introduction

**Extension**: Add a "cold source" — can you create a self-sustaining pattern?

---

### Module 4: "The Predator's Math"

**Hook**: A simple chase. Predator follows prey. Prey flees predator. The mathematics are beautiful.

*Can you write the rules for optimal hunting?*

**Experiment**: Students code steering behaviors. They optimize for speed, turns, prediction.

**Discovery**: Pure pursuit is dumb. Intercept trajectories are elegant.

**Formalization**:
- Pursuit curves
- Differential games
- Evolutionary arms races

**Extension**: Add terrain. Watch strategies evolve.

---

### Module 5: "The Neural Dream"

**Hook**: A network learns to classify images. We watch it learn. It makes mistakes. We see its dreams.

*What does a neural network actually "see"?*

**Experiment**: Students train a simple network. They visualize weights, watch learning curves.

**Discovery**: Deep learning isn't magic — it's calculus + chain rule + lots of data.

**Formalization**:
- Perceptrons
- Backpropagation (intuitive)
- Feature extraction

**Extension**: What happens if you remove half the neurons?

---

### Module 6: "The Evolutionary Canvas"

**Hook**: Start with random shapes. Select for "fitness." After 100 generations, you have... art.

*Can evolution create beauty?*

**Experiment**: Students run genetic algorithms. They design fitness functions. They select for aesthetics.

**Discovery**: Evolution is blind, but guided selection is powerful.

**Formalization**:
- Genetic algorithms
- Fitness landscapes
- Crossover and mutation

**Extension**: Co-evolution — two populations competing.

---

## Interactive Components

### Built-In Simulations

Each lesson includes a pre-built p5.js simulation students can:
- Fork and modify
- Tweak parameters in real-time
- Save their variations

### Embedded Quizzes

```
┌──────────────────────────────────────────┐
│  ⚡ QUICK CHECK                          │
├──────────────────────────────────────────┤
│                                          │
│  Q1: If you double the mass...          │
│      ○ acceleration doubles              │
│      ○ acceleration halves               │
│      ○ stays the same                    │
│      ○ depends on gravity                │
│                                          │
│  Q2: What's the pattern?                 │
│      [Interactive: predict the path]     │
│                                          │
│  Q3: Explain in 1 sentence:             │
│      [Text input + AI feedback]          │
│                                          │
└──────────────────────────────────────────┘
```

### The Lab Notebook

Students maintain a digital notebook:
- Screenshots of discoveries
- Code snippets
- Reflection prompts
- Connection to other modules

---

## Novel Integration: The Story Arc

Modules connect through a **narrative**:

> *"You've been recruited by The Simulation Institute to investigate mysterious phenomena. Each lab reveals a new piece of the puzzle..."*

This creates:
- Intrinsic motivation
- Coherent learning journey
- Memorable experience

---

## Assessment Philosophy

### What We Measure

1. **Exploration Quality** - Did they try varied experiments?
2. **Discovery Articulation** - Can they explain what they found?
3. **Connection Making** - Do they link concepts?
4. **Code Fluency** - Can they express ideas in code?
5. **Creative Extension** - Do they go beyond the lab?

### Assessment Types

| Type | When | Weight |
|------|------|--------|
| Lab Notebook Entries | After each module | 20% |
| Code Challenges | Weekly | 25% |
| The Big Build | End of course | 30% |
| Peer Teaching | 2x per semester | 15% |
| Reflection Essays | Monthly | 10% |

---

## Technology Stack

### For Students (No Install)

- **p5.js Web Editor** - All code runs in browser
- **Google Colab** - For any Python/ML modules
- **Observable** - For reactive notebooks

### For Instructors

- **Dashboard** - Track student progress
- **Lab Templates** - Quick lesson creation
- **Analytics** - Identify struggling students early

---

## Why This Is Different

| Traditional | This Approach |
|-------------|---------------|
| Learn theory → Apply | Explore → Discover → Formalize |
| Science first, code second | Code IS the lens for science |
| Verification exercises | Open-ended exploration |
| Individual work | Social discovery |
| memorize → implement | discover → understand → apply |

---

## The Promise

Students don't just learn to code AND don't just learn science.

They learn that **code is a way of thinking** — a powerful lens to see, explore, and understand the natural world.

They become **computational thinkers** who can approach ANY problem: model it, simulate it, understand it.

---

## Course Titles (Pick One)

- **"Code Lab: The Computational Nature of Things"**
- **"Simulation t(r)ial: A Code-First Science Journey"**
- **"The Algorithmic Laboratory"**
- **"Discoveries in Code"**

---

*This is just the beginning. The curriculum can expand to any scientific domain: physics, biology, chemistry, climate science, neuroscience, economics... The method is universal.*
