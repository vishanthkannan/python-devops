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
    background: radial-gradient(circle at center, #050510, #000000);
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
    margin: 0;
    letter-spacing: 3px;
}

p {
    margin-top: 15px;
    font-size: 18px;
    color: #bbbbbb;
}
</style>
</head>

<body>

<canvas id="space"></canvas>

<div class="content">
    <h1>Python DevOps</h1>
    <p>Deployed using Flask, Docker, Jenkins and AWS</p>
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

for (let i = 0; i < 400; i++) {
    stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 1.5,
        depth: Math.random() * 3
    });
}

planets.push({
    x: canvas.width * 0.25,
    y: canvas.height * 0.35,
    radius: 50,
    color: "#4fc3f7"
});

planets.push({
    x: canvas.width * 0.75,
    y: canvas.height * 0.65,
    radius: 70,
    color: "#ff4081"
});

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    stars.forEach(star => {
        let dx = (mouseX - canvas.width / 2) * 0.001 * star.depth;
        let dy = (mouseY - canvas.height / 2) * 0.001 * star.depth;

        ctx.beginPath();
        ctx.arc(star.x + dx, star.y + dy, star.radius, 0, Math.PI * 2);
        ctx.fillStyle = "white";
        ctx.fill();
    });

    planets.forEach(planet => {
        ctx.beginPath();
        ctx.arc(
            planet.x + Math.sin(Date.now() * 0.0008) * 20,
            planet.y + Math.cos(Date.now() * 0.0008) * 20,
            planet.radius,
            0,
            Math.PI * 2
        );
        ctx.fillStyle = planet.color;
        ctx.shadowBlur = 30;
        ctx.shadowColor = planet.color;
        ctx.fill();
        ctx.shadowBlur = 0;
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
