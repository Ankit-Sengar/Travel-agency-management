# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car_free.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_provide_detail(object):
    def setupUi(self, provide_detail):
        provide_detail.setObjectName("provide_detail")
        provide_detail.resize(613, 273)
        provide_detail.setMinimumSize(QtCore.QSize(613, 0))
        provide_detail.setMaximumSize(QtCore.QSize(613, 16777215))
        self.label = QtWidgets.QLabel(provide_detail)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 511))
        self.label.setMinimumSize(QtCore.QSize(611, 0))
        self.label.setMaximumSize(QtCore.QSize(611, 16777215))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Resources/give_info_car.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(provide_detail)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(provide_detail)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label_3.setObjectName("label_3")
        self.pd_edit = QtWidgets.QLineEdit(provide_detail)
        self.pd_edit.setGeometry(QtCore.QRect(160, 90, 113, 31))
        self.pd_edit.setObjectName("pd_edit")
        self.label_4 = QtWidgets.QLabel(provide_detail)
        self.label_4.setGeometry(QtCore.QRect(60, 140, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label_4.setObjectName("label_4")
        self.pd_button = QtWidgets.QPushButton(provide_detail)
        self.pd_button.setGeometry(QtCore.QRect(300, 90, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pd_button.setFont(font)
        self.pd_button.setStyleSheet("border:3px solid red;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));\n"
"")
        self.pd_button.setObjectName("pd_button")

        self.pd_button.clicked.connect(self.popup_action)

        self.retranslateUi(provide_detail)
        QtCore.QMetaObject.connectSlotsByName(provide_detail)

    def retranslateUi(self, provide_detail):
        _translate = QtCore.QCoreApplication.translate
        provide_detail.setWindowTitle(_translate("provide_detail", "Dialog"))
        self.label_2.setText(_translate("provide_detail", "Provide Detail"))
        self.label_3.setText(_translate("provide_detail", "Car No:"))
        self.label_4.setText(_translate("provide_detail", "*Enter the no. of car that is free"))
        self.pd_button.setText(_translate("provide_detail", "OK"))


    def popup_action(self,text):
        import json

        cons_car=self.pd_edit.text()

        filename = 'Resources/DataFiles/car.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            data[cons_car] = " "
        f.close()

        with open(filename, 'w') as f:
            json.dump(data,f)
        f.close()

        self.pd_edit.setText("")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    provide_detail = QtWidgets.QDialog()
    ui = Ui_provide_detail()
    ui.setupUi(provide_detail)
    provide_detail.show()
    sys.exit(app.exec_())
