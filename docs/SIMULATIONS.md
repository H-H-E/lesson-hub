# Interactive Simulation Examples

## Grade 1: Living vs Non-Living

### Simulation Concept
- Screen shows mix of living/non-living items
- Students drag items to correct category
- Immediate feedback
- Score tracking

### p5.js Code Structure
```javascript
let items = [
  {name: "dog", type: "living", img: "🐕"},
  {name: "rock", type: "nonliving", img: "🪨"},
  // ... more items
];

function setup() {
  createCanvas(800, 600);
}

function draw() {
  background(240);
  // Display items to sort
  // Drag and drop logic
}
```

---

## Grade 2: Life Cycles

### Simulation Concept
- Show butterfly, frog, chicken life cycles
- Click to advance stages
- Compare cycles

---

## Grade 3: Forces and Motion

### Simulation Concept
- Add push/pull forces
- Watch objects accelerate
- Record distance traveled

### p5.js Code Structure
```javascript
let ball = {x: 100, y: 300, vx: 0, ax: 0};

function draw() {
  ball.vx += ball.ax;
  ball.x += ball.vx;
  
  // Draw ball
  fill(255, 100, 100);
  ellipse(ball.x, ball.y, 50);
}

// Add force when mouse pressed
function mousePressed() {
  ball.ax = 0.5; // Push!
}
```

---

## Grade 4: Energy Transfer

### Simulation Concept
- Ball rolls down ramp
- Shows potential → kinetic energy
- Energy bar display

---

*Simulation examples for each grade*


## Grade 2: Matter Simulation

```javascript
// States of matter simulation
let particles = [];

function setup() {{
  createCanvas(600, 400);
  // Create particles
  for(let i = 0; i < 50; i++) {{
    particles.push({{
      x: random(width),
      y: random(height),
      speed: random(0.5, 2),
      state: random(['solid', 'liquid', 'gas'])
    }});
  }}
}}

function draw() {{
  background(30);
  
  for(let p of particles) {{
    // Different behavior based on state
    if(p.state === 'solid') {{
      // Vibrate in place
      fill(200);
      ellipse(p.x + random(-1,1), p.y + random(-1,1), 10);
    }} else if(p.state === 'liquid') {{
      // Flow together
      fill(100, 200, 255);
      p.y += p.speed;
      if(p.y > height) p.y = 0;
      ellipse(p.x, p.y, 12);
    }} else {{
      // Gas - spread out
      fill(255, 255, 200, 100);
      p.x += random(-2, 2);
      p.y += random(-2, 2);
      ellipse(p.x, p.y, 8);
    }}
  }}
}}

function mousePressed() {{
  // Heat up - make particles move faster
  for(let p of particles) {{
    p.speed *= 1.5;
  }}
}}
```

---

## Grade 3: Forces Simulation

```javascript
// Simple force simulation
let ball = {{x: 100, y: 200, vx: 0, vy: 0}};

function draw() {{
  background(50);
  
  // Apply gravity
  ball.vy += 0.2;
  
  // Apply mouse force
  if(mouseIsPressed) {{
    let dx = mouseX - ball.x;
    let dy = mouseY - ball.y;
    ball.vx += dx * 0.01;
    ball.vy += dy * 0.01;
  }}
  
  // Update position
  ball.x += ball.vx;
  ball.y += ball.vy;
  
  // Bounce off walls
  if(ball.x < 0 || ball.x > width) ball.vx *= -0.8;
  if(ball.y > height) ball.vy *= -0.8;
  
  // Draw ball
  fill(255, 100, 100);
  ellipse(ball.x, ball.y, 40);
}}
```

---

*Additional simulation code*
