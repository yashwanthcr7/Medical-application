from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# create connection to MySQL database
conn = mysql.connector.connect(
  host="3.109.182.164",
  user="root",
  password="1234",
  database="mydb"
)

# home page
@app.route('/')
def home():
    return render_template('home.html')

# add patient page
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        # get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        gender = request.form['gender']
        diagnosis = request.form['diagnosis']
        covid = request.form['covid']
        address = request.form['address']

        # create cursor
        cursor = conn.cursor()

        # execute query to insert new patient
        query = "INSERT INTO patients (first_name, last_name, dob, gender, diagnosis, covid, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, dob, gender,  diagnosis, covid, address)
        cursor.execute(query, values)

        # commit changes to database
        conn.commit()

        # close cursor
        cursor.close()

        return 'Patient added successfully'
    else:
        return render_template('add_patient.html')

# view patients page
@app.route('/view_patients')
def view_patients():
    # create cursor
    cursor = conn.cursor()

    # execute query to get all patients
    query = "SELECT * FROM patients"
    cursor.execute(query)

    # get results
    patients = cursor.fetchall()

    # close cursor
    cursor.close()

    return render_template('view_patients.html', patients=patients)

if __name__ == '__main__':
    app.run(debug=True)

