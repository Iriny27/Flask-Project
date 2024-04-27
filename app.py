from flask import Flask, request, render_template, redirect, url_for
import sqlite3


app = Flask(__name__)

# Function to create a database connection
def get_db_connection():
    conn = sqlite3.connect('registration.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to initialize the database
def init_db():
    conn = get_db_connection()
    with app.open_resource('schema.sql', mode='r') as f:
        conn.executescript(f.read())
    conn.close()

# Initialize the database when the application starts
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/register', methods=['POST'])
def register():
    # Get form data
    full_name = request.form['full_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    birth_date = request.form['birth_date']
    gender = request.form['gender']
    address_line1 = request.form['address_line1']
    address_line2 = request.form['address_line2']
    country = request.form['country']
    city = request.form['city']
    region = request.form['region']
    postal_code = request.form['postal_code']
    
    # Insert data into the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO registrations (full_name, email, phone_number, birth_date, gender, address_line1, address_line2, country, city, region, postal_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (full_name, email, phone_number, birth_date, gender, address_line1, address_line2, country, city, region, postal_code))
    conn.commit()
    conn.close()
    
    # Redirect to success page
    return redirect(url_for('success'))

if __name__ == "__main__":
    app.run(debug=True)
