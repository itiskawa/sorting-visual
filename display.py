from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

#defines how to access this page
@app.route("/") # here, it's the home page
# makes a home page
def home(methods = ["POST", "GET"]):
    if request.method == "POST":
        return render_template("login.html", content = "le pain")
        print(form.request["size"])
    else:
        return render_template("index.html", content="DIDN'T WORK")



@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)