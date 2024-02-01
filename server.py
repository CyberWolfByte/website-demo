from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)


@app.route('/')
def home():
    # Render your homepage
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def send_message():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')

            if not all([name, email, message]):
                return 'Error: All fields are required. Please try again.'

            save_to_csv(name, email, message)

            return redirect(url_for('thank_you'))
        except:
            # Return the exception as an error message
            return 'An error occurred'
    else:
        return render_template('index.html')


def save_to_text(name, email, message):
    with open('database.txt', 'a') as file_db:
        file_db.write(f"Name: {name}, Email: {email}, Message: {message}\n")


def save_to_csv(name, email, message):
    with open('database.csv', 'a', newline='') as csv_db:
        csv_writer = csv.writer(csv_db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/thank-you')
def thank_you():
    # Render thank you page
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
