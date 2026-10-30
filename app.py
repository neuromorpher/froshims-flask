import sqlite3
from db_connection import connect_db 
from flask import Flask, render_template, request, redirect  

app = Flask(__name__)

# REGISTRANTS = {}

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":     

        # Validate name first 

        name = request.form.get("name") 
        if not name: 
            return render_template("error.html", message="Missing name") 

        # Then Validate Sport 

        sport = request.form.get("sport") 
        if sport not in SPORTS:

            return render_template("error.html", message="Invalid sport")  

        #REGISTRANTS[name] = sport 

        conn = connect_db("froshims.db")

        try: 
            conn.execute(
            """ 
            CREATE TABLE if not exists registrants (

                id integer, 
                name varchar(50) not null,
                sport varchar(20) not null,
                primary key(id)
                );
            """)

            conn.execute(
            """
            INSERT INTO registrants(name, sport)
            values(?, ?)
            """,(name, sport)) 

            '''
            return render_template("success.html", name=request.form.get("name")) 
            '''

        except sqlite3.Error as e:
            print(f"Error:{e}") 

        finally: 
            conn.commit() 
            conn.close() 

        return redirect("/registrants") 

    return render_template("index.html", sports=SPORTS)  

@app.route("/registrants") 
def registrants():

    conn = connect_db("froshims.db") 
    registrants = conn.execute("SELECT * FROM registrants").fetchall() 
    conn.close() 
    return render_template("registrants.html", registrants=registrants)

@app.route("/deregister", methods=["POST"]) 
def deregister():

    id = request.form.get("id")
    if id:

        conn = connect_db("froshims.db") 
        conn.execute("""
        delete from registrants where id = ?

        """, id) 
        conn.commit() 
        conn.close()
        return redirect("/registrants") 

