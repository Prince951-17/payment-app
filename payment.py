# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Payment(object):
    def setupUi(self, Payment):
        Payment.setObjectName("Payment")
        Payment.resize(1006, 580)
        Payment.setModal(False)
        self.layoutWidget = QtWidgets.QWidget(Payment)
        self.layoutWidget.setGeometry(QtCore.QRect(14, 11, 981, 542))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.type_label = QtWidgets.QLabel(self.layoutWidget)
        self.type_label.setObjectName("type_label")
        self.gridLayout.addWidget(self.type_label, 1, 0, 1, 1)
        self.month = QtWidgets.QComboBox(self.layoutWidget)
        self.month.setObjectName("month")
        self.gridLayout.addWidget(self.month, 4, 3, 1, 1)
        self.group = QtWidgets.QComboBox(self.layoutWidget)
        self.group.setObjectName("group")
        self.gridLayout.addWidget(self.group, 5, 3, 1, 1)
        self.comment_label = QtWidgets.QLabel(self.layoutWidget)
        self.comment_label.setObjectName("comment_label")
        self.gridLayout.addWidget(self.comment_label, 8, 0, 1, 1)
        self.direction_label = QtWidgets.QLabel(self.layoutWidget)
        self.direction_label.setObjectName("direction_label")
        self.gridLayout.addWidget(self.direction_label, 5, 0, 1, 1)
        self.month_label = QtWidgets.QLabel(self.layoutWidget)
        self.month_label.setObjectName("month_label")
        self.gridLayout.addWidget(self.month_label, 4, 2, 1, 1)
        self.teacher_label = QtWidgets.QLabel(self.layoutWidget)
        self.teacher_label.setObjectName("teacher_label")
        self.gridLayout.addWidget(self.teacher_label, 7, 0, 1, 1)
        self.naqd = QtWidgets.QRadioButton(self.layoutWidget)
        self.naqd.setObjectName("naqd")
        self.gridLayout.addWidget(self.naqd, 1, 1, 1, 1)
        self.price_label = QtWidgets.QLabel(self.layoutWidget)
        self.price_label.setObjectName("price_label")
        self.gridLayout.addWidget(self.price_label, 4, 0, 1, 1)
        self.balance = QtWidgets.QLabel(self.layoutWidget)
        self.balance.setObjectName("balance")
        self.gridLayout.addWidget(self.balance, 9, 1, 1, 1)
        self.comment = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.comment.setObjectName("comment")
        self.gridLayout.addWidget(self.comment, 8, 1, 1, 3)
        self.group_label = QtWidgets.QLabel(self.layoutWidget)
        self.group_label.setObjectName("group_label")
        self.gridLayout.addWidget(self.group_label, 5, 2, 1, 1)
        self.date = QtWidgets.QLineEdit(self.layoutWidget)
        self.date.setReadOnly(True)
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 0, 1, 1, 1)
        self.direction = QtWidgets.QComboBox(self.layoutWidget)
        self.direction.setObjectName("direction")
        self.gridLayout.addWidget(self.direction, 5, 1, 1, 1)
        self.student_label = QtWidgets.QLabel(self.layoutWidget)
        self.student_label.setObjectName("student_label")
        self.gridLayout.addWidget(self.student_label, 6, 0, 1, 1)
        self.balance_label = QtWidgets.QLabel(self.layoutWidget)
        self.balance_label.setObjectName("balance_label")
        self.gridLayout.addWidget(self.balance_label, 9, 0, 1, 1)
        self.date_label = QtWidgets.QLabel(self.layoutWidget)
        self.date_label.setObjectName("date_label")
        self.gridLayout.addWidget(self.date_label, 0, 0, 1, 1)
        self.price = QtWidgets.QLineEdit(self.layoutWidget)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 4, 1, 1, 1)
        self.id_label = QtWidgets.QLabel(self.layoutWidget)
        self.id_label.setObjectName("id_label")
        self.gridLayout.addWidget(self.id_label, 0, 2, 1, 1)
        self.plastik = QtWidgets.QRadioButton(self.layoutWidget)
        self.plastik.setObjectName("plastik")
        self.gridLayout.addWidget(self.plastik, 2, 1, 1, 1)
        self.hisob_raqam = QtWidgets.QRadioButton(self.layoutWidget)
        self.hisob_raqam.setObjectName("hisob_raqam")
        self.gridLayout.addWidget(self.hisob_raqam, 3, 1, 1, 1)
        self.id = QtWidgets.QLineEdit(self.layoutWidget)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 0, 3, 1, 1)
        self.student = QtWidgets.QComboBox(self.layoutWidget)
        self.student.setObjectName("student")
        self.gridLayout.addWidget(self.student, 6, 1, 1, 3)
        self.teacher = QtWidgets.QLineEdit(self.layoutWidget)
        self.teacher.setObjectName("teacher")
        self.gridLayout.addWidget(self.teacher, 7, 1, 1, 3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.payment_table = QtWidgets.QTableWidget(self.layoutWidget)
        self.payment_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.payment_table.setObjectName("payment_table")
        self.payment_table.setColumnCount(5)
        self.payment_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.payment_table, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.total_price_label = QtWidgets.QLabel(self.layoutWidget)
        self.total_price_label.setObjectName("total_price_label")
        self.gridLayout_3.addWidget(self.total_price_label, 0, 0, 1, 1)
        self.total_price = QtWidgets.QLabel(self.layoutWidget)
        self.total_price.setText("")
        self.total_price.setObjectName("total_price")
        self.gridLayout_3.addWidget(self.total_price, 0, 1, 1, 1)
        self.gridLayout_3.setColumnMinimumWidth(1, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 5)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(Payment)
        self.layoutWidget1.setEnabled(True)
        self.layoutWidget1.setGeometry(QtCore.QRect(760, 550, 231, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.print_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.print_btn.setEnabled(True)
        self.print_btn.setAutoFillBackground(False)
        self.print_btn.setStyleSheet("background-color: rgb(64, 77, 191);\n"
"color: rgb(255, 255, 255);")
        self.print_btn.setObjectName("print_btn")
        self.horizontalLayout_2.addWidget(self.print_btn)
        self.save_bnt = QtWidgets.QPushButton(self.layoutWidget1)
        self.save_bnt.setEnabled(True)
        self.save_bnt.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.save_bnt.setIconSize(QtCore.QSize(16, 16))
        self.save_bnt.setObjectName("save_bnt")
        self.horizontalLayout_2.addWidget(self.save_bnt)

        self.retranslateUi(Payment)
        QtCore.QMetaObject.connectSlotsByName(Payment)

    def retranslateUi(self, Payment):
        _translate = QtCore.QCoreApplication.translate
        Payment.setWindowTitle(_translate("Payment", "Payment"))
        self.type_label.setText(_translate("Payment", "To\'lov turi:"))
        self.comment_label.setText(_translate("Payment", "Izohlar:"))
        self.direction_label.setText(_translate("Payment", "Kurs:"))
        self.month_label.setText(_translate("Payment", "Oy:"))
        self.teacher_label.setText(_translate("Payment", "O\'qituvchi:"))
        self.naqd.setText(_translate("Payment", "Naqd"))
        self.price_label.setText(_translate("Payment", "Summa:"))
        self.balance.setText(_translate("Payment", "0"))
        self.group_label.setText(_translate("Payment", "Guruh:"))
        self.student_label.setText(_translate("Payment", "O\'quvchi:"))
        self.balance_label.setText(_translate("Payment", "Balans:"))
        self.date_label.setText(_translate("Payment", "Sana:"))
        self.id_label.setText(_translate("Payment", "№"))
        self.plastik.setText(_translate("Payment", "Plastik"))
        self.hisob_raqam.setText(_translate("Payment", "Hisob raqam"))
        item = self.payment_table.horizontalHeaderItem(0)
        item.setText(_translate("Payment", "№"))
        item = self.payment_table.horizontalHeaderItem(1)
        item.setText(_translate("Payment", "Kurs"))
        item = self.payment_table.horizontalHeaderItem(2)
        item.setText(_translate("Payment", "Guruh"))
        item = self.payment_table.horizontalHeaderItem(3)
        item.setText(_translate("Payment", "Oy"))
        item = self.payment_table.horizontalHeaderItem(4)
        item.setText(_translate("Payment", "Qarz"))
        self.total_price_label.setText(_translate("Payment", "Umumiy balans:"))
        self.print_btn.setText(_translate("Payment", "Chop qilish"))
        self.save_bnt.setText(_translate("Payment", "Saqlash"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Payment = QtWidgets.QDialog()
    ui = Ui_Payment()
    ui.setupUi(Payment)
    Payment.show()
    sys.exit(app.exec_())
