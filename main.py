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
    server = SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login('naiktanvi30@gmail.com', '')
    if mail_type == "query-mail":
        message = "Thankyou for your query we will contact you as son as possible !"
        name = request.form['name']
        subject = request.form['subject']
        user_message = request.form['message']
        server.sendmail('naiktanvi30@gmail.com', email, message)
        server.sendmail(email, 'naiktanvi30@gmail.com', user_message)
    else:
        message = "Thank you for subscribing to our newsletter"
        msg = "This email subscribe our newsletter !"
        server.sendmail(email, 'naiktanvi30@gmail.com', msg)
        server.sendmail('naiktanvi30@gmail.com', email, message)
    server.close()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
