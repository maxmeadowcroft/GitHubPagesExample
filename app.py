from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

def create_db():
    with app.app_context():
        db.create_all()

# Ensure the database is created before handling any requests
create_db()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            new_user = User(name=name)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))
    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
