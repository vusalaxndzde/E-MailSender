from PyQt5 import QtWidgets, QtGui
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("Mail Sender")
        self.setWindowIcon(QtGui.QIcon("Images/images.jpg"))
        self.setGeometry(235, 130, 900, 500)

    def init_ui(self):

        self.from_email_input = QtWidgets.QLineEdit()
        self.from_email_input.setPlaceholderText("Your e-mail address: ")
        self.your_email_password = QtWidgets.QLineEdit()
        self.your_email_password.setPlaceholderText("Your Password: ")
        self.your_email_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.image = QtWidgets.QLabel()
        self.image.setPixmap(QtGui.QPixmap("Images/gmail1.png"))
        self.mail_to = QtWidgets.QLineEdit()
        self.mail_to.setPlaceholderText("To: ")
        self.subject = QtWidgets.QLineEdit()
        self.subject.setPlaceholderText("Subject")
        self.text_area = QtWidgets.QTextEdit()
        self.send_button = QtWidgets.QPushButton("Send")
        self.error_message = QtWidgets.QLabel("")
        self.error_message.setFont(QtGui.QFont("Arial", 10))

        hBox = QtWidgets.QHBoxLayout()
        hBox.addWidget(self.from_email_input)
        hBox.addWidget(self.your_email_password)
        hBox.addStretch()
        hBox.addStretch()
        hBox.addWidget(self.image)

        hBox2 = QtWidgets.QHBoxLayout()
        hBox2.addWidget(self.mail_to)
        hBox2.addStretch()

        hBox3 = QtWidgets.QHBoxLayout()
        hBox3.addWidget(self.subject)
        hBox3.addStretch()

        hBox4 = QtWidgets.QHBoxLayout()
        hBox4.addWidget(self.send_button)
        hBox4.addWidget(self.error_message)
        hBox4.addStretch()

        vBox = QtWidgets.QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addLayout(hBox2)
        vBox.addLayout(hBox3)
        vBox.addWidget(self.text_area)
        vBox.addLayout(hBox4)

        self.setLayout(vBox)

        self.send_button.clicked.connect(self.clicked)

        self.show()

    def clicked(self):
        your_mail = self.from_email_input.text()
        your_password = self.your_email_password.text()
        to = self.mail_to.text()

        if your_mail != "" and your_password == "" and to != "":
            error = "   Fill in the password field!!!"
            self.error_message.setStyleSheet("color: red")
            self.error_message.setText(error)
            self.mail_to.setStyleSheet("border: 1px solid black;")
            self.from_email_input.setStyleSheet("border: 1px solid black;")
            self.your_email_password.setStyleSheet("border: 1px solid red;")

        elif your_mail == "" and your_password != "" and to != "":
            error = "   Fill in the your e-mail field!!!"
            self.error_message.setStyleSheet("color: red")
            self.error_message.setText(error)
            self.mail_to.setStyleSheet("border: 1px solid black;")
            self.your_email_password.setStyleSheet("border: 1px solid black;")
            self.from_email_input.setStyleSheet("border: 1px solid red;")

        elif your_mail != "" and your_password != "" and to == "":
            error = "   Enter the email address to send to!!!"
            self.error_message.setStyleSheet("color: red")
            self.error_message.setText(error)
            self.from_email_input.setStyleSheet("border: 1px solid black;")
            self.your_email_password.setStyleSheet("border: 1px solid black;")
            self.mail_to.setStyleSheet("border: 1px solid red;")

        elif your_mail == "" and your_password == "" and to == "":
            error = "   Fill in the blanks!!!"
            self.error_message.setStyleSheet("color: red")
            self.error_message.setText(error)
            self.mail_to.setStyleSheet("border: 1px solid red;")
            self.from_email_input.setStyleSheet("border: 1px solid red;")
            self.your_email_password.setStyleSheet("border: 1px solid red;")

        elif your_mail == "" and your_password == "" and to != "":
            error = "   Fill in the blanks!!!"
            self.error_message.setStyleSheet("color: red")
            self.error_message.setText(error)
            self.mail_to.setStyleSheet("border: 1px solid black;")
            self.from_email_input.setStyleSheet("border: 1px solid red;")
            self.your_email_password.setStyleSheet("border: 1px solid red;")

        elif your_mail != "" and your_password == "" and to == "":
            error = "   Fill in the blanks!!!"
            self.error_message.setStyleSheet("color: red")
            self.error_message.setText(error)
            self.from_email_input.setStyleSheet("border: 1px solid black;")
            self.mail_to.setStyleSheet("border: 1px solid red;")
            self.your_email_password.setStyleSheet("border: 1px solid red;")

        elif your_mail == "" and your_password != "" and to == "":
            error = "   Fill in the blanks!!!"
            self.error_message.setStyleSheet("color: red")
            self.error_message.setText(error)
            self.your_email_password.setStyleSheet("border: 1px solid black;")
            self.mail_to.setStyleSheet("border: 1px solid red;")
            self.from_email_input.setStyleSheet("border: 1px solid red;")

        else:
            self.mail_to.setStyleSheet("border: 1px solid black;")
            self.from_email_input.setStyleSheet("border: 1px solid black;")
            self.your_email_password.setStyleSheet("border: 1px solid black;")

            message = MIMEMultipart()
            message["From"] = self.from_email_input.text()
            message["To"] = self.mail_to.text()
            message["Subject"] = self.subject.text()

            writing = self.text_area.toPlainText()

            message_body = MIMEText(writing, "plain")
            message.attach(message_body)

            try:
                mail = smtplib.SMTP("smtp.gmail.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login(self.from_email_input.text(), self.your_email_password.text())
                mail.sendmail(message["From"], message["To"], message.as_string())
                self.error_message.setText("   Email sent successfully!")
                self.error_message.setStyleSheet("color: green")
                mail.close()

            except:
                self.error_message.setText("   Check Entries!")


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
