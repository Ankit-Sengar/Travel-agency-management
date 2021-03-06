# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(953, 853)
        Menu.setMinimumSize(QtCore.QSize(953, 853))
        Menu.setMaximumSize(QtCore.QSize(953, 16777215))
        self.menu_bg = QtWidgets.QLabel(Menu)
        self.menu_bg.setGeometry(QtCore.QRect(0, -10, 1201, 871))
        self.menu_bg.setMinimumSize(QtCore.QSize(1201, 871))
        self.menu_bg.setText("")
        self.menu_bg.setPixmap(QtGui.QPixmap("Resources/assistent_menu.png"))
        self.menu_bg.setObjectName("menu_bg")
        self.menu_head = QtWidgets.QLabel(Menu)
        self.menu_head.setGeometry(QtCore.QRect(110, 100, 311, 111))
        self.menu_head.setMinimumSize(QtCore.QSize(311, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(72)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.menu_head.setFont(font)
        self.menu_head.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.menu_head.setObjectName("menu_head")
        self.menu_itm1 = QtWidgets.QPushButton(Menu)
        self.menu_itm1.setGeometry(QtCore.QRect(42, 350, 161, 111))
        self.menu_itm1.setMinimumSize(QtCore.QSize(161, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.menu_itm1.setFont(font)
        self.menu_itm1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_itm1.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));\n"
"border: 3px solid red;")
        self.menu_itm1.setObjectName("menu_itm1")
        self.menu_itm2 = QtWidgets.QPushButton(Menu)
        self.menu_itm2.setGeometry(QtCore.QRect(230, 350, 161, 111))
        self.menu_itm2.setMinimumSize(QtCore.QSize(161, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.menu_itm2.setFont(font)
        self.menu_itm2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_itm2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));\n"
"border: 3px solid red;")
        self.menu_itm2.setObjectName("menu_itm2")
        self.menu_itm3 = QtWidgets.QPushButton(Menu)
        self.menu_itm3.setGeometry(QtCore.QRect(40, 500, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.menu_itm3.setFont(font)
        self.menu_itm3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_itm3.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));\n"
"border: 3px solid red;")
        self.menu_itm3.setObjectName("menu_itm3")
        self.pushButton = QtWidgets.QPushButton(Menu)
        self.pushButton.setGeometry(QtCore.QRect(230, 500, 161, 111))
        self.pushButton.setMinimumSize(QtCore.QSize(161, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));\n"
"border: 3px solid red;")
        self.pushButton.setObjectName("pushButton")
        self.menu_botm1 = QtWidgets.QLabel(Menu)
        self.menu_botm1.setGeometry(QtCore.QRect(20, 700, 181, 51))
        self.menu_botm1.setMinimumSize(QtCore.QSize(181, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.menu_botm1.setFont(font)
        self.menu_botm1.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.menu_botm1.setObjectName("menu_botm1")
        self.menu_botm2 = QtWidgets.QLabel(Menu)
        self.menu_botm2.setGeometry(QtCore.QRect(20, 750, 231, 31))
        self.menu_botm2.setMinimumSize(QtCore.QSize(231, 31))
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        font.setPointSize(14)
        self.menu_botm2.setFont(font)
        self.menu_botm2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.menu_botm2.setObjectName("menu_botm2")

        self.menu_itm1.clicked.connect(self.cpanel_func)
        self.menu_itm2.clicked.connect(self.booking_panel_func)
        self.menu_itm3.clicked.connect(self.billing_panel_func)
        self.pushButton.clicked.connect(self.car_service_func)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Dialog"))
        self.menu_head.setText(_translate("Menu", "Menu"))
        self.menu_itm1.setText(_translate("Menu", "cPanel"))
        self.menu_itm2.setText(_translate("Menu", "Booking"))
        self.menu_itm3.setText(_translate("Menu", "Billing"))
        self.pushButton.setText(_translate("Menu", "Car Care"))
        self.menu_botm1.setText(_translate("Menu", "SAMSTARF"))
        self.menu_botm2.setText(_translate("Menu", "Simplifying your work!!"))

    def cpanel_func(self,text):
        from cpanel import Ui_cpanel
        cpanel = QtWidgets.QDialog()
        ui = Ui_cpanel()
        ui.setupUi(cpanel)
        cpanel.show()
        #print("effieh")
        ret=cpanel.exec_()
        
    def booking_panel_func(self,text):
        from car_free import Ui_provide_detail
        provide_detail = QtWidgets.QDialog()
        ui = Ui_provide_detail()
        ui.setupUi(provide_detail)
        provide_detail.show()
        #print("effieh")
        ret=provide_detail.exec_()
    
        from booking_panel import Ui_booking 
        booking = QtWidgets.QDialog()
        ui = Ui_booking()
        ui.setupUi(booking)
        booking.show()
        #print("effieh")
        ret=booking.exec_()

    def billing_panel_func(self,text):
        from billing_panel import Ui_billing 
        billing = QtWidgets.QDialog()
        ui = Ui_billing()
        ui.setupUi(billing)
        billing.show()
        #print("effieh")
        ret=billing.exec_()

    def car_service_func(self,text):
        from service_alert import Ui_service_alert
        service_alert = QtWidgets.QDialog()
        ui = Ui_service_alert()
        ui.setupUi(service_alert)
        service_alert.show()
        #print("effieh")
        ret=service_alert.exec_()

        from service_info import Ui_service_dialog
        service_dialog = QtWidgets.QDialog()
        ui = Ui_service_dialog()
        ui.setupUi(service_dialog)
        service_dialog.show()
        #print("effieh")
        ret=service_dialog.exec_()     
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
