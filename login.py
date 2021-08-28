# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from PathResolver import resource_path
from connections import Connection
from payment import Ui_Payment


class Login_Form(QMainWindow):
    def __init__(self, Payment, connection):
        super().__init__()
        self.payment_ui = Payment
        self.setObjectName("Form")
        self.setFixedSize(365, 493)
        self.center()
        self.setStyleSheet("background-color: #60a3bc")
        self.message_box = QtWidgets.QMessageBox()
        self.api = connection
        self.login_box = QtWidgets.QFrame(self)
        self.login_box.setGeometry(QtCore.QRect(23, 90, 321, 380))
        self.login_box.setAutoFillBackground(False)
        self.login_box.setStyleSheet("  background: #f39c12;\n"
                                     "  border-radius: 5px;")
        self.login_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_box.setObjectName("login_box")
        self.brand_logo = QtWidgets.QFrame(self.login_box)
        self.brand_logo.setGeometry(QtCore.QRect(77, -80, 170, 170))
        self.brand_logo.setStyleSheet("border-radius: 85px;\n"
                                      "background: #60a3bc;")
        self.brand_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.brand_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.brand_logo.setObjectName("brand_logo")
        self.login = QtWidgets.QLineEdit(self.login_box)
        self.login.setGeometry(QtCore.QRect(70, 120, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "border-bottom-left-radius: 0;\n"
                                 "border-top-left-radius: 0;")
        self.login.setText("")
        self.login.setObjectName("login")
        self.login.returnPressed.connect(self.on_submit)
        self.user_icon = QtWidgets.QLabel(self.login_box)
        self.user_icon.setGeometry(QtCore.QRect(10, 120, 60, 51))
        self.user_icon.setStyleSheet("background-color: rgb(204, 0, 0);\n"
                                     "border-top-right-radius: 0;\n"
                                     "border-bottom-right-radius: 0;")
        self.user_icon.setText("")
        self.user_icon.setObjectName("user_icon")
        self.user_icon.setAlignment(Qt.AlignCenter)
        user_image = QtGui.QImage(resource_path('img/user.png'))
        user_image = user_image.scaled(40, 40)
        self.user_icon.setPixmap(QtGui.QPixmap.fromImage(user_image))
        self.key_icon = QtWidgets.QLabel(self.login_box)
        self.key_icon.setGeometry(QtCore.QRect(10, 210, 60, 51))
        self.key_icon.setStyleSheet("background-color: rgb(204, 0, 0);\n"
                                    "border-top-right-radius: 0;\n"
                                    "border-bottom-right-radius: 0;")
        self.key_icon.setText("")
        self.key_icon.setObjectName("key_icon")
        self.key_icon.setAlignment(Qt.AlignCenter)
        key_image = QtGui.QImage(resource_path('img/key.png'))
        key_image = key_image.scaled(40, 40)
        self.key_icon.setPixmap(QtGui.QPixmap.fromImage(key_image))
        self.password = QtWidgets.QLineEdit(self.login_box)
        self.password.setGeometry(QtCore.QRect(70, 210, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-bottom-left-radius: 0;\n"
                                    "border-top-left-radius: 0;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password.returnPressed.connect(self.on_submit)
        self.pushButton = QtWidgets.QPushButton(self.login_box)
        self.pushButton.setGeometry(QtCore.QRect(20, 294, 280, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("QPushButton {background-color: rgb(204, 0, 0);\n"
                                      "color: #ffffff;\n"
                                      "}\n"
                                      "QPushButton:hover {background-color: rgb(190, 0, 0);\n"
                                      "color: #ffffff;\n"
                                      "}\n"
                                      "QPushButton:pressed {background-color: rgb(150, 0, 0);\n"
                                      "color: #ffffff;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QLabel(self)
        self.graphicsView.setGeometry(QtCore.QRect(110, 20, 150, 150))
        self.graphicsView.setStyleSheet("background-color: rgb(204, 0, 0);\n"
                                        "border-radius: 75px;")
        self.graphicsView.setAlignment(Qt.AlignCenter)
        self.graphicsView.setObjectName("graphicsView")
        logo_image = QtGui.QImage(resource_path('img/data-logo.png'))
        logo_image = logo_image.scaled(130, 130)
        self.graphicsView.setPixmap(QtGui.QPixmap.fromImage(logo_image))
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Kirish"))
        self.pushButton.clicked.connect(self.on_submit)

    def on_submit(self):
        if self.login.text() == '':
            self.message_box.setText("Iltimos loginingizni kiriting!")
            self.message_box.exec_()
        elif self.password.text() == '':
            self.message_box.setText("Iltimos parolingizni kiriting!")
            self.message_box.exec_()
        else:
            response = self.api.checkUser(self.login.text(), self.password.text())
            if response.status_code == 200:
                self.hide()
                self.payment_ui.setupUi(self.api)
                self.payment_ui.show()
            else:
                self.message_box.setText(response._content)
                self.message_box.exec_()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    connection = Connection()
    payment = Ui_Payment()
    ui = Login_Form(payment, connection)
    ui.show()
    sys.exit(app.exec_())
