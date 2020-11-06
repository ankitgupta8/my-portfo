from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<page_name>')
def func(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("Database.txt", mode="a") as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open("database.csv", mode="a") as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # db.write(f"\n{email}, {subject}, {message}")
        csv_write = csv.writer(
            db2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankyou.html")
    else:
        return "Something got wrong!"

    return 'Form Submitted Successfully !! '
