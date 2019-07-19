#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<username>")
def uname(username):
    return render_template("whoyouare.html", name = username)

if __name__ == "__main__":
    app.run(port=5006)
