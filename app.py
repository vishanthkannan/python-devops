from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Royal Tea Shop</title>

        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #f8f1e5;
                text-align: center;
            }

            header {
                background-color: #6b3e26;
                color: white;
                padding: 20px;
                font-size: 32px;
                font-weight: bold;
            }

            h2 {
                margin-top: 30px;
                color: #6b3e26;
            }

            .menu {
                margin: 30px auto;
                width: 300px;
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }

            .item {
                display: flex;
                justify-content: space-between;
                margin: 10px 0;
                font-size: 18px;
            }

            footer {
                margin-top: 40px;
                padding: 15px;
                background-color: #6b3e26;
                color: white;
            }
        </style>
    </head>

    <body>

        <header>
            Royal Tea Shop
        </header>

        <h2>Our Special Menu</h2>

        <div class="menu">
            <div class="item">
                <span>Masala Tea</span>
                <span>₹15</span>
            </div>
            <div class="item">
                <span>Ginger Tea</span>
                <span>₹20</span>
            </div>
            <div class="item">
                <span>Green Tea</span>
                <span>₹25</span>
            </div>
            <div class="item">
                <span>Milk Tea</span>
                <span>₹15</span>
            </div>
            <div class="item">
                <span>Lemon Tea</span>
                <span>₹20</span>
            </div>
        </div>

        <footer>
            Open Daily | 7:00 AM - 9:00 PM
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
