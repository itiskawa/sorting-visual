from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#defines how to access this page
@app.route("/") # here, it's the home page
# makes a home page
def home():
    return render_template("index.html", content="yes")

if __name__ == "__main__":
    app.run(debug=True)