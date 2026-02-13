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
                height: 100vh;
                overflow: hidden;
                background: #000;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                text-align: center;
            }

            h1 {
                font-size: 60px;
                letter-spacing: 4px;
                z-index: 10;
            }

            p {
                font-size: 18px;
                color: #ccc;
                z-index: 10;
            }

            canvas {
                position: absolute;
                top: 0;
                left: 0;
                z-index: 1;
            }
        </style>
    </head>

    <body>

        <canvas id="galaxy"></canvas>

        <h1>Python DevOps </h1>
        <p>Deployed using Flask + Docker + Jenkins + AWS</p>

        <script>
            const canvas = document.getElementById("galaxy");
            const ctx = canvas.getContext("2d");

            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            let stars = [];

            for (let i = 0; i < 200; i++) {
                stars.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    radius: Math.random() * 2,
                    speed: Math.random() * 0.5
                });
            }

            function drawStars() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "white";
                stars.forEach(star => {
                    ctx.beginPath();
                    ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
                    ctx.fill();

                    star.y += star.speed;

                    if (star.y > canvas.height) {
                        star.y = 0;
                        star.x = Math.random() * canvas.width;
                    }
                });

                requestAnimationFrame(drawStars);
            }

            drawStars();

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
