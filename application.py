import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///Elections.db")

@app.route("/")
def index():
    partys=db.execute("SELECT * FROM partys")
    return render_template("index.html",partys=partys)



@app.route("/register", methods=["GET", "POST"])
def register():
        # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("must provide password", 400)

        if request.form.get("password") == "" or  request.form.get("confirmation") == "":
            return apology("no correct password", 400)

        if request.form.get("password") == "" or  request.form.get("confirmation") == "":
            return apology("no correct password", 400)

        # Ensure password was submitted
        if not request.form.get("age"):
            return apology("no correct age", 400)

        # Ensure password was submitted
        if not request.form.get("sex"):
            return apology("no correct sex", 400)

        # Ensure password was submitted
        if not request.form.get("city"):
            return apology("no correct city", 400)

        # Ensure password was submitted
        if not request.form.get("district"):
            return apology("no correct district", 400)


         # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = LOWER(?)", request.form.get("username"))

        # Ensure username doesnt exists and password is exist
        if rows:
            return apology("There is already a user with your username", 400)

        else:
            password_hash = generate_password_hash(request.form.get("password"))
            # Query database to insert username and password
            db.execute("INSERT INTO users (username,hash,age,sex,city,district,party) VALUES (?,?,?,?,?,?,?)", request.form.get("username"),password_hash, request.form.get("age"), request.form.get("sex"), request.form.get("city"),request.form.get("district"), request.form.get("party"))

        # Redirect user to home page
        return render_template("login.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        partys=db.execute("SELECT * FROM partys")
        return render_template("register.html",partys=partys)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))


        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["user_age"] = rows[0]["age"]
        session["user_sex"] = rows[0]["sex"]
        session["user_city"] = rows[0]["city"]
        session["user_party"] = rows[0]["party"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/candidates")
def candidates():
    "Show candidates and information related"
    partys=db.execute("SELECT * FROM partys")
    return render_template("candidates.html",partys=partys)


@app.route("/statistics")
def statistics():
    "Show survey results and other information"
    president=db.execute("SELECT id_candidate_election, COUNT(*) as N FROM answer GROUP BY id_candidate_election")
    congress=db.execute("SELECT congress_party_id, COUNT(*) as P FROM answer GROUP BY congress_party_id")
    answer=db.execute("SELECT * FROM answer")
    partys=db.execute("SELECT * FROM partys")
    survey_ipsos=db.execute("SELECT * FROM survey_ipsos")
    return render_template("statistics.html",survey_ipsos=survey_ipsos,partys=partys,answer=answer,president=president,congress=congress)


@app.route("/survey", methods=["GET","POST"])
@login_required
def survey():
    if request.method=="POST":

        president=request.form.get("president")
        congress_party=request.form.get("congress_party")
        congress_1=request.form.get("congress_1")
        congress_2=request.form.get("congress_2")

        db.execute("INSERT INTO answer (id,age,sex,city,party,id_candidate_election,congress_party_id,id_candidate_congress_1,id_candidate_congress_2) VALUES (?,?,?,?,?,?,?,?,?)", session["user_id"],session["user_age"],session["user_sex"],session["user_city"],session["user_party"],president,congress_party,congress_1,congress_2)
        return redirect("/candidates")
    else:
        user = db.execute("SELECT * FROM answer WHERE id = ?",session["user_id"])
        if user:
            return render_template("answered.html")
        else:
            partys=db.execute("SELECT * FROM partys")
            return render_template("survey.html",partys=partys)
