from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# CONFIGURATION
app = Flask(__name__)
db_connection = db.connect_to_database()

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_behringr'
app.config['MYSQL_PASSWORD'] = '1834'
app.config['MYSQL_DB'] = 'cs340_behringr'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

people_from_app_py = [
{
    "name": "Thomas",
    "age": 33,
    "location": "New Mexico",
    "favorite_color": "Blue"
},
{
    "name": "Gregory",
    "age": 41,
    "location": "Texas",
    "favorite_color": "Red"
},
{
    "name": "Vincent",
    "age": 27,
    "location": "Ohio",
    "favorite_color": "Green"
},
{
    "name": "Alexander",
    "age": 29,
    "location": "Florida",
    "favorite_color": "Orange"
}
]

# ROUTES
@app.route('/')
def home():
    return redirect("/index")

@app.route('/main')
def main():
    return render_template("main.j2", people=people_from_app_py)

@app.route('/bsg-people')
def bsg_people():
    query = "SELECT * FROM bsg_people;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("bsg.j2", bsg_people=results)

@app.route("/people", methods=["POST", "GET"])
def people():
    if request.method == "GET":
        query = "SELECT bsg_people.id, fname, lname, bsg_planets.name AS homeworld, age FROM bsg_people LEFT JOIN bsg_planets ON homeworld = bsg_planets.id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT id, name FROM bsg_planets"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        homeworld_data = cur.fetchall()

        return render_template("people.j2", data=data, homeworlds=homeworld_data)

    if request.method == "POST":
        if request.form.get("Add_Person"):
            fname = request.form["fname"]
            lname = request.form["lname"]
            homeworld = request.form["homeworld"]
            age = request.form["age"]

            if age == "" and homeworld == "0":
                query = "INSERT INTO bsg_people (fname, lname) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname))
                mysql.connection.commit()
            elif homeworld == "0":
                query = "INSERT INTO bsg_people (fname, lname, age) VALUE (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, age))
                mysql.connection.commit()
            elif age == "":
                query = "INSERT INTO bsg_people (fname, lname, homeworld) VALUE (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, homeworld))
                mysql.connection.commit()
            else:
                query = "INSERT INTO bsg_people (fname, lname, homeworld, age) VALUE (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, homeworld, age))
                mysql.connection.commit()
            
            return redirect("/people")

@app.route("/delete_people/<int:id>")
def delete_people(id):
    query = "DELETE FROM bsg_people WHERE id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/people")

@app.route("/edit_people/<int:id>", methods=["POST", "GET"])
def edit_people(id):
    if request.method == "GET":
        query = "SELECT * FROM bsg_people WHERE id = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT id, name FROM bsg_planets"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        homeworld_data = cur.fetchall()

        return render_template("edit_people.j2", data=data, homeworlds=homeworld_data)

    if request.method == "POST":
        if request.form.get("Edit_Person"):
            id = request.form["personID"]
            fname = request.form["fname"]
            lname = request.form["lname"]
            homeworld = request.form["homeworld"]
            age = request.form["age"]

            if (age == "" or age == "None") and homeworld == "0":
                query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = NULL, bsg_people.age = NULL WHERE bsg_people.id = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, id))
                mysql.connection.commit()
            elif homeworld == "0":
                query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = NULL, bsg_people.age = %s WHERE bsg_people.id = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, age, id))
                mysql.connection.commit()
            elif age == "":
                query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = NULL WHERE bsg_people.id = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, homeworld, id))
                mysql.connection.commit()
            else:
                query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = %s WHERE bsg_people.id = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, homeworld, age, id))
                mysql.connection.commit()

            return redirect("/people")

# YouBreccia Website Routes ###############
@app.route('/index')
def index():
    return render_template("index.j2")

@app.route('/users', methods=["POST", "GET"])
def user():
    if request.method == "GET":
        query = "SELECT Users.userID AS 'User ID', first_name, last_name, address, specialization, bio FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("users.j2", data=data)


@app.route('/rocks', methods=["POST", "GET"])
def rock():
    if request.method == "GET":
        query = "SELECT Rocks.rockID, name AS 'Rock Number', geoOrigin, type, description, chemicalComp FROM Rocks"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("rocks.j2", data=data)

@app.route('/reviews', methods=["POST", "GET"])
def review():
    if request.method == "GET":
        query = "SELECT Reviews.reviewID AS 'Review Number', title, body, rating FROM Reviews"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("reviews.j2", data=data)

@app.route('/shipments', methods=["POST", "GET"])
def shipment():
    if request.method == "GET":
        query = "SELECT Shipments.shipmentID AS 'Shipping Number' , shipOrigin AS 'Origin', shipDest as 'Destination', shipDate AS 'Date Shipped' FROM Shipments"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("shipments.j2", data=data)

###########################################

# LISTENER
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 41992))

    app.run(port=port, debug=True)
