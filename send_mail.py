import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'bb976c98c13188'
    password = '00c5a5255425cb'
    message = (f"<h3>New Feedback Submission</h3>"
               f"<ul>"
               f"<li>Customer: {customer}</li>"
               f"<li>Dealer: {dealer}<li>"
               f"<li>Rating: {rating}<li>"
               f"<li>Comments: {comments}<li>"
               f"</ul>")
    sender_email = 'lexus@test.com'
    receiver_email = 'test@test.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
