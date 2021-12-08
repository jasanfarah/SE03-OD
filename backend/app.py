from flask import Flask, request, jsonify, redirect
import mysql.connector

app = Flask(__name__)
#Husk at ændre host til database!!
def databaseConnection():
	return mysql.connector.connect(user='root',host='localhost',database='Person', password="")

@app.route('/person',methods=['POST'])
def person():
    connector = databaseConnection()     
    cur = connector.cursor()  
    firstName = request.form["firstname"]
    lastName =  request.form["lastname"]   
    cur.execute("INSERT INTO person_table(Firstname, Lastname) VALUES (%s, %s)", (firstName, lastName))
    mysql.connection.commit()
    return redirect('https://localhost/select.html',200)

@app.route('/persons', methods=['GET'])
def persons():

    connector = databaseConnection()
    cur = connector.cursor(dictionary=True)     
    cur.execute("SELECT * FROM person_table")
    dbData = cur.fetchall()
    persons =[ ]
    for row in dbData:
        obj= {
        "Firstname": row['Firstname'],
        "PersonID" : row['PersonID'],
        "Lastname" : row['Lastname']
        }
        persons.append(obj)
    data= jsonify(persons)
    return data


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)