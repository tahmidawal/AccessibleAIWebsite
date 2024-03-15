from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100))
    client_email = db.Column(db.String(100))
    appointment_time = db.Column(db.String(50))

@app.route('/')
def index():
    appointments = Appointment.query.all()
    return render_template('index.html', appointments=appointments)

@app.route('/add_appointment', methods=['POST', 'GET'])
def add_appointment():
    if request.method == 'POST':
        client_name = request.form.get('client_name')
        client_email = request.form.get('client_email')
        appointment_time = request.form.get('appointment_time')

        new_appointment = Appointment(client_name=client_name, client_email=client_email, appointment_time=appointment_time)
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_appointment.html')

# ... [the rest of your code]

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
