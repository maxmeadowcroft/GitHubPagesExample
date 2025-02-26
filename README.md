
## What is GitHub Pages?

GitHub Pages is a free hosting service provided by GitHub that allows you to publish static websites directly from a GitHub repository. It is often used for personal projects, documentation, and portfolio websites.

### Key Features:

- Free hosting for static sites.
- Direct integration with GitHub repositories.
- Supports custom domains and HTTPS.
- Automatic deployment from branches like `main` or `gh-pages`.

## Setting Up GitHub Pages for a Static Site

1. **Create a GitHub Repository**
    - Go to [GitHub](https://github.com) and create a new repository.
    - Give it a name and initialize it with a `README.md` file (optional).
2. **Add Your Static Website Files**
    - Create `index.html`, `style.css`, and any other static files.
    - Commit and push them to your repository.
3. **Enable GitHub Pages**
    - Navigate to **Settings** in your repository.
    - Scroll down to **GitHub Pages**.
    - Under "Source," select `main` or `gh-pages` branch.
    - Save changes, and GitHub will generate a URL for your site.
4. **Access Your Site**
    - Your site will be available at `https://yourusername.github.io/repository-name/`.

---

## Deploying a Flask App on GitHub Pages

GitHub Pages is designed for static sites, but you can deploy a Flask app using **Frozen-Flask**, which converts a Flask app into static files.

### Steps to Deploy:

### 1. Install Dependencies

```Shell
pip install Flask Frozen-Flask SQLAlchemy
```

### 2. Create a Basic Flask App with SQLAlchemy

Create a file called `app.py`:

```Python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

def create_db():
    with app.app_context():
        db.create_all()

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
    create_db()
    app.run(debug=True)
```

### 3. Create an HTML Form

Create a file called `templates/index.html`:

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>User List</title>
</head>
<body>
    <h1>Users</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.name }}</li>
        {% endfor %}
    </ul>
    <form method="POST">
        <input type="text" name="name" placeholder="Enter name" required>
        <button type="submit">Add User</button>
    </form>
</body>
</html>
```

### 4. Convert Flask App to Static Files

Create a `freeze.py` file:

```Python
from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
```

Run the script:

```Shell
python freeze.py
```

This will generate a `build/` folder with static files.

### 5. Push Files to GitHub

- Move the `build/` folder contents to your repository.
- Commit and push the changes.
- Follow the GitHub Pages setup steps.

### 6. View Your Deployed Flask App

Your Flask site will be available at `https://yourusername.github.io/`.

---

## Conclusion

GitHub Pages is a powerful tool for hosting static sites, and with Frozen-Flask, you can even deploy Flask applications. This guide provided an overview of GitHub Pages and a step-by-step method to host a Flask app as static content, including a basic SQLite database setup and a form for adding users.