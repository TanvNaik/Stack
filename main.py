from flask import Flask, render_template, request, url_for
import smtplib
from flask_mail import Mail, Message
import socket
from email.message import EmailMessage

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jaggudixit686@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form_mail', methods=['POST'])
def form_mail():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login('jaggudixit686@gmail.com', 'jaggu@5252')
    s.sentmail('jaggudixit686@gmail.com', 'jagmohandixit686@gmail.com', message)
    s.close()

if __name__ == '__main__':
    app.run(debug=True)
