# p5.js Simulation Code
## Grade 1 - Living Things

### Simulation: Living vs Non-Living

**Link:** editor.p5js.org

```javascript
let items = [];
let dragging = null;

function setup() {
  createCanvas(800, 600);
  
  // Create items to sort
  items.push({name: "Dog", type: "living", emoji: "🐕", x: 100, y: 100});
  items.push({name: "Rock", type: "nonliving", emoji: "🪨", x: 200, y: 100});
  items.push({name: "Tree", type: "living", emoji: "🌳", x: 300, y: 100});
  items.push({name: "Car", type: "nonliving", emoji: "🚗", x: 400, y: 100});
  items.push({name: "Cat", type: "living", emoji: "🐱", x: 500, y: 100});
  items.push({name: "Book", type: "nonliving", emoji: "📚", x: 600, y: 100});
  items.push({name: "Bird", type: "living", emoji: "🐦", x: 100, y: 250});
  items.push({name: "Sun", type: "nonliving", emoji: "☀️", x: 200, y: 250});
  items.push({name: "Fish", type: "living", emoji: "🐟", x: 300, y: 250});
  items.push({name: "Cloud", type: "nonliving", emoji: "☁️", x: 400, y: 250});
}

function draw() {
  background(240);
  
  // Title
  textSize(32);
  fill(0);
  textAlign(CENTER);
  text("Living vs Non-Living", width/2, 40);
  
  textSize(20);
  text("Drag items to sort them!", width/2, 70);
  
  // Draw bins
  fill(100, 255, 100, 150);
  rect(50, 350, 300, 200, 20);
  textSize(24);
  fill(0);
  text("LIVING", 200, 400);
  text("🐕🌳🐱🐦🐟", 200, 440);
  
  fill(255, 100, 100, 150);
  rect(450, 350, 300, 200, 20);
  textSize(24);
  fill(0);
  text("NON-LIVING", 600, 400);
  text("🪨🚗📚☀️☁️", 600, 440);
  
  // Draw items
  textSize(40);
  for (let item of items) {
    text(item.emoji, item.x, item.y);
    textSize(14);
    text(item.name, item.x, item.y + 25);
    textSize(40);
  }
}

function mousePressed() {
  for (let item of items) {
    if (dist(mouseX, mouseY, item.x, item.y) < 30) {
      dragging = item;
      break;
    }
  }
}

function mouseDragged() {
  if (dragging) {
    dragging.x = mouseX;
    dragging.y = mouseY;
  }
}

function mouseReleased() {
  dragging = null;
}
```

---

### How to Use

1. Go to editor.p5js.org
2. Copy/paste code
3. Click Play
4. Students drag items to sort

---

*Simulation code*
