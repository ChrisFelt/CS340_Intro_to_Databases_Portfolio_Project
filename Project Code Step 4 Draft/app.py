from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# CONFIGURATION
app = Flask(__name__)
db_connection = db.connect_to_database()

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_feltc'
app.config['MYSQL_PASSWORD'] = 'xxxx' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_feltc'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)


# ROUTES
@app.route('/')
def home():
    return redirect("/index")


@app.route('/index')
def index():
    return render_template("index.jinja2")


@app.route('/users', methods=["POST", "GET"])
def user():
    if request.method == "GET":
        query = """SELECT Users.userID AS 'User ID', 
                        firstName AS 'First Name', 
                        lastName AS 'Last Name', 
                        address AS Address, 
                        specialization AS Specialization, 
                        bio AS Biography 
                    FROM Users"""
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        usersQuery = "SELECT CONCAT(firstName, ' ', lastName) FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(usersQuery)
        users = cur.fetchall()

        return render_template("users.jinja2", data=data, users=users)

    if request.method == "POST":
        """
        TODO: Create more user friendly error message when firstName/lastName are not unique.
        """
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        address = request.form["address"]
        specialization = request.form["specialization"]
        bio = request.form["bio"]

        if request.form.get("Add_User"):
            # account for null specialization AND bio
            if specialization == "" and bio == "":
                # mySQL query to insert a new person into bsg_people with our form inputs
                query = "INSERT INTO Users (firstName, lastName, address) VALUES (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, address))
                mysql.connection.commit()
            # account for null specialization
            elif specialization == "":
                query = "INSERT INTO Users (firstName, lastName, address, bio) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, address, bio))
                mysql.connection.commit()
            # account for null bio
            elif bio == "":
                query = "INSERT INTO Users (firstName, lastName, address, specialization) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, address, specialization))
                mysql.connection.commit()
            # account for NO null
            else:
                query = "INSERT INTO Users (firstName, lastName, address, specialization, bio) VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, address, specialization, bio))
                mysql.connection.commit()

            return redirect("/users")


@app.route('/rocks', methods=["POST", "GET"])
def rock():
    if request.method == "GET":
        query = """SELECT Rocks.rockID AS 'Rock Number', 
                        Rocks.name AS 'Rock Name', 
                        CONCAT(Users.firstName, ' ', Users.lastName) AS Owner, 
                        Rocks.geoOrigin AS 'Place of Origin', 
                        Rocks.type AS 'Rock Type', 
                        Rocks.description AS 'Description', 
                        Rocks.chemicalComp AS 'Chemical Composition' 
                    FROM Rocks 
                        INNER JOIN Users ON Rocks.userID = Users.userID"""
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        usersQuery = "SELECT CONCAT(firstName, ' ', lastName) FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(usersQuery)
        users = cur.fetchall()

        return render_template("rocks.jinja2", data=data, users=users)


@app.route('/reviews', methods=["POST", "GET"])
def review():
    if request.method == "GET":
        query = "SELECT Reviews.reviewID, CONCAT(Users.firstName, ' ', Users.lastName) AS Reviewer, Rocks.name AS Rock, Reviews.title AS Title, Reviews.body AS Review, Reviews.rating AS Rating FROM Reviews LEFT JOIN Users ON Reviews.userID = Users.userID INNER JOIN Rocks ON Reviews.rockID = Rocks.rockID ORDER BY Reviews.reviewID ASC"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        usersQuery = "SELECT CONCAT(firstName, ' ', lastName) FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(usersQuery)
        users = cur.fetchall()

        rocksQuery = "SELECT name FROM Rocks"
        cur = mysql.connection.cursor()
        cur.execute(rocksQuery)
        rocks = cur.fetchall()

        review_id_query = "SELECT reviewID FROM Reviews"
        cur = mysql.connection.cursor()
        cur.execute(review_id_query)
        reviews = cur.fetchall()

        return render_template("reviews.jinja2", data=data, rocks=rocks, users=users, reviews=reviews)


@app.route('/shipments', methods=["POST", "GET"])
def shipment():
    # READ Shipment data
    if request.method == "GET":
        shipmentsQuery = """SELECT Shipments.shipmentID AS 'Shipment Number', 
                                CONCAT(Users.firstName, ' ', Users.lastName) AS 'User', 
                                Shipments.shipOrigin AS 'Origin', 
                                Shipments.shipDest AS 'Destination', 
                                Shipments.shipDate AS 'Date Shipped', 
                                Shipments.miscNote AS 'Notes' 
                                FROM Shipments 
                                    INNER JOIN Users 
                                        ON Shipments.userID = Users.userID"""
        cur = mysql.connection.cursor()
        cur.execute(shipmentsQuery)
        data = cur.fetchall()

        rocksQuery = "SELECT name FROM Rocks"
        cur = mysql.connection.cursor()
        cur.execute(rocksQuery)
        rocks = cur.fetchall()

        usersQuery = "SELECT CONCAT(firstName, ' ', lastName) FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(usersQuery)
        users = cur.fetchall()

        shipment_id_query = "SELECT shipmentID FROM Shipments"
        cur = mysql.connection.cursor()
        cur.execute(shipment_id_query)
        shipment_ids = cur.fetchall()

        return render_template("shipments.jinja2", data=data, rocks=rocks, users=users, shipment_ids=shipment_ids)

    # CREATE Shipment
    if request.method == "POST":
        user = request.form["user"]
        rock = request.form["rock"]
        shipOrigin = request.form["shipOrigin"]
        shipDest = request.form["shipDest"]
        shipDate = request.form["shipDate"]
        miscNote = request.form["miscNote"]

        if request.form.get("Add_Shipment"):
            # account for null miscNote
            if miscNote == "":
                # first, SQL query to insert new Shipment
                shipQuery = """INSERT INTO Shipments (userID, shipOrigin, shipDest, shipDate, miscNote) 
                                VALUES ((SELECT userID FROM Users WHERE CONCAT(firstName, ' ', lastName) = %s), %s, %s, %s, NULL)"""
                cur = mysql.connection.cursor()
                cur.execute(shipQuery, (user, shipOrigin, shipDest, shipDate))
                mysql.connection.commit()
                # next, SQL query to insert new Shipments_has_Rocks
                shipRockQuery = """INSERT INTO Shipments_has_Rocks (shipmentID, rockID) 
                                    VALUES ((SELECT shipmentID FROM Shipments 
                                        WHERE shipOrigin = %s 
                                            AND shipDest = %s 
                                            AND shipDate = %s 
                                            AND miscNote IS NULL), 
                                    (SELECT rockID FROM Rocks WHERE name = %s))"""
                cur = mysql.connection.cursor()
                cur.execute(shipRockQuery, (shipOrigin, shipDest, shipDate, rock))
                mysql.connection.commit()
            # account for NO null
            else:
                # first, SQL query to insert new Shipment
                shipQuery = """INSERT INTO Shipments (userID, shipOrigin, shipDest, shipDate, miscNote) 
                                VALUES ((SELECT userID FROM Users WHERE CONCAT(firstName, ' ', lastName) = %s), %s, %s, %s, %s)"""
                cur = mysql.connection.cursor()
                cur.execute(shipQuery, (user, shipOrigin, shipDest, shipDate, miscNote))
                mysql.connection.commit()
                # next, SQL query to insert new Shipments_has_Rocks
                shipRockQuery = """INSERT INTO Shipments_has_Rocks (shipmentID, rockID) 
                                    VALUES ((SELECT shipmentID FROM Shipments 
                                        WHERE shipOrigin = %s 
                                            AND shipDest = %s 
                                            AND shipDate = %s 
                                            AND miscNote = %s), 
                                    (SELECT rockID FROM Rocks WHERE name = %s))"""
                cur = mysql.connection.cursor()
                cur.execute(shipRockQuery, (shipOrigin, shipDest, shipDate, miscNote, rock))
                mysql.connection.commit()

            return redirect("/shipments")


@app.route('/edit_user/<int:id>', methods=["POST", "GET"])
def edit_user(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Users WHERE userID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_user.jinja2", data=data)

    if request.method == "POST":
        if request.method == "POST":
            """
            TODO: Create more user friendly error message when firstName/lastName are not unique.
            """
            userID = request.form["userID"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            address = request.form["address"]
            specialization = request.form["specialization"]
            bio = request.form["bio"]

            if request.form.get("Edit_User"):
                # account for null specialization AND bio
                if specialization == "" and bio == "":
                    # mySQL query to insert a new person into bsg_people with our form inputs
                    query = "UPDATE Users SET Users.firstName = %s, Users.lastName = %s, Users.address = %s, Users.specialization = NULL, Users.bio = NULL WHERE Users.userID = %s"
                    cur = mysql.connection.cursor()
                    cur.execute(query, (firstName, lastName, address, userID))
                    mysql.connection.commit()
                # account for null specialization
                elif specialization == "":
                    query = "UPDATE Users SET Users.firstName = %s, Users.lastName = %s, Users.address = %s, Users.specialization = NULL, Users.bio = %s WHERE Users.userID = %s"
                    cur = mysql.connection.cursor()
                    cur.execute(query, (firstName, lastName, address, bio, userID))
                    mysql.connection.commit()
                # account for null bio
                elif bio == "":
                    query = "UPDATE Users SET Users.firstName = %s, Users.lastName = %s, Users.address = %s, Users.specialization = %s, Users.bio = NULL WHERE Users.userID = %s"
                    cur = mysql.connection.cursor()
                    cur.execute(query, (firstName, lastName, address, specialization, userID))
                    mysql.connection.commit()
                # account for NO null
                else:
                    query = "UPDATE Users SET Users.firstName = %s, Users.lastName = %s, Users.address = %s, Users.specialization = %s, Users.bio = %s WHERE Users.userID = %s"
                    cur = mysql.connection.cursor()
                    cur.execute(query, (firstName, lastName, address, specialization, bio, userID))
                    mysql.connection.commit()

            return redirect("/users")


# edit Shipments and Shipments_has_Rocks page
@app.route('/edit_shipment/<int:id>', methods=["POST", "GET"])
def edit_shipment(id):
    # READ Shipment data
    if request.method == "GET":

        # get shipment data with some snappy monikers
        readShipmentQuery = """SELECT Shipments.shipmentID AS 'Shipment Number', 
                                CONCAT(Users.firstName, ' ', Users.lastName) AS 'User', 
                                Shipments.shipOrigin AS 'Origin', 
                                Shipments.shipDest AS 'Destination', 
                                Shipments.shipDate AS 'Date Shipped', 
                                Shipments.miscNote AS 'Notes'
                                FROM Shipments 
                                    INNER JOIN Users 
                                        ON Shipments.userID = Users.userID 
                                WHERE Shipments.shipmentID = %s""" % (id)
        cur = mysql.connection.cursor()
        cur.execute(readShipmentQuery)
        readShipment = cur.fetchall()

        # get shipment data vanilla style
        editShipmentQuery = """SELECT Shipments.shipmentID, 
                                CONCAT(Users.firstName, ' ', Users.lastName), 
                                Shipments.shipOrigin, 
                                Shipments.shipDest, 
                                Shipments.shipDate, 
                                Shipments.miscNote
                                FROM Shipments 
                                    INNER JOIN Users 
                                        ON Shipments.userID = Users.userID 
                                WHERE Shipments.shipmentID = %s""" % (id)
        cur = mysql.connection.cursor()
        cur.execute(editShipmentQuery)
        editShipment = cur.fetchall()

        # get Rock names and their owner's names 
        rocksQuery = """SELECT Shipments_has_Rocks.shipmentHasRockID,
                            CONCAT(Users.firstName, ' ', Users.lastName) AS 'Owner', 
                            Rocks.name AS 'Rock Name' 
                            From Shipments_has_Rocks
                                INNER JOIN Shipments
                                    ON Shipments_has_Rocks.shipmentID = Shipments.shipmentID
                                INNER JOIN Rocks
                                    ON Shipments_has_Rocks.rockID = Rocks.rockID
                                LEFT JOIN Users
                                    ON Rocks.userID = Users.userID
                            WHERE Shipments_has_Rocks.shipmentID = %s""" % (id)
        cur = mysql.connection.cursor()
        cur.execute(rocksQuery)
        rocks = cur.fetchall()

        # get Rock names and their owner's names 
        addRocksQuery = """SELECT Rocks.name AS rock
                            From Rocks
                                WHERE rockID NOT IN (SELECT rockID FROM Shipments_has_Rocks WHERE shipmentID = %s)""" % (id)
        cur = mysql.connection.cursor()
        cur.execute(addRocksQuery)
        addRocks = cur.fetchall()
        
        # get all User names BESIDES the original User in the Shipment
        shipUsersOptionQuery = """SELECT CONCAT(firstName, ' ', lastName) AS name
                                    FROM Users 
                                    WHERE userID != (SELECT userID from Shipments WHERE shipmentID = %s)
                                    GROUP BY name""" % (id)
        cur = mysql.connection.cursor()
        cur.execute(shipUsersOptionQuery)
        shipUsersOption = cur.fetchall()

        # get the original User in the Shipment
        shipUserQuery = """SELECT CONCAT(firstName, ' ', lastName) AS name 
                            FROM Users 
                            WHERE userID = (SELECT userID from Shipments WHERE shipmentID = %s)""" % (id)
        cur = mysql.connection.cursor()
        cur.execute(shipUserQuery)
        shipUser = cur.fetchall()

        return render_template("edit_shipment.jinja2", readShipment=readShipment, editShipment=editShipment, rocks=rocks, addRocks=addRocks, shipUsersOption=shipUsersOption, shipUser=shipUser)

    # UPDATE Shipment
    if request.method == "POST":
        # update shipment attributes only
        if request.form.get("Edit_Shipment"):

            # gather variables from Add_Shipment form
            user = request.form["user"]
            shipOrigin = request.form["shipOrigin"]
            shipDest = request.form["shipDest"]
            shipDate = request.form["shipDate"]
            miscNote = request.form["miscNote"]

            # account for null miscNote
            if miscNote == "":
                # first, SQL query to insert new Shipment
                shipUpdateQuery = """UPDATE Shipments
                                        SET userID = (SELECT userID FROM Users WHERE CONCAT(firstName, ' ', lastName) = %s),
                                        shipOrigin = %s,
                                        shipDest = %s,
                                        shipDate = %s, 
                                        miscNote = NULL
                                        WHERE shipmentID = %s;"""
                cur = mysql.connection.cursor()
                cur.execute(shipUpdateQuery, (user, shipOrigin, shipDest, shipDate, id))
                mysql.connection.commit()

            # account for NO null
            else:
                # first, SQL query to insert new Shipment
                shipUpdateQuery = """UPDATE Shipments
                                        SET userID = (SELECT userID FROM Users WHERE CONCAT(firstName, ' ', lastName) = %s),
                                        shipOrigin = %s,
                                        shipDest = %s,
                                        shipDate = %s,
                                        miscNote = %s
                                        WHERE shipmentID = %s;"""
                cur = mysql.connection.cursor()
                cur.execute(shipUpdateQuery, (user, shipOrigin, shipDest, shipDate, miscNote, id))
                mysql.connection.commit()

            return redirect("/shipments")


# delete Shipments
@app.route("/delete_shipment/<int:id>")
def delete_shipment(id):
    # SQL query to delete the Shipment given id
    query = "DELETE FROM Shipments WHERE shipmentID =  '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to Shipments
    return redirect("/shipments")    


# delete Shipments_has_Rocks
@app.route("/delete_shipments_has_rocks/<int:id>")
def delete_shipments_has_rocks(id):
    # save shipmentID
    shipQuery = "SELECT shipmentID FROM Shipments_has_Rocks WHERE shipmentHasRockID = %s" % (id)
    cur = mysql.connection.cursor()
    cur.execute(shipQuery)
    shipmentID = cur.fetchall()
    # get value from query
    shipmentID = str(shipmentID[0]["shipmentID"])

    # SQL query to delete the Shipment given id
    query = "DELETE FROM Shipments_has_Rocks WHERE shipmentHasRockID =  %s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # check if no Rocks left in Shipment
    checkQuery = "SELECT COUNT(shipmentID) AS count FROM Shipments_has_Rocks WHERE shipmentHasRockID = %s" % (id)
    cur = mysql.connection.cursor()
    cur.execute(checkQuery)
    checkRocks = cur.fetchall()
    # get value from query
    checkRocks = str(checkRocks[0]["count"])

    # if no Rocks left in Shipment, delete Shipment
    if checkRocks == "0":
        # delete Shipment
        deleteShipmentQuery = "DELETE FROM Shipments WHERE shipmentID = %s"
        cur = mysql.connection.cursor()
        cur.execute(deleteShipmentQuery, (shipmentID,))
        mysql.connection.commit()

        # go back to Shipments page
        return redirect("/shipments")

    else:

        # reload edit Shipment page
        return redirect("/edit_shipment/" + shipmentID)


###########################################

# LISTENER
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 57779))

    app.run(port=port, debug=True)
