from flask import Flask, url_for
import smtplib  # Импортируем библиотеку по работе с SMTP
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'
app.secret_key = 'eaa2cc52a16507cf194e4f0c'

with app.app_context():
    def generate_token(email):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return serializer.dumps(email)

    def send_email(email, token):
        link = url_for('change_password', token=token, _external=True)

        addr_from = "sharipovaydar2@yandex.ru"
        addr_to = email
        password = "D8u5GS4v!xEwh.i"  # пароль от почты addr_from

        msg = MIMEMultipart()   # Создаем сообщение
        msg['From'] = addr_from     # Адресат
        msg['To'] = addr_to     # Получатель
        msg['Subject'] = 'Восстановление пароля'   # Тема сообщения

        body = f"Для восстановления пароля перейдите по следующей ссылке: {link}"
        msg.attach(MIMEText(body, 'plain'))      # Добавляем в сообщение текст

        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP
        server.login(addr_from, password)  # Получаем доступ
        server.send_message(msg)  # Отправляем сообщение
        server.quit()  # Выходим