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
    background: radial-gradient(circle at center, #000010, #000);
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
    font-size: 60px;
    letter-spacing: 4px;
}

p {
    color: #ccc;
    font-size: 18px;
}
</style>
</head>

<body>

<canvas id="space"></canvas>

<div class="content">
    <h1>Python DevOps</h1>
    <p>Deployed using Flask + Docker + Jenkins + AWS</p>
</div>

<script>
const canvas = document.getElementById("space");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let mouseX = canvas.width / 2;
let mouseY = canvas.height / 2;

document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

let stars = [];
let planets = [];

for (let i = 0; i < 250; i++) {
    stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 2,
        depth: Math.random() * 2 + 0.5
    });
}

planets.push({
    x: canvas.width * 0.2,
    y: canvas.height * 0.3,
    radius: 40,
    color: "#4fc3f7"
});

planets.push({
    x: canvas.width * 0.8,
    y: canvas.height * 0.7,
    radius: 60,
    color: "#ff4081"
});

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Stars with parallax
    stars.forEach(star => {
        let dx = (mouseX - canvas.width/2) * 0.0005 * star.depth;
        let dy = (mouseY - canvas.height/2) * 0.0005 * star.depth;

        ctx.beginPath();
        ctx.arc(star.x + dx, star.y + dy, star.radius, 0, Math.PI * 2);
        ctx.fillStyle = "white";
        ctx.fill();
    });

    // Floating planets
    planets.forEach(planet => {
        ctx.beginPath();
        ctx.arc(
            planet.x + Math.sin(Date.now()*0.001)*20,
            planet.y + Math.cos(Date.now()*0.001)*20,
            planet.radius,
            0,
            Math.PI * 2
        );
        ctx.fillStyle = planet.color;
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
