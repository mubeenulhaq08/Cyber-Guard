from flask import Flask, render_template, request
import hashlib
import re

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Password Strength Checker
@app.route("/password", methods=["GET", "POST"])
def password():
    strength = ""
    if request.method == "POST":
        pwd = request.form["password"]

        if (len(pwd) >= 8 and
            re.search("[A-Z]", pwd) and
            re.search("[a-z]", pwd) and
            re.search("[0-9]", pwd) and
            re.search("[@#$!]", pwd)):
            strength = "Strong Password 💪"
        else:
            strength = "Weak Password ❌"

    return render_template("password.html", strength=strength)

# Password Hashing Demo
@app.route("/hash", methods=["GET", "POST"])
def hash_password():
    hashed = ""
    if request.method == "POST":
        pwd = request.form["password"]
        hashed = hashlib.sha256(pwd.encode()).hexdigest()

    return render_template("hash.html", hashed=hashed)

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
