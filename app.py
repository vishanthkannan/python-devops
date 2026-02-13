from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>VK Python Store</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #141e30, #243b55);
                color: white;
                text-align: center;
            }

            header {
                padding: 20px;
                font-size: 24px;
                font-weight: bold;
                background-color: rgba(0,0,0,0.4);
            }

            .container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                padding: 40px;
                gap: 30px;
            }

            .card {
                background: white;
                color: black;
                width: 250px;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
                transition: 0.4s ease;
                cursor: pointer;
            }

            .card:hover {
                transform: translateY(-10px) scale(1.05);
                box-shadow: 0 15px 30px rgba(0,0,0,0.5);
            }

            .price {
                color: green;
                font-weight: bold;
                margin: 10px 0;
            }

            button {
                padding: 8px 15px;
                border: none;
                background: black;
                color: white;
                border-radius: 5px;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                background: #444;
            }

            footer {
                margin-top: 30px;
                padding: 20px;
                background: rgba(0,0,0,0.4);
            }
        </style>
    </head>

    <body>

        <header>Python DevOps Store</header>

        <div class="container">

            <div class="card">
                <h3>Wireless Headphones</h3>
                <p class="price">₹2,499</p>
                <button>Add to Cart</button>
            </div>

            <div class="card">
                <h3>Smart Watch</h3>
                <p class="price">₹3,999</p>
                <button>Add to Cart</button>
            </div>

            <div class="card">
                <h3>Gaming Mouse</h3>
                <p class="price">₹999</p>
                <button>Add to Cart</button>
            </div>

        </div>

        <footer>
            Deployed using Flask + Docker + Jenkins + AWS 
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
