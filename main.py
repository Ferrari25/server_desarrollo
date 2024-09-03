from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
#[protocolo]://[usuario]:[password]@[host]:[Puerto]/[base de datos]
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/db_desarrollo'
db = SQLAlchemy(app)


# Definición de la clase User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"{{\"id\": {self.id}, \"username\": \"{self.username}\", \"email\": \"{self.email}\"}}"

@app.route("/init")
def init():
    db.create_all()
    return "ok"

@app.get('/users')
def get_user():
    return jsonify(User.query.all())

@app.post('/users')
def add_user():
    user = request.get_json()
    dbUser = User(username=user.username, email=user.email)
    db.session.add(dbUser)
    db.session.commit()
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)