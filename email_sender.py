import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

email_sender = os.getenv("email_sender")
email_password = os.getenv("email_password")
smtp_server = os.getenv("smtp_server")
smtp_port = int(os.getenv("smtp_port", 465))  

site_name = 'https://dvmn.org/profession-ref-program/egor.bezborodoff/eCOFs/'
friend_name = 'Кирилл Клементьев'
sender_name = 'Егор'

msg = MIMEMultipart()
msg["From"] = email_sender
msg["To"] = email_sender
msg["Subject"] = "Приглашение на курс"

body = """Привет, {1}! {2} приглашает тебя на сайт {0}!

{0} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {0}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {0} 
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(site_name, friend_name, sender_name)

msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.login(email_sender, email_password)
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()