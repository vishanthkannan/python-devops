from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Python DevOps</title>

<style>
body {
    margin: 0;
    overflow: hidden;
    background: radial-gradient(circle at center, #080808, #000000 70%);
    font-family: Arial, sans-serif;
    color: white;
}

canvas {
    position: absolute;
    top: 0;
    left: 0;
}

.content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 10;
}

h1 {
    font-size: 64px;
    letter-spacing: 4px;
    margin: 0;
}

p {
    margin-top: 15px;
    font-size: 18px;
    color: #cccccc;
}

.cursor-glow {
    position: absolute;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    pointer-events: none;
    background: radial-gradient(circle, rgba(255,215,0,0.4) 0%, rgba(255,215,0,0.15) 40%, transparent 70%);
    transform: translate(-50%, -50%);
    z-index: 5;
}
</style>
</head>

<body>

<canvas id="space"></canvas>
<div class="cursor-glow" id="cursorGlow"></div>

<div class="content">
    <h1>Python DevOps</h1>
    <p>Deployed using Flask, Docker, Jenkins and AWS</p>
</div>

<script>
const canvas = document.getElementById("space");
const ctx = canvas.getContext("2d");
const glow = document.getElementById("cursorGlow");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let mouseX = canvas.width / 2;
let mouseY = canvas.height / 2;

document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    glow.style.left = mouseX + "px";
    glow.style.top = mouseY + "px";
});

let stars = [];

for (let i = 0; i < 500; i++) {
    stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 1.5,
        depth: Math.random() * 3
    });
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    stars.forEach(star => {
        let dx = (mouseX - canvas.width / 2) * 0.0015 * star.depth;
        let dy = (mouseY - canvas.height / 2) * 0.0015 * star.depth;

        ctx.beginPath();
        ctx.arc(star.x + dx, star.y + dy, star.radius, 0, Math.PI * 2);
        ctx.fillStyle = "#FFD700";  // Golden color
        ctx.fill();
    });

    requestAnimationFrame(draw);
}

draw();

window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
</script>

</body>
</html>
"""
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
