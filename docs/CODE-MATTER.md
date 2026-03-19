# p5.js Simulation Code
## Grade 1 - Matter (States of Water)

### Simulation: Water Cycle

```javascript
let particles = [];

function setup() {
  createCanvas(800, 500);
  
  // Create water particles
  for (let i = 0; i < 100; i++) {
    particles.push({
      x: random(width),
      y: random(400, 500),
      speed: random(0.5, 2),
      state: "liquid" // solid, liquid, gas
    });
  }
}

function draw() {
  // Sky
  background(135, 206, 235);
  
  // Sun
  fill(255, 255, 0);
  ellipse(700, 80, 80, 80);
  
  // Sun rays
  stroke(255, 255, 0);
  for (let i = 0; i < 8; i++) {
    let angle = i * PI / 4;
    line(700 + cos(angle) * 50, 80 + sin(angle) * 50,
         700 + cos(angle) * 70, 80 + sin(angle) * 70);
  }
  
  // Ground
  noStroke();
  fill(100, 200, 100);
  rect(0, 400, width, 100);
  
  // Sun label
  fill(0);
  textSize(16);
  text("Click to add HEAT!", 650, 130);
  text("Solid ← → Gas", 50, 450);
  
  // Draw particles
  for (let p of particles) {
    if (p.state === "solid") {
      fill(200, 230, 255); // Ice blue
      ellipse(p.x, p.y, 15, 15);
      // Vibration
      p.x += random(-1, 1);
      p.y += random(-1, 1);
    } else if (p.state === "liquid") {
      fill(0, 100, 255); // Water blue
      ellipse(p.x, p.y, 12, 12);
      // Flow down
      p.y += p.speed;
      if (p.y > 500) p.y = 400;
    } else { // gas
      fill(255, 255, 255, 100); // Steam white
      ellipse(p.x, p.y, 8, 8);
      // Rise up
      p.y -= p.speed;
      p.x += random(-2, 2);
      if (p.y < 50) {
        p.y = 400;
        p.state = "liquid";
      }
    }
  }
  
  // Instructions
  textSize(14);
  fill(0);
  text("Click in sky to heat up particles!", 300, 30);
}

function mousePressed() {
  // Add heat - turn to gas
  for (let p of particles) {
    if (dist(mouseX, mouseY, p.x, p.y) < 50) {
      p.state = "gas";
      p.speed = random(2, 4);
    }
  }
}

function mouseReleased() {
  // Cool down
  for (let p of particles) {
    p.state = "liquid";
    p.speed = random(0.5, 2);
  }
}
```

---

### States of Matter - Teacher Demo

This simulation shows:
- **Solid (Ice)**: Particles vibrate in place
- **Liquid (Water)**: Particles flow down
- **Gas (Steam)**: Particles rise and spread

Click to heat up!

---

*Simulation code*
