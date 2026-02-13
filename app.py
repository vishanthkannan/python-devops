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
                background: radial-gradient(circle at center, #111, #000);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                font-family: Arial, sans-serif;
                overflow: hidden;
            }

            h1 {
                font-size: 60px;
                margin: 0;
                letter-spacing: 3px;
            }

            p {
                margin-top: 10px;
                font-size: 18px;
                color: #ccc;
            }

            .spark {
                position: absolute;
                width: 15px;
                height: 15px;
                background: radial-gradient(circle, #00f2ff, transparent);
                border-radius: 50%;
                pointer-events: none;
                animation: fadeOut 0.8s linear forwards;
            }

            @keyframes fadeOut {
                0% {
                    transform: scale(1);
                    opacity: 1;
                }
                100% {
                    transform: scale(3);
                    opacity: 0;
                }
            }
        </style>
    </head>

    <body>

        <h1>Python DevOps </h1>
        <p>Deployed using Flask + Docker + Jenkins + AWS</p>

        <script>
            document.addEventListener("mousemove", function(e) {
                const spark = document.createElement("div");
                spark.className = "spark";
                spark.style.left = e.pageX + "px";
                spark.style.top = e.pageY + "px";
                document.body.appendChild(spark);

                setTimeout(() => {
                    spark.remove();
                }, 800);
            });
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
