# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz_fw.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(680, 433)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(680, 433))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 390, 111, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 390, 111, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 641, 121))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 31, 22))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(390, 70, 110, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 55, 22))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 70, 110, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 30, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(430, 30, 99, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(530, 30, 99, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 30, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 390, 111, 22))
        self.pushButton_5.setObjectName("pushButton_5")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 140, 641, 241))
        self.listWidget.setObjectName("listWidget")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(30, 70, 183, 15))
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 90, 300, 15))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "iptables Güvenlik Duvarı"))
        self.pushButton_3.setText(_translate("Form", "Ayarları Kaydet"))
        self.pushButton_4.setText(_translate("Form", "Ayarları Sıfırla"))
        self.groupBox.setTitle(_translate("Form", "IP İşlemleri"))
        self.label_2.setText(_translate("Form", "Port"))
        self.pushButton.setText(_translate("Form", "UYGULA"))
        self.label.setText(_translate("Form", "IP Adres"))
        self.pushButton_2.setText(_translate("Form", "DÜZENLE"))
        self.comboBox.setCurrentText(_translate("Form", "INPUT"))
        self.comboBox.setItemText(0, _translate("Form", "INPUT"))
        self.comboBox.setItemText(1, _translate("Form", "FORWARD"))
        self.comboBox.setItemText(2, _translate("Form", "OUTPUT"))
        self.comboBox_2.setItemText(0, _translate("Form", "DROP"))
        self.comboBox_2.setItemText(1, _translate("Form", "ACCEPT"))
        self.comboBox_2.setItemText(2, _translate("Form", "REJECT"))
        self.comboBox_3.setItemText(0, _translate("Form", "TCP"))
        self.comboBox_3.setItemText(1, _translate("Form", "UDP"))
        self.pushButton_5.setText(_translate("Form", "iptables listesi"))
        self.checkBox.setText("Tüm Localhost'a İzin Ver")
        self.checkBox_2.setText("Ayarlarım Haricindeki Tüm Trafiği Engelle")
