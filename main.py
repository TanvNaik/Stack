from flask import Flask, render_template, request, url_for
import smtplib
from flask_mail import Mail, Message
import socket
from email.message import EmailMessage

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jaggudixit686@gmail.com'
app.config['MAIL_PASSWORD'] = 'jaggu@5252'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# socket.getaddrinfo('127.0.0.1', 5000)

mail = Mail(app)

def mailing():
    msg = Message('Hello', sender='jaggudixit686@gmail.com', recipients=['jagmohandixit686@gmail.com'])
    mail.send(msg)

@app.route('/')
# @app.route('/about')
def home():
    return render_template('index.html')

@app.route('/home')
def homes():
    return render_template('home.html')
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @app.route('/services')
# def services():
#     return render_template('services.html')
#
# @app.route('/portfolio')
# def portfolio():
#     return render_template('portfolio.html')
#
# @app.route('/team')
# def team():
#     return render_template('team.html')
#
# @app.route('/dropdown')
# def dropdown():
#     return render_template('index.html')
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/testinomial')
# def testinomial():
#     return render_template('testinomial.html')

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