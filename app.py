from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For session security

@app.route('/')
def index():
    # Generate new number if it doesn't exist
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    target = session['random_number']

    if user_guess == target:
        message = "You won!"
        session.pop('random_number', None)  # Reset game
    elif user_guess < target:
        message = "Too low!"
    else:
        message = "Too high!"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
