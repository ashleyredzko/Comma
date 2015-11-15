from flask import Flask, render_template

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/demo')
def demo():
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