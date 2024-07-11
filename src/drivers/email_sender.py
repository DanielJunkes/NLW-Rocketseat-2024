import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "sln4jurpcmbq4i2g@ethereal.email"
    login = "sln4jurpcmbq4i2g@ethereal.email"
    senha = "TNmHUeE3rFANM3JmgF"
    
    msg = MIMEMultipart()
    msg['From'] = "confirmar_viagem@emial.com"
    msg['To'] = ", ".join(to_addrs)
    msg['Subject'] = "Confirmação de viagem"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, senha)
    text = msg.as_string()
    
    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    server.quit()