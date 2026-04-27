from flask import Flask, render_template,request
import mysql.connector

app = Flask(__name__)

# connect to mysql database
conn = {
    'host': 'localhost',
    'user': 'test',
    'password': 'redhat',
    'database': 'test'
}


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')

    # # connect to mysql
    connection = mysql.connector.connect(**conn)
    cursor = connection.cursor()
    # check if the email and password match a record in the database
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    values = (email, password)
    cursor.execute(query, values)
    result = cursor.fetchone()
   
    cursor.close()
    connection.close()
    if result:
        return render_template('dashboard.html',fullname=result[1], email=result[2], role=result[3])   
    else:
        # redirect back to / route  with error message
        error = "Invalid email or password"
        return render_template('login.html', error=error)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registeruser', methods=['POST'])
def registeruser():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    role = request.form.get('role')
    password = request.form.get('password')

    # connect to mysql
    connection = mysql.connector.connect(**conn)
    cursor = connection.cursor()
    # insert the new user into the database
    query = "INSERT INTO users (fullname, email, role, password) VALUES (%s, %s, %s, %s)"
    values = (fullname, email, role, password)
    cursor.execute(query, values)
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return render_template('login.html', message="Registration successful. Please login.")  

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000, debug=True)    