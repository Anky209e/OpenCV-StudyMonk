# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nmap_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebKitWidgets
import nmap
scanner = nmap.PortScanner()
import logging
import sys

logging.basicConfig(filename="main.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 694)
        MainWindow.setStyleSheet("background-color:rgb(40, 40, 40);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 10, 541, 31))
        self.textEdit.setStyleSheet("background-color:rgb(74, 74, 74);\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.info_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.info_box.setGeometry(QtCore.QRect(10, 290, 781, 371))
        self.info_box.setStyleSheet("background-color:rgb(70, 70, 70);")
        self.info_box.setObjectName("info_box")
        self.start_scan = QtWidgets.QPushButton(self.centralwidget)
        self.start_scan.setGeometry(QtCore.QRect(630, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_scan.setFont(font)
        self.start_scan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_scan.setMouseTracking(False)
        self.start_scan.setAcceptDrops(False)
        self.start_scan.setToolTipDuration(2)
        self.start_scan.setAutoFillBackground(False)
        self.start_scan.setStyleSheet("background-color:rgb(134, 188, 255);\n"
"border-radius:20px;\n"
"hover: { color: rgb(42, 42, 42) };")
        icon = QtGui.QIcon.fromTheme("start")
        self.start_scan.setIcon(icon)
        self.start_scan.setFlat(False)
        self.start_scan.setObjectName("start_scan")
        self.start_scan.clicked.connect(self.scan)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 260, 61, 22))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 741, 31))
        self.groupBox.setObjectName("groupBox")
        self.ping = QtWidgets.QRadioButton(self.groupBox)
        self.ping.setGeometry(QtCore.QRect(200, 0, 111, 26))
        self.ping.setObjectName("ping")
        self.os_detection = QtWidgets.QRadioButton(self.groupBox)
        self.os_detection.setGeometry(QtCore.QRect(420, 0, 121, 26))
        self.os_detection.setObjectName("os_detection")
        self.regular = QtWidgets.QRadioButton(self.groupBox)
        self.regular.setGeometry(QtCore.QRect(630, 0, 111, 26))
        self.regular.setObjectName("regular")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 160, 141, 71))
        self.pushButton.setStyleSheet("background-color:rgb(255, 12, 12);\n"
"border-radius:20px;\n"
"hover: { color: rgb(42, 42, 42) };")
        icon = QtGui.QIcon.fromTheme("exit")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.exit)
        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(10, 90, 311, 191))
        self.webView.setUrl(QtCore.QUrl("https://cloud7.news/wp-content/uploads/2022/04/Nmap-open-source-network-mapping-tool.jpg"))
        self.webView.setObjectName("webView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nmap Scanner"))
        self.textEdit.setStatusTip(_translate("MainWindow", "Input Ip or Web address"))
        self.textEdit.setWhatsThis(_translate("MainWindow", "Input Address"))
        self.info_box.setStatusTip(_translate("MainWindow", "Information Bar"))
        self.info_box.setWhatsThis(_translate("MainWindow", "It will show you all scan information."))
        self.info_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1)Enter Ip address or web address</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) Select a Scan Type</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3) Press Start</p></body></html>"))
        self.start_scan.setToolTip(_translate("MainWindow", "Start to Scan "))
        self.start_scan.setStatusTip(_translate("MainWindow", "Start Button"))
        self.start_scan.setWhatsThis(_translate("MainWindow", "Press this to start a scan"))
        self.start_scan.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Web address or Ip address:"))
        self.label_2.setText(_translate("MainWindow", "All info"))
        self.groupBox.setTitle(_translate("MainWindow", "Scan Type:"))
        self.ping.setStatusTip(_translate("MainWindow", "Basic Ping Scan Only checks if host is Up"))
        self.ping.setText(_translate("MainWindow", "Ping Scan"))
        self.os_detection.setStatusTip(_translate("MainWindow", "Os Detection Scan (Requires admin )"))
        self.os_detection.setText(_translate("MainWindow", "OS Detection"))
        self.regular.setStatusTip(_translate("MainWindow", "Checks all open ports"))
        self.regular.setText(_translate("MainWindow", "Regular"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Forcefully Exits process"))
        self.pushButton.setText(_translate("MainWindow", "Force Exit"))
    def scan(self):
        ip = self.textEdit.toPlainText()
        if not ip:
            ip = "127.0.0.1"
        print(ip)
        if self.ping.isChecked():
            scanner.scan(hosts=ip+"/24", arguments='-n -sP -PE -PA21,23,80,3389')
            hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
            for host , status in hosts_list:
                logger.info(f'Host:{host}>Status:{status}')

            with open('main.log','r') as f:
                data = f.read()
            self.info_box.setText(data)
        
        elif self.regular.isChecked():
            scanner.scan(ip)
            print(scanner.scaninfo())
            print("Ip Status: ", scanner[ip].state())
            print(scanner[ip].all_protocols())
            port_info = scanner[ip]['tcp'].keys()
            logger.info(f'Ip Status: { scanner[ip].state()} > Open Ports:{port_info} ')

            with open('main.log','r') as f:
                data = f.read()
            self.info_box.setText(data)
        elif self.os_detection.isChecked():
            print(scanner.scan(ip, arguments="-O")['scan'][ip]['osmatch'])
            logger.info(scanner.scan(ip, arguments="-O")['scan'][ip]['osmatch'])
            with open('main.log','r') as f:
                data = f.read()
            self.info_box.setText(data)
        else:
            self.info_box.setText("Please Choose a Scan Type")


    def exit(self):
        print("exiting...")
        sys.exit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
