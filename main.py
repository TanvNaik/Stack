from flask import Flask, render_template, request, url_for, redirect
import os
import smtplib


app = Flask(__name__)

host = os.environ.get('host')
sender_email = os.environ.get('senderEmail')
email_pass = os.environ.get('emailPass')

def send_email(user, pwd, recipient, subject, body):


    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body
    
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    with smtplib.SMTP_SSL(host="mail.stackx.online") as smtp:
        smtp.login(user,pwd)
        smtp.sendmail(user,TO,message)
        smtp.quit()




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form_mail', methods=['POST'])
def form_mail():

    email = request.form['email']
    mail_type = request.form['mail_type']

    if mail_type == "query-mail":
        subject = request.form['subject'] 
        message = request.form['message']
        send_email(sender_email, email_pass, email, "Thankyou for contacting us","Our representative will reach to you soon.\nTeam Stackx")
        
    else:
        send_email(sender_email, email_pass, email, "ThankYou", "Thankyou For subscribing NewsLetter")
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)

