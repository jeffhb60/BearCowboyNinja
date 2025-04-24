from flask import Flask, render_template, request, session, redirect, url_for
import random
from game_logic import get_winner, choices
from whitenoise import WhiteNoise
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required to use sessions
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')
@app.route("/", methods=["GET", "POST"])
def index():
    user_choice = None
    cpu_choice = None
    result = None

    if "player_score" not in session:
        session["player_score"] = 0
        session["cpu_score"] = 0

    if request.method == "POST":
        user_choice = request.form["choice"]
        cpu_choice = random.choice(choices)
        result = get_winner(user_choice, cpu_choice)

        if result == "You win!":
            session["player_score"] += 1
        elif result == "You lose!":
            session["cpu_score"] += 1

    return render_template(
        "index.html",
        user_choice=user_choice,
        cpu_choice=cpu_choice,
        result=result,
        player_score=session.get("player_score", 0),
        cpu_score=session.get("cpu_score", 0),
        choices=choices
    )

@app.route("/list-static")
def list_static():
    paths = []
    for dirpath, dirnames, filenames in os.walk("static"):
        for file in filenames:
            paths.append(os.path.join(dirpath, file))
    return "<br>".join(paths)

@app.route("/reset", methods=["GET"])
def reset():
    session["player_score"] = 0
    session["cpu_score"] = 0
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
