from flask import Flask
import requests

app = Flask(__name__)

def get_cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact")
        return response.json().get('fact', "Факт загубився по дорозі...")
    except:
        return "Не вдалося отримати факт."

@app.route('/')
def home():
    fact = get_cat_fact()
    return f"""
    <html>
        <head><title>Мій перший сайт на Flask</title></head>
        <body style="text-align: center; font-family: sans-serif; padding-top: 50px;">
            <h1>Вітаю! Це вебсторінка на Flask 🚀</h1>
            <p style="font-size: 1.2em; color: #555;">Ось цікавий факт, отриманий через API:</p>
            <div style="background: #f0f0f0; padding: 20px; border-radius: 10px; display: inline-block;">
                <strong>{fact}</strong>
            </div>
            <br><br>
            <a href="/">Оновити сторінку</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Запускаємо сервер на локальному хості
    app.run(debug=True)

     