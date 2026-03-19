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
