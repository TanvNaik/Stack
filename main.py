from flask import Flask, render_template, request, url_for
import os
from smtplib import  SMTP


app = Flask(__name__)

host = os.environ.get('host')
sender_email = os.environ.get('senderEmail')
email_pass = os.environ.get('emailPass')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form_mail', methods=['POST'])
def form_mail():

    email = request.form['email']
    mail_type = request.form['mail_type']
    server = SMTP(host=host, port=587)
    server.starttls()
    server.login(sender_email, email_pass)

    if mail_type == "query-mail":
        message = "Thankyou for your query we will contact you as son as possible !"
        name = request.form['name']
        subject = request.form['subject']
        user_message = request.form['message']
        server.sendmail(sender_email, email, message)
        server.sendmail(email, sender_email, user_message)
    else:
        message = "Thank you for subscribing to our newsletter"
        msg = "This email subscribe our newsletter !"
        server.sendmail(email, sender_email, msg)
        server.sendmail(sender_email, email, message)

    server.close()
    return render_template('index.html')

@app.route('/portfolio/<project>')
def portfolio_details(project):

   return render_template("portfolio-details.html", project = project)


if __name__ == '__main__':
    app.run(debug=True)
