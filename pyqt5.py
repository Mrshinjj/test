# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:18:02 2023

@author: User
"""
pip install pyinstaller==4.3 dsdev-utils==1.0.5 PyUpdater==4.0 PyUpdater-S3-plugin==4.1.2

from pyupdater.client import Client
from os_client_config import config


APP_NAME = 'PyUpdater App'
APP_VERSION = '1.0.0'

def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print(downloaded, total, status)

client = Client(config(), refresh=True, progress_hooks=[print_status_info])
client.FROZEN = True
client.strategy = 'rename'



import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setAcceptDrops(True)
    
    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()
        btn1.clicked.connect(self.read)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)


        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
 
    def dropEvent(self, event):
        
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            data=f
            print(data)
        self.data = data
        

    def read(self):
        with open(self.data,"r") as a:
            strings = a.read()
            print(strings)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
    