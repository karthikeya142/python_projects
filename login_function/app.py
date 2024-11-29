from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production

# Simulated user database (you would replace this with a real database)
users = {
    'john_doe': {'password': 'password123', 'email': 'john_doe@example.com'},
    'jane_smith': {'password': 'password456', 'email': 'jane_smith@example.com'}
}


# Function to check if username exists
def username_exists(username):
    return username in users


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username exists and password matches
        if username_exists(username) and users[username]['password'] == password:
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/dashboard/<username>')
def dashboard(username):
    if username_exists(username):
        user_info = users[username]
        return render_template('dashboard.html', username=username, email=user_info['email'])
    else:
        flash('User not found. Please log in.', 'error')
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, flash
#
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Change this to a secure key in production
#
# # Simulated user database (you would replace this with a real database)
# users = {
#     'john_doe': {'password': 'password123', 'email': 'john_doe@example.com'},
#     'jane_smith': {'password': 'password456', 'email': 'jane_smith@example.com'}
# }
#
#
# # Function to check if username exists
# def username_exists(username):
#     return username in users
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         # Check if username exists and password matches
#         if username_exists(username) and users[username]['password'] == password:
#             flash('Logged in successfully!', 'success')
#             return redirect(url_for('dashboard', username=username))
#         else:
#             flash('Invalid username or password. Please try again.', 'error')
#             return redirect(url_for('index'))
#
#     return render_template('index.html')
#
#
# @app.route('/create_account', methods=['GET', 'POST'])
# def create_account():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#
#         if username_exists(username):
#             flash('Username already exists. Please choose a different one.', 'error')
#             return redirect(url_for('create_account'))
#         else:
#             users[username] = {'password': password, 'email': email}
#             flash('Account created successfully! Please log in.', 'success')
#             return redirect(url_for('index'))
#
#     return render_template('create_account.html')
#
#
# @app.route('/dashboard/<username>')
# def dashboard(username):
#     if username_exists(username):
#         user_info = users[username]
#         return render_template('dashboard.html', username=username, email=user_info['email'])
#     else:
#         flash('User not found. Please log in.', 'error')
#         return redirect(url_for('index'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
