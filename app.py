from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@{}/{}'.format('postgres',
                                                          'Ropac123',
                                                          'localhost:5432',
                                                          'test_flask')

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.app = app
db.init_app(app)


class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return self.name


db.create_all()

volunteer = Volunteer(name='Vincent')
db.session.add(volunteer)
db.session.commit()

# list_volunteers = ['Jeff', 'Robinson', 'Richard']
list_volunteers = Volunteer.query.all()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/volunteers')
def get_volunteers():
    output = ''
    for volunteer in list_volunteers:
        output += str(volunteer) + ' '
    return output
