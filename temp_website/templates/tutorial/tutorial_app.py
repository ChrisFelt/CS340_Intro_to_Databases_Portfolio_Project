# @app.route('/main')
# def main():
#     return render_template("main.j2", people=people_from_app_py)

# @app.route('/bsg-people')
# def bsg_people():
#     query = "SELECT * FROM bsg_people;"
#     cursor = db.execute_query(db_connection=db_connection, query=query)
#     results = cursor.fetchall()
#     return render_template("bsg.j2", bsg_people=results)

# @app.route("/people", methods=["POST", "GET"])
# def people():
#     if request.method == "GET":
#         query = "SELECT bsg_people.id, fname, lname, bsg_planets.name AS homeworld, age FROM bsg_people LEFT JOIN bsg_planets ON homeworld = bsg_planets.id"
#         cur = mysql.connection.cursor()
#         cur.execute(query)
#         data = cur.fetchall()

#         query2 = "SELECT id, name FROM bsg_planets"
#         cur = mysql.connection.cursor()
#         cur.execute(query2)
#         homeworld_data = cur.fetchall()

#         return render_template("people.j2", data=data, homeworlds=homeworld_data)

#     if request.method == "POST":
#         if request.form.get("Add_Person"):
#             fname = request.form["fname"]
#             lname = request.form["lname"]
#             homeworld = request.form["homeworld"]
#             age = request.form["age"]

#             if age == "" and homeworld == "0":
#                 query = "INSERT INTO bsg_people (fname, lname) VALUES (%s, %s)"
#                 cur = mysql.connection.cursor()
#                 cur.execute(query, (fname, lname))
#                 mysql.connection.commit()
#             elif homeworld == "0":
#                 query = "INSERT INTO bsg_people (fname, lname, age) VALUE (%s, %s, %s)"
#                 cur = mysql.connection.cursor()
#                 cur.execute(query, (fname, lname, age))
#                 mysql.connection.commit()
#             elif age == "":
#                 query = "INSERT INTO bsg_people (fname, lname, homeworld) VALUE (%s, %s, %s)"
#                 cur = mysql.connection.cursor()
#                 cur.execute(query, (fname, lname, homeworld))
#                 mysql.connection.commit()
#             else:
#                 query = "INSERT INTO bsg_people (fname, lname, homeworld, age) VALUE (%s, %s, %s, %s)"
#                 cur = mysql.connection.cursor()
#                 cur.execute(query, (fname, lname, homeworld, age))
#                 mysql.connection.commit()
            
#             return redirect("/people")

# @app.route("/delete_people/<int:id>")
# def delete_people(id):
#     query = "DELETE FROM bsg_people WHERE id = '%s';"
#     cur = mysql.connection.cursor()
#     cur.execute(query, (id,))
#     mysql.connection.commit()

#     return redirect("/people")

# @app.route("/edit_people/<int:id>", methods=["POST", "GET"])
# def edit_people(id):
    # if request.method == "GET":
    #     query = "SELECT * FROM bsg_people WHERE id = %s" % (id)
    #     cur = mysql.connection.cursor()
    #     cur.execute(query)
    #     data = cur.fetchall()

    #     query2 = "SELECT id, name FROM bsg_planets"
    #     cur = mysql.connection.cursor()
    #     cur.execute(query2)
    #     homeworld_data = cur.fetchall()

    #     return render_template("edit_people.j2", data=data, homeworlds=homeworld_data)

    # if request.method == "POST":
    #     if request.form.get("Edit_Person"):
    #         id = request.form["personID"]
    #         fname = request.form["fname"]
    #         lname = request.form["lname"]
    #         homeworld = request.form["homeworld"]
    #         age = request.form["age"]

    #         if (age == "" or age == "None") and homeworld == "0":
    #             query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = NULL, bsg_people.age = NULL WHERE bsg_people.id = %s"
    #             cur = mysql.connection.cursor()
    #             cur.execute(query, (fname, lname, id))
    #             mysql.connection.commit()
    #         elif homeworld == "0":
    #             query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = NULL, bsg_people.age = %s WHERE bsg_people.id = %s"
    #             cur = mysql.connection.cursor()
    #             cur.execute(query, (fname, lname, age, id))
    #             mysql.connection.commit()
    #         elif age == "":
    #             query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = NULL WHERE bsg_people.id = %s"
    #             cur = mysql.connection.cursor()
    #             cur.execute(query, (fname, lname, homeworld, id))
    #             mysql.connection.commit()
    #         else:
    #             query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = %s WHERE bsg_people.id = %s"
    #             cur = mysql.connection.cursor()
    #             cur.execute(query, (fname, lname, homeworld, age, id))
    #             mysql.connection.commit()

    #         return redirect("/people")