from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="3.111.170.253",
    user="root",
    password="1234",
    database="mydb"
)

@app.route('/')
def home():
    return 'Welcome to the Student App!'

@app.route('/students')
def students():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM students")
    students = mycursor.fetchall()
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        major = request.form['major']
        mycursor = mydb.cursor()
        sql = "INSERT INTO students (name, age, major) VALUES (%s, %s, %s)"
        val = (name, age, major)
        mycursor.execute(sql, val)
        mydb.commit()
        return 'Student added successfully!'
    else:
        return render_template('add_student.html')

