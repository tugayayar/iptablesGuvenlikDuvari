import self as self
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from functools import partial
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog, QMessageBox, QPushButton,
QLineEdit, QInputDialog)

from arayuz_fw import Ui_Form

import os, subprocess

from subprocess import Popen, PIPE
class FireWall(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem(self.Yazdir())
        #self.ui.lineEdit.setText("iitb.ac.in")
        self.ui.pushButton.clicked.connect(self.IpEngelle)
        self.ui.pushButton_2.clicked.connect(self.IpEngellemesiniKaldir)
        self.ui.pushButton_4.clicked.connect(self.Sifirla)
        self.ui.pushButton_5.clicked.connect(self.Yazdir)
        self.ui.checkBox.stateChanged.connect(self.CheckBoxUygula)
        self.ui.checkBox_2.stateChanged.connect(self.CheckBoxUygula2)
        self.ui.pushButton_3.clicked.connect(self.AyarlariKaydet)

    # sudo /sbin/iptables-save  =>  Tüm ayarları kaydeder
    def AyarlariKaydet(self):
        self.KomutGir2("sudo /sbin/iptables-save")
        if (self.KomutSatiriHatasi != ''):
            self.ui.listWidget.clear()
            self.ui.listWidget.addItem("Ayarlarınız Başarılı Bir Şekilde Kaydedildi.")
            self.ui.listWidget.addItem("")
            arr = self.KomutSatiriHatasi.split('\n')
            for i in arr:
                self.ui.listWidget.addItem(i)
            #self.ui.listWidget.addItem(self.KomutSatiriHatasi)
            self.KomutSatiriHatasi = ''


    #Tüm Localhost'a İzin Veren Fonksiyon
    def CheckBoxUygula(self, state):
        if state == QtCore.Qt.Checked:
            self.KomutGir2("sudo iptables -A INPUT -i lo -j ACCEPT")
            if (self.KomutSatiriHatasi != ''):
                self.ui.listWidget.clear()
                self.ui.listWidget.addItem(self.KomutSatiriHatasi)
                self.KomutSatiriHatasi = ''
            else:
                self.Yazdir()

    #Bu komut listede belirtilen portlar dışındaki tüm trafiği reddeder.
    def CheckBoxUygula2(self, state):
        if state == QtCore.Qt.Checked:
            self.KomutGir2("sudo iptables -A INPUT -j DROP")
            if (self.KomutSatiriHatasi != ''):
                self.ui.listWidget.clear()
                self.ui.listWidget.addItem(self.KomutSatiriHatasi)
                self.KomutSatiriHatasi = ''
            else:
                self.Yazdir()

    def Yazdir(self):
        """import pexpect
        cikti = pexpect.spawn('sudo iptables -L --line-numbers -n -v')      #subprocess.getstatusoutput(f'sudo iptables -L --line-numbers -n -v')
        cikti.expect('[sudo]')
        cikti.sendline("abc123456")
        StrCikti=["asdasd"]
        print(type(cikti.read()))
        print(cikti.read())
        StrCikti = str(cikti.read(), 'utf-8')
        print(StrCikti)
        #StrCikti = str(cikti[1])
        StrSatir = StrCikti.split("\n")
        print(StrSatir)
        self.ui.listWidget.clear()
        for i in StrSatir:
            self.ui.listWidget.addItem(i)
        """
        cikti = subprocess.getstatusoutput(f'sudo iptables -L --line-numbers -n -v')
        StrCikti = str(cikti[1])
        StrSatir = StrCikti.split("\n")
        self.ui.listWidget.clear()
        for i in StrSatir:
            self.ui.listWidget.addItem(i)


    def Komutgir(self, cmd):
        os.system(cmd)

    KomutSatiriHatasi = ""
    def KomutGir2(self, cmd):
        KonsolCiktisi = subprocess.getstatusoutput(cmd)
        if(KonsolCiktisi[1] != ''):
            self.KomutSatiriHatasi = KonsolCiktisi[1]

    def KomutGir3(self, cmd, pw):
        import pexpect

        child = pexpect.spawn(cmd)
        child.expect('[sudo]')
        child.sendline(pw)
        print(child.read())
        return child

    def IpEngelle(self):
        if(len(self.ui.lineEdit.text()) >= 19):
            #sudo iptables -A INPUT -m iprange --src-range 192.168.1.100-192.168.1.200 -j DROP
            kmt = "sudo iptables -A " + self.ui.comboBox.currentText() + " -m iprange --src-range " + self.ui.lineEdit.text() + " -j " + self.ui.comboBox_2.currentText()
            self.KomutGir2(kmt)
        elif(len(self.ui.lineEdit_2.text()) > 0 and len(self.ui.lineEdit.text()) == 0):
            """HTTP, SSH ve SSL portuna bağlantılara izin vermek
            Olağan HTTP (port 80), https (port 443) ve ssh (port 22) bağlantılarının aynen normalde olduğu gibi çalışmaya 
            devam etmesini isteriz. Bu portlara izin vermek için aşağıdaki komutları çalıştırın. Aşağıdaki komutlarda 
            protokolü -p seçeneği ile ve her protokolün ilgili olduğu portu -dport (destination port – hedef port) ile gösterdik.
            sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
            Şimdi belirlenen port numaralarından gelen tüm protokol bağlantıları kabul edilecek."""
            kmt1 = "sudo iptables -A " + self.ui.comboBox.currentText() + " -p " + (self.ui.comboBox_3.currentText()).lower() + " --dport " + self.ui.lineEdit_2.text() + " -j " + self.ui.comboBox_2.currentText()
            self.KomutGir2(kmt1)
        elif(len(self.ui.lineEdit.text()) > 0 and len(self.ui.lineEdit_2.text()) > 0):
            #sudo iptables -A INPUT -s IP-ADDRESS -p tcp --destination-port port_number -j DROP
            kmt2 = "sudo iptables -A " + self.ui.comboBox.currentText() + " -s " + self.ui.lineEdit.text() + " -p " + (self.ui.comboBox_3.currentText()).lower() + " --destination-port " + self.ui.lineEdit_2.text() + " -j " + self.ui.comboBox_2.currentText()
            self.KomutGir2(kmt2)
        else:
            komut = "sudo iptables -A " + self.ui.comboBox.currentText() + " -s " + self.ui.lineEdit.text() + " -j " + self.ui.comboBox_2.currentText() #"sudo iptables -A INPUT -s %s -j DROP"%(self.ui.lineEdit.text())
            self.KomutGir2(komut)  # self.Komutgir(komut)
        if (self.KomutSatiriHatasi != ''):
            self.ui.listWidget.clear()
            self.ui.listWidget.addItem(self.KomutSatiriHatasi)
            self.KomutSatiriHatasi = ''
        else:
            self.Yazdir()


    def TDiyalogKutusu(self):
        qWidget = QWidget()
        text, ok = QInputDialog.getText(qWidget, 'IP Düzenle', 'Silmek istediğiniz ip adresinin listedeki sıra numarasını giriniz?')
        if ok:
            return str(text) # self.ui.lineEdit_2.setText(str(text))

    def CDiyalogKutusu(self):
        qWidget = QWidget()
        elemanlar=("INPUT", "FORWARD", "OUTPUT")
        ok = QInputDialog.getItem(qWidget, "IP Düzenle", "Hangi CHAIN Düzenlenecek", elemanlar, 0)
        if ok:
            return str(ok[0])

    def IpEngellemesiniKaldir(self):
        komut = "sudo iptables -D " + str(self.CDiyalogKutusu()) + " " + str(self.TDiyalogKutusu()) # sudo iptables -D INPUT " + str(self.TDiyalogKutusu())
        self.KomutGir2(komut)  # self.Komutgir(komut)
        if(self.KomutSatiriHatasi != ''):
            self.ui.listWidget.clear()
            self.ui.listWidget.addItem(self.KomutSatiriHatasi)
            self.KomutSatiriHatasi = ''
        else:
            self.Yazdir()

    AyarlariSifirla = ["sudo iptables -P INPUT ACCEPT",
                       "sudo iptables -P FORWARD ACCEPT",
                       "sudo iptables -P OUTPUT ACCEPT",
                       "sudo iptables -t nat -P PREROUTING ACCEPT",
                       "sudo iptables -t nat -P POSTROUTING ACCEPT",
                       "sudo iptables -t nat -P OUTPUT ACCEPT",
                       "sudo iptables -t mangle -P PREROUTING ACCEPT",
                       "sudo iptables -t mangle -P OUTPUT ACCEPT",
                       "sudo iptables -F",
                       "sudo iptables -X",
                       "sudo iptables -t nat -F",
                       "sudo iptables -t nat -X",
                       "sudo iptables -t mangle -F",
                       "sudo iptables -t mangle -X"]

    def Sifirla(self):
        hata = False
        for sayac in self.AyarlariSifirla:
            self.KomutGir2(sayac) # self.Komutgir(sayac)
            if (self.KomutSatiriHatasi != ''):
                self.ui.listWidget.clear()
                self.ui.listWidget.addItem(self.KomutSatiriHatasi)
                self.KomutSatiriHatasi = ''
                hata = True
                break
        if(hata == False):
            self.Yazdir()
        else:
            hata = False


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    c = FireWall()
    c.show()
    sys.exit(app.exec_())


