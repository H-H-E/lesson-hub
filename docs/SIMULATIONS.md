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


## Grade 4: Water Cycle Simulation

```javascript
let drops = [];
let clouds = [];

function setup() {
  createCanvas(800, 500);
  // Create clouds
  clouds.push({x: 100, y: 50, size: 80});
  clouds.push({x: 400, y: 30, size: 100});
  clouds.push({x: 650, y: 60, size: 70});
}

function draw() {
  background(200, 230, 255);
  
  // Draw sun
  fill(255, 255, 0);
  ellipse(700, 50, 60, 60);
  
  // Draw clouds
  fill(255);
  for(let c of clouds) {
    ellipse(c.x, c.y, c.size, c.size * 0.6);
    if(c.size > 70) {
      // Evaporation
      if(random() < 0.02) {
        drops.push({x: c.x + random(-30,30), y: c.y + 30, speed: random(1,3)});
      }
    }
  }
  
  // Draw and move rain drops
  fill(0, 0, 200);
  for(let i = drops.length - 1; i >= 0; i--) {
    let d = drops[i];
    d.y += d.speed;
    ellipse(d.x, d.y, 8, 10);
    
    // Ground
    if(d.y > 450) {
      // Collection
      drops.splice(i, 1);
    }
  }
  
  // Draw ground
  fill(100, 200, 100);
  rect(0, 450, 800, 50);
  
  // Labels
  fill(0);
  textSize(14);
  text("Evaporation ↑", 80, 120);
  text("Condensation", 350, 80);
  text("Precipitation ↓", 550, 200);
  text("Collection", 650, 480);
}
```

---

## Grade 5: Food Chain Simulation

```javascript
let plants = [];
let herbivores = [];
let carnivores = [];

function setup() {
  createCanvas(800, 500);
  // Create initial populations
  for(let i = 0; i < 20; i++) {
    plants.push({x: random(width), y: random(300, 490), energy: 100});
  }
}

function draw() {
  background(100, 150, 100);
  
  // Draw and grow plants
  fill(0, 150, 0);
  for(let p of plants) {
    ellipse(p.x, p.y, 15, 15);
    if(random() < 0.01) p.energy += 10;
  }
  
  // Move herbivores
  fill(150, 100, 50);
  for(let h of herbivores) {
    ellipse(h.x, h.y, 20, 15);
    h.x += h.vx;
    h.y += h.vy;
    // Wrap around
    if(h.x < 0) h.x = width;
    if(h.x > width) h.x = 0;
    if(h.y < 0) h.y = height;
    if(h.y > height) h.y = 0;
  }
  
  // Labels
  fill(255);
  textSize(16);
  text("Plants (Producers)", 20, 30);
  text("Herbivores", 20, 50);
  text("Carnivores", 20, 70);
}
```
