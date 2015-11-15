from flask import Flask, render_template
import sqlite3

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo')
def demo():
    connection = sqlite3.connect('comma_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT name, happiness_amt, surprise_amt, contempt_amt, disgust_amt, fear_amt, neutral_amt, anger_amt, sadness_amt FROM movies')

    movies = cursor.fetchall()

    print(movies)

    cursor.close()
    connection.close()

    return render_template('Demo.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/team')
def team():
    return render_template('Team.html')

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run(host="0.0.0.0", port=8000)