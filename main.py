from flask import Flask, render_template, request, url_for
from smtplib import SMTP

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form_mail', methods = ['POST'])
def form_mail():
    email = request.form['email']
    mail_type = request.form['mail_type']

    if mail_type == "subcription-mail":
        message = "Thank you subscribing to our newsletter"
        name = request.form['name']
        subject = request.form['subject']
        user_message = request.form['message']
    else:
        message = "Your message has been sent. Thank you!"

    server = SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login('emailId', 'pass')
    server.sendmail('naiktanvi30@gmail.com', email, message)
    server.close()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)