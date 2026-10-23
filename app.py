from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# -----------------------------
# MySQL Configuration
# -----------------------------

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ruby2006'
app.config['MYSQL_DB'] = 'gym_fitness'

mysql = MySQL(app)


# -----------------------------
# Home Page
# -----------------------------

@app.route('/')
def home():
    return render_template('index.html')


# -----------------------------
# Login Page
# -----------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cur.fetchone()

        cur.close()

        if user:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Email or Password"

    return render_template('login.html')


# -----------------------------
# Register Page
# -----------------------------

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute("""
            INSERT INTO users
            (full_name, email, phone, password)
            VALUES (%s, %s, %s, %s)
        """, (fullname, email, phone, password))

        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))

    return render_template('register.html')


# -----------------------------
# Membership Page
# -----------------------------

@app.route('/membership', methods=['GET', 'POST'])
def membership():

    if request.method == 'POST':

        fullname = request.form['fullname']
        email = request.form['email']
        plan = request.form['plan']
        price = request.form['price']

        if plan == 'Silver':
            duration = '1 Month'
            features = 'Gym Access, Cardio Training, Locker Facility'

        elif plan == 'Gold':
            duration = '1 Month'
            features = 'Gym Access, Cardio Training, Personal Trainer, Diet Plan'

        elif plan == 'Platinum':
            duration = '1 Month'
            features = 'Unlimited Gym Access, Personal Trainer, Diet Consultation, Steam Bath, Premium Support'

        cur = mysql.connection.cursor()

        cur.execute("""
            INSERT INTO membership
            (fullname, email, membership_name, duration, price, features)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (fullname, email, plan, duration, price, features))

        mysql.connection.commit()
        cur.close()

        return """
        <script>
            alert("Membership Joined Successfully!");
            window.location.href = "/membership";
        </script>
        """

    return render_template('membership.html')


# -----------------------------
# Trainer Page
# -----------------------------

@app.route('/trainer')
def trainer():
    return render_template('trainer.html')


# -----------------------------
# Workout Page
# -----------------------------

@app.route('/workout')
def workout():
    return render_template('workout.html')


# -----------------------------
# Diet Page
# -----------------------------

@app.route('/diet')
def diet():
    return render_template('diet.html')


# -----------------------------
# BMI Calculator Page
# -----------------------------

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')


# -----------------------------
# Gallery Page
# -----------------------------

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


# -----------------------------
# Testimonials Page
# -----------------------------

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')


# -----------------------------
# Dashboard
# -----------------------------

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# -----------------------------
# Contact
# -----------------------------

@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    cur = mysql.connection.cursor()

    cur.execute("""
        INSERT INTO contact(name, email, message)
        VALUES(%s, %s, %s)
    """, (name, email, message))

    mysql.connection.commit()
    cur.close()

    return redirect(url_for('home'))


# -----------------------------
# Run Application
# -----------------------------

if __name__ == '__main__':
    app.run(debug=True)