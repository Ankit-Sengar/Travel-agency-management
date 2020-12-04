# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cpanel(object):
    def setupUi(self, cpanel):
        cpanel.setObjectName("cpanel")
        cpanel.resize(835, 510)
        cpanel.setMinimumSize(QtCore.QSize(835, 0))
        cpanel.setMaximumSize(QtCore.QSize(835, 16777215))
        self.cbgimage = QtWidgets.QLabel(cpanel)
        self.cbgimage.setGeometry(QtCore.QRect(0, 0, 831, 631))
        self.cbgimage.setMinimumSize(QtCore.QSize(831, 631))
        self.cbgimage.setMaximumSize(QtCore.QSize(831, 631))
        self.cbgimage.setText("")
        self.cbgimage.setPixmap(QtGui.QPixmap("Resources/blank.png"))
        self.cbgimage.setObjectName("cbgimage")
        self.ctoplabel = QtWidgets.QLabel(cpanel)
        self.ctoplabel.setGeometry(QtCore.QRect(320, 30, 181, 61))
        self.ctoplabel.setMinimumSize(QtCore.QSize(0, 61))
        self.ctoplabel.setMaximumSize(QtCore.QSize(16777215, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.ctoplabel.setFont(font)
        self.ctoplabel.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.ctoplabel.setObjectName("ctoplabel")
        self.label = QtWidgets.QLabel(cpanel)
        self.label.setGeometry(QtCore.QRect(580, 130, 191, 31))
        self.label.setMinimumSize(QtCore.QSize(0, 31))
        self.label.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label.setObjectName("label")
        self.clinecp = QtWidgets.QLineEdit(cpanel)
        self.clinecp.setGeometry(QtCore.QRect(610, 200, 181, 31))
        self.clinecp.setMinimumSize(QtCore.QSize(0, 31))
        self.clinecp.setMaximumSize(QtCore.QSize(16777215, 31))
        self.clinecp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clinecp.setObjectName("clinecp")
        self.clinenp = QtWidgets.QLineEdit(cpanel)
        self.clinenp.setGeometry(QtCore.QRect(610, 250, 181, 31))
        self.clinenp.setMinimumSize(QtCore.QSize(0, 31))
        self.clinenp.setMaximumSize(QtCore.QSize(16777215, 31))
        self.clinenp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clinenp.setObjectName("clinenp")
        self.clinecnp = QtWidgets.QLineEdit(cpanel)
        self.clinecnp.setGeometry(QtCore.QRect(610, 310, 181, 31))
        self.clinecnp.setMinimumSize(QtCore.QSize(0, 31))
        self.clinecnp.setMaximumSize(QtCore.QSize(16777215, 31))
        self.clinecnp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clinecnp.setObjectName("clinecnp")
        self.label_2 = QtWidgets.QLabel(cpanel)
        self.label_2.setGeometry(QtCore.QRect(480, 199, 121, 31))
        self.label_2.setMinimumSize(QtCore.QSize(0, 31))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(cpanel)
        self.label_3.setGeometry(QtCore.QRect(500, 250, 101, 31))
        self.label_3.setMinimumSize(QtCore.QSize(0, 31))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(cpanel)
        self.label_4.setGeometry(QtCore.QRect(470, 310, 131, 31))
        self.label_4.setMinimumSize(QtCore.QSize(0, 31))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label_4.setObjectName("label_4")
        self.ccpb = QtWidgets.QPushButton(cpanel)
        self.ccpb.setGeometry(QtCore.QRect(580, 380, 131, 41))
        self.ccpb.setMinimumSize(QtCore.QSize(0, 41))
        self.ccpb.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ccpb.setFont(font)
        self.ccpb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ccpb.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));\n"
"border: 3px solid red;")
        self.ccpb.setObjectName("ccpb")
        self.label_5 = QtWidgets.QLabel(cpanel)
        self.label_5.setGeometry(QtCore.QRect(110, 140, 101, 21))
        self.label_5.setMinimumSize(QtCore.QSize(0, 21))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label_5.setObjectName("label_5")
        self.csrb = QtWidgets.QPushButton(cpanel)
        self.csrb.setGeometry(QtCore.QRect(50, 220, 241, 41))
        self.csrb.setMinimumSize(QtCore.QSize(0, 41))
        self.csrb.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.csrb.setFont(font)
        self.csrb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.csrb.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));\n"
"border:3px solid red;")
        self.csrb.setObjectName("csrb")
        self.cp_action = QtWidgets.QLineEdit(cpanel)
        self.cp_action.setGeometry(QtCore.QRect(472, 430, 361, 22))
        self.cp_action.setReadOnly(True)
        self.cp_action.setObjectName("cp_action")

        self.ccpb.clicked.connect(self.pswd)
        self.csrb.clicked.connect(self.search)

        self.retranslateUi(cpanel)
        QtCore.QMetaObject.connectSlotsByName(cpanel)

    def retranslateUi(self, cpanel):
        _translate = QtCore.QCoreApplication.translate
        cpanel.setWindowTitle(_translate("cpanel", "Dialog"))
        self.ctoplabel.setText(_translate("cpanel", "cPanel"))
        self.label.setText(_translate("cpanel", "Reset Password"))
        self.label_2.setText(_translate("cpanel", "Current Password"))
        self.label_3.setText(_translate("cpanel", "New Password"))
        self.label_4.setText(_translate("cpanel", "Confirm Password"))
        self.ccpb.setText(_translate("cpanel", "Change"))
        self.label_5.setText(_translate("cpanel", "Records"))
        self.csrb.setText(_translate("cpanel", "Search and Delete"))

    def pswd(self,text):
        import json

        filename = 'Resources/DataFiles/credentials.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            curnt_pswd=data['password']
            old_pswd=self.clinecp.text()
            new_pswd=self.clinenp.text()
            cnfm_pswd=self.clinecnp.text()
            if(str(old_pswd)==curnt_pswd):
                if(new_pswd==cnfm_pswd):
                    data['password']=new_pswd
                    self.cp_action.setText('Password changed!!')
                else:
                    self.cp_action.setText('Re-enter pswd not match')    
            else:
                self.cp_action.setText('Previous pswd dont match')
        f.close()

        with open(filename, 'w') as f:
            json.dump(data,f)
        f.close()

    def search(self,text):
        from search_record import Ui_s_record
        s_record = QtWidgets.QDialog()
        ui = Ui_s_record()
        ui.setupUi(s_record)
        s_record.show()
        #print("effieh")
        ret=s_record.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cpanel = QtWidgets.QDialog()
    ui = Ui_cpanel()
    ui.setupUi(cpanel)
    cpanel.show()
    sys.exit(app.exec_())
