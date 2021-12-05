from flask import Flask, request, render_template, jsonify, redirect
from flask_mysqldb import MySQL
import json

app = Flask(__name__, template_folder='../html')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Person'
app.config['MYSQL_CURSORCLASS'] ='DictCursor'

mysql = MySQL(app)


@app.route('/')
def start():
    return '<h1> Welcome <h1> <br> <a href="/person">Person</a> <br> <a href="/persons">Persons</a>'
@app.route('/person',methods=['POST'])
def person():
    if request.method == "POST":
        firstName = request.form['firstname']
        lastName = request.form['lastname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO person_table(Firstname, Lastname) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
    return redirect('https://localhost/select.html',code=200)

@app.route('/persons', methods=['GET'])
def persons():
        if request.method == "GET":
            cur = mysql.connection.cursor()
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