from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, static_folder="static", static_url_path="")

movie_names = {
    "casinoroyale": "Casino Royale",
    "faultinourstars": "The Fault in Our Stars",
    "greatgatsby": "Great Gatsby",
    "ingloriousbasterds": "Inglorious Basterds",
    "romeoandjuliet": "Romeo and Juliet",
    "schindlerslist": "Schindler's List",
    "shutterisland": "Shutter Island",
}

movie_videos = {
    "casinoroyale": "36mnx8dBbGE",
    "faultinourstars": "9ItBvH5J6ss",
    "greatgatsby": "rARN6agiW7o",
    "ingloriousbasterds": "6AtLlVNsuAc",
    "romeoandjuliet": "sMel13nY0PE",
    "schindlerslist": "dwfIf1WMhgc",
    "shutterisland": "5iaYLCiq5RM",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo')
def demo():
    connection = sqlite3.connect('comma_database.db')
    cursor = connection.cursor()

    emotion = request.args.get('emotion', 'neutral')

    cursor.execute('SELECT name, %s_amt FROM movies ORDER BY %s_amt DESC' % (emotion, emotion, ))

    movie_data = cursor.fetchall()
    movies = []

    for movie in movie_data:
        movie = list(movie)
        movie.append(movie_names[movie[0]])

        movies.append(movie)

    cursor.close()
    connection.close()

    return render_template('Demo.html', movies=movies, emotion=emotion)

@app.route('/details/<movie>')
def details(movie):
    connection = sqlite3.connect('comma_database.db')
    cursor = connection.cursor()

    emotion = request.args.get('emotion', 'neutral')

    cursor.execute('SELECT name, anger_amt, contempt_amt, disgust_amt, fear_amt, happiness_amt, neutral_amt, sadness_amt, surprise_amt FROM movies WHERE name=?', (movie, ))

    movie = list(cursor.fetchone())

    movie.append(movie_names[movie[0]])
    movie.append(movie_videos[movie[0]])

    cursor.close()
    connection.close()

    return render_template('details.html', movie=movie)

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/team')
def team():
    return render_template('Team.html')

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run(host="0.0.0.0", port=8000)