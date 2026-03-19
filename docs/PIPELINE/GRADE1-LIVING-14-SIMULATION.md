# Interactive p5.js Simulation: Living Things

## Overview
An interactive simulation for Grade 1 Science students to learn about living vs. non-living things through hands-on exploration.

**Platform:** [editor.p5js.org](https://editor.p5js.org/)  
**Copy/Paste:** The code below into a new p5.js sketch

---

## How to Use This Simulation

### Teacher Instructions
1. Open [editor.p5js.org](https://editor.p5js.org/)
2. Copy the entire code block below
3. Paste into the editor and press Play
4. Students can click/tap on objects to discover which are living

### Student Instructions
- Look at the scene with living and non-living things
- Click on any object to check if it's living or non-living
- Watch the character explain what makes something alive!
- Try to find all the living things!

---

## p5.js Simulation Code

```javascript
// Grade 1 Science: Living Things - Interactive Simulation
// Students discover what makes something ALIVE!

let objects = [];
let selectedObject = null;
let feedbackText = "";
let score = 0;
let totalFound = 0;
let gameStarted = false;
let showIntro = true;
let introTimer = 0;

// Colors
const COLORS = {
  sky: "#87CEEB",
  grass: "#90EE90",
  dirt: "#8B4513",
  sun: "#FFD700",
  living: "#4CAF50",
  nonLiving: "#FF6B6B",
  text: "#333333",
  white: "#FFFFFF"
};

function setup() {
  createCanvas(800, 500);
  textAlign(CENTER, CENTER);
  
  // Create scene objects
  initObjects();
}

function initObjects() {
  objects = [];
  
  // LIVING THINGS (Animals & Plants)
  objects.push(new SceneObject(120, 340, "dog", "🐕", true, "I move and need food! Woof!"));
  objects.push(new SceneObject(250, 350, "flower", "🌻", true, "I grow toward the sun!"));
  objects.push(new SceneObject(400, 330, "bird", "🐦", true, "I breathe and fly!"));
  objects.push(new SceneObject(550, 360, "tree", "🌳", true, "I am a living plant!"));
  objects.push(new SceneObject(680, 340, "fish", "🐟", true, "I live in water and swim!"));
  objects.push(new SceneObject(180, 400, "grass", "🌱", true, "I am a living plant too!"));
  objects.push(new SceneObject(620, 400, "butterfly", "🦋", true, "I was a caterpillar before!"));
  
  // NON-LIVING THINGS
  objects.push(new SceneObject(320, 420, "rock", "🪨", false, "I don't need food or air."));
  objects.push(new SceneObject(480, 430, "ball", "⚽", false, "I never grow or change."));
  objects.push(new SceneObject(720, 420, "cloud", "☁️", false, "I'm just water vapor!"));
  objects.push(new SceneObject(80, 420, "book", "📚", false, "I was made by living things, but I'm not alive."));
  objects.push(new SceneObject(560, 80, "sun", "☀️", false, "I give light and heat, but I'm not alive!"));
}

function draw() {
  // Draw background
  drawBackground();
  
  if (showIntro) {
    drawIntroScreen();
    return;
  }
  
  // Draw all objects
  for (let obj of objects) {
    obj.display();
  }
  
  // Draw UI
  drawUI();
  
  // Draw feedback popup
  if (selectedObject) {
    drawFeedback();
  }
}

function drawBackground() {
  // Sky
  background(COLORS.sky);
  
  // Sun
  noStroke();
  fill(COLORS.sun);
  circle(700, 60, 60);
  
  // Clouds
  fill(255, 230, 230, 200);
  ellipse(150, 80, 80, 40);
  ellipse(190, 70, 70, 45);
  ellipse(230, 85, 60, 35);
  
  ellipse(450, 100, 90, 45);
  ellipse(500, 90, 70, 50);
  
  // Hills
  fill("#7CB342");
  ellipse(200, 420, 350, 150);
  ellipse(600, 400, 400, 180);
  
  // Grass
  fill(COLORS.grass);
  rect(0, 380, 800, 120);
  
  // Ground line
  stroke("#558B2F");
  strokeWeight(3);
  line(0, 380, 800, 380);
}

function drawIntroScreen() {
  fill(0, 0, 0, 150);
  rect(0, 0, width, height);
  
  fill(255);
  stroke(0);
  strokeWeight(3);
  rect(100, 50, 600, 400, 20);
  
  fill(0);
  noStroke();
  textSize(36);
  text("🔍 Living Things Hunt!", 400, 100);
  
  textSize(18);
  text("Can you find all the living things?", 400, 150);
  text("Click on objects to check if they are alive!", 400, 180);
  
  textSize(16);
  fill(0);
  text("Living things can:", 400, 230);
  text("🏃 Move on their own", 400, 260);
  text("🍎 Need food and water", 400, 285);
  text("📏 Grow and change", 400, 310);
  text("💨 Breathe air", 400, 335);
  
  // Blinking start text
  if (frameCount % 60 < 30) {
    fill("#4CAF50");
    textSize(24);
    text("👉 Click anywhere to START!", 400, 390);
  }
}

function drawUI() {
  // Score panel
  fill(255, 255, 255, 220);
  stroke(0);
  strokeWeight(2);
  rect(10, 10, 180, 60, 10);
  
  noStroke();
  fill(0);
  textSize(16);
  textAlign(LEFT, TOP);
  text("🌿 Living Things Found:", 20, 20);
  
  textSize(24);
  fill(COLORS.living);
  let livingCount = objects.filter(o => o.isLiving && o.found).length;
  text(livingCount + " / 7", 25, 42);
  
  textAlign(CENTER, CENTER);
}

function drawFeedback() {
  // Popup box
  fill(255, 255, 255, 250);
  stroke(selectedObject.isLiving ? COLORS.living : COLORS.nonLiving);
  strokeWeight(4);
  rect(150, 150, 500, 180, 20);
  
  // Emoji
  noStroke();
  textSize(60);
  text(selectedObject.emoji, 400, 200);
  
  // Label
  textSize(28);
  fill(selectedObject.isLiving ? COLORS.living : COLORS.nonLiving);
  let label = selectedObject.isLiving ? "✅ LIVING THING!" : "❌ NOT ALIVE";
  text(label, 400, 260);
  
  // Fact
  textSize(16);
  fill(0);
  text(selectedObject.fact, 400, 300);
  
  // Continue prompt
  if (frameCount % 40 < 20) {
    fill("#666");
    textSize(14);
    text("Click anywhere to continue...", 400, 360);
  }
}

function mousePressed() {
  if (showIntro) {
    showIntro = false;
    gameStarted = true;
    return;
  }
  
  if (selectedObject) {
    selectedObject = null;
    return;
  }
  
  // Check if clicked on an object
  for (let obj of objects) {
    if (obj.isClicked(mouseX, mouseY)) {
      selectedObject = obj;
      if (obj.isLiving && !obj.found) {
        obj.found = true;
        totalFound++;
      }
      break;
    }
  }
}

function keyPressed() {
  // Press R to restart
  if (key === 'r' || key === 'R') {
    initObjects();
    selectedObject = null;
    showIntro = true;
  }
}

// Scene Object Class
class SceneObject {
  constructor(x, y, name, emoji, isLiving, fact) {
    this.x = x;
    this.y = y;
    this.name = name;
    this.emoji = emoji;
    this.isLiving = isLiving;
    this.fact = fact;
    this.size = 50;
    this.found = false;
    this.floatOffset = random(1000);
  }
  
  display() {
    // Floating animation
    let floatY = sin((frameCount + this.floatOffset) * 0.05) * 3;
    
    // Hover effect
    let isHovered = this.isClicked(mouseX, mouseY);
    let displaySize = isHovered ? this.size * 1.2 : this.size;
    
    // Draw shadow
    fill(0, 0, 0, 30);
    noStroke();
    ellipse(this.x, this.y + this.size/2 + 5, displaySize * 0.8, 10);
    
    // Draw emoji
    textSize(displaySize);
    text(this.emoji, this.x, this.y + floatY);
    
    // Found indicator
    if (this.found) {
      fill(COLORS.living);
      ellipse(this.x + 20, this.y - 20, 20, 20);
      fill(255);
      textSize(12);
      text("✓", this.x + 20, this.y - 20);
    }
  }
  
  isClicked(mx, my) {
    let d = dist(mx, my, this.x, this.y);
    return d < this.size / 2 + 10;
  }
}
```

---

## Learning Outcomes Supported

| Objective | Simulation Feature |
|-----------|-------------------|
| Identify 5+ living things | Students click objects to identify 7 living things |
| Distinguish living vs non-living | Immediate feedback explains why something is/isn't alive |
| Basic needs (food, air, water) | Facts explain needs: "I need food and water!" |
| Growth and change | Facts mention: "I was a caterpillar before!" |

---

## Differentiation Tips

### For Struggling Students
- Focus on just 3-4 objects initially
- Use the visual feedback (green = living, red = non-living)

### For Advanced Students
- Ask: "What would happen if the plant had no water?"
- Challenge: Can you find something that was NEVER alive vs. something made by living things?

---

## Technical Notes

- **No external dependencies** - runs entirely in p5.js
- **Touch-friendly** - works on tablets
- **Responsive** - fixed 800x500 canvas, scales in editor
- **Keyboard shortcut** - press 'R' to restart
