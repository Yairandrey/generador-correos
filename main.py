import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_email = 'yarodriguezn@ufpso.edu.co'
password = "correo"

recipent = 'yairrodrigueznavarro@gmail.com'

message = MIMEMultipart()
message['From'] = your_email
message['To'] = recipent
message['Subject'] = 'Email de prueba con Python'


body = 'Hola, buenos días querido Yair, la presente es para informarte que estoy mandando correos de prueba con Python'
message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(your_email,password)

smtp_server.sendmail(your_email,recipent,message.as_string())
smtp_server.quit()
print(f'Correo enviado a {recipent}')


