from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon, QIcon, QFont
from PyQt5.QtCore import QSize
from datetime import datetime
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtWidgets

import random
import sqlite3



conn = sqlite3.connect('GPA_database.db')
database = conn.cursor()
database.execute('''
          CREATE TABLE IF NOT EXISTS user
          ([username] TEXT PRIMARY KEY, [password] TEXT
           [pass_list] TEXT)
          ''')
conn.commit()

mainlist = [["RAJ"],]
l1 = []
l2 = []
imgline = []
imgurl = []
time_dict = {}


def imgselector():
    for x in range(0,9):
        imagenum = random.randint(1,6700)
        file = open('C:\GPA_images\CombinedImages_1.txt','r')

        if imagenum not in imgline:
            imgline.append(imagenum)
            #URL is image source
            url = file.readlines()
            imgsrc = url[imagenum]
            imglen = len(imgsrc)
            image = ''
            image = image + imgsrc[0:int(imglen-1)] + ','
            imgurl.append(imgsrc[0:int(imglen-1)])

        print(image)

print(time_dict)

imgselector()
print(imgline)



def signup(username):
    database.execute("SELECT USERNAME FROM user")
    data = database.fetchall()
    for x in data:
        if username==x:
            nameLabel = QLabel()
            nameLabel.setText('User Already Exist.')
@pyqtSlot()

def login(username):
    print(username)
    database.execute("SELECT username FROM user")
    conn.commit()
    data = database.fetchall()
    print(data)
    y=0
    for x in data:
        if username==x:
            y=1
    if y==0:
        nameLabel = QLabel()
        nameLabel.setText('User Already Exist.')



class Window(QDialog):
    def __init__(self):


        # window title, icon and geometry

        self.login_window()

    def clearLayout(layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def login_window(self):
        super().__init__()
        self.setGeometry(300, 300, 50, 600)
        self.setWindowTitle("GPA")
        self.setWindowIcon(QIcon('C:\RAJ\gpa.jpeg'))
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Username:')
        self.input_box = QLineEdit(self)

        self.input_box.move(150, 300)
        self.input_box.resize(200, 32)

        self.nameLabel.move(20, 300)
        #self.create_checkbox()
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Username:')



        self.input_box.resize(200, 32)
        self.nameLabel.move(20, 300)
        self.text1 = self.input_box.text()

        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + self.text1, QMessageBox.Ok,QMessageBox.Ok)
        self.textbox.setText("")
        # ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
        # print(ok)
        print(self.text1)
        self.login_button = QPushButton('LOGIN', self)
        self.login_button.move(50, 450)
        self.login_button.clicked.connect(lambda: login(self.text1))

        self.signup_button = QPushButton('SIGN UP', self)
        self.signup_button.move(150, 450)
        self.signup_button.clicked.connect(lambda: self.clearLayout())

    def signup_window(self):
        self.login_button.clear()
        super().__init__()
        self.setGeometry(300, 300, 50, 600)
        self.setWindowTitle("GPA")
        self.setWindowIcon(QIcon('C:\RAJ\gpa.jpeg'))
        self.login_window()

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Username:')
        line = QLineEdit()
        self.line.move(150, 300)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 300)
        self.text1 = self.line.text()
        # ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
        # print(ok)
        ok = line.text()
        print(ok)
        self.login_button = QPushButton('LOGIN', self)
        self.login_button.move(50, 450)
        self.login_button.clicked.connect(lambda: login(ok))

        self.signup_button = QPushButton('SIGN UP', self)
        self.signup_button.move(50, 450)
        #self.signup_button.clicked.connect(signup_window())

    def create_checkbox(self):

        # this is our hboxlayout
        hbox = QHBoxLayout()

        # these are checkboxes
        self.check0 = QCheckBox()
        self.check0.setIcon(QIcon(imgurl[0]))
        self.check0.setIconSize(QSize(170, 170))
        self.check0.setGeometry(29000, 200, 8199, 2419)
        self.check0.toggled.connect(self.item_selected0)
        hbox.addWidget(self.check0)

        self.check1 = QCheckBox()
        self.check1.setIcon(QIcon(imgurl[1]))
        self.check1.setIconSize(QSize(170, 170))
        self.check1.move(150, 10)
        self.check1.toggled.connect(self.item_selected1)
        hbox.addWidget(self.check1)

        self.check2 = QCheckBox()
        self.check2.setIcon(QIcon(imgurl[2]))
        self.check2.setIconSize(QSize(170, 170))
        self.check2.move(2500, 10)
        self.check2.toggled.connect(self.item_selected2)
        hbox.addWidget(self.check2)

        self.check3 = QCheckBox()
        self.check3.setIcon(QIcon(imgurl[3]))
        self.check3.setIconSize(QSize(170, 170))
        self.check3.move(1500, 1000)
        self.check3.toggled.connect(self.item_selected3)
        hbox.addWidget(self.check3)

        self.check4 = QCheckBox()
        self.check4.setIcon(QIcon(imgurl[4]))
        self.check4.setIconSize(QSize(170, 170))
        self.check4.toggled.connect(self.item_selected4)
        hbox.addWidget(self.check4)

        self.check5 = QCheckBox()
        self.check5.setIcon(QIcon(imgurl[5]))
        self.check5.setIconSize(QSize(170, 170))
        self.check5.toggled.connect(self.item_selected5)
        hbox.addWidget(self.check5)

        self.check6 = QCheckBox()
        self.check6.setIcon(QIcon(imgurl[6]))
        self.check6.setIconSize(QSize(170, 170))
        self.check6.toggled.connect(self.item_selected6)
        hbox.addWidget(self.check6)

        self.check7 = QCheckBox()
        self.check7.setIcon(QIcon(imgurl[7]))
        self.check7.setIconSize(QSize(170, 170))
        self.check7.toggled.connect(self.item_selected7)
        hbox.addWidget(self.check7)

        self.check8 = QCheckBox()
        self.check8.setIcon(QIcon(imgurl[8]))
        self.check8.setIconSize(QSize(170, 170))
        self.check8.toggled.connect(self.item_selected8)
        hbox.addWidget(self.check8)

        # this is the vboxlayout
        vbox = QVBoxLayout()

        # we have created a label in here
        self.label = QLabel("GRAPHICAL PASSWORD AUTHENTICATOR")
        self.label.setFont(QFont("Sanserif", 30))

        # add the label in the vbox layout
        vbox.addWidget(self.label)

        # add the hbox layout in the vbox layout
        vbox.addLayout(hbox)

        # set the layout for the main window
        self.setLayout(vbox)

    def item_selected0(self):
        value = ""
        l1=[]

        # check for the check box value
        if self.check0.isChecked():
            value = self.check0.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)

            temp_dict = {0: current_time}
            time_dict.update(temp_dict)
            l1.append(0)
            l1.append(current_time)
            l2.append(l1)
            l1=[]
        print(time_dict)
        print(l2)

    def item_selected1(self):
        l1 = []

        if self.check1.isChecked():
            value = self.check1.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)
            temp_dict = {1: current_time}
            time_dict.update(temp_dict)
            l1.append(1)
            l1.append(current_time)
            l2.append(l1)
            l1 = []
        print(time_dict)
        print(l2)

    def item_selected2(self):
        value = ""
        l1 = []
        if self.check2.isChecked():
            value = self.check2.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)
            temp_dict = {2: current_time}
            time_dict.update(temp_dict)
            l1.append(2)
            l1.append(current_time)
            l2.append(l1)
            l1 = []
        print(time_dict)
        print(l2)

    def item_selected3(self):
        l1 = []
        value = ""
        if self.check3.isChecked():
            value = self.check3.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)
            temp_dict = {3: current_time}
            time_dict.update(temp_dict)
            l1.append(3)
            l1.append(current_time)
            l2.append(l1)
            l1 = []
        print(time_dict)
        print(l2)


    def item_selected4(self):
        l1 = []
        value = ""
        if self.check4.isChecked():
            value = self.check4.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)
            temp_dict = {4: current_time}
            time_dict.update(temp_dict)
            l1.append(4)
            l1.append(current_time)
            l2.append(l1)
            l1 = []
        print(time_dict)
        print(l2)

    def item_selected5(self):
        l1 = []
        value = ""
        if self.check5.isChecked():
            value = self.check5.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)
            temp_dict = {5: current_time}
            time_dict.update(temp_dict)
            l1.append(5)
            l1.append(current_time)
            l2.append(l1)
            l1 = []
        print(time_dict)
        print(l2)


    def item_selected6(self):
        l1 = []
        value = ""
        if self.check6.isChecked():
            value = self.check6.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)
            temp_dict = {6: current_time}
            time_dict.update(temp_dict)
            l1.append(6)
            l1.append(current_time)
            l2.append(l1)
            l1 = []
        print(time_dict)
        print(l2)

    def item_selected7(self):
        l1 = []
        value = ""
        if self.check7.isChecked():
            value = self.check7.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)
            temp_dict = {7: current_time}
            time_dict.update(temp_dict)
            l1.append(7)
            l1.append(current_time)
            l2.append(l1)
            l2.append(l1)
            l1 = []
        print(time_dict)
        print(l2)

    def item_selected8(self):
        l1 = []
        value = ""
        if self.check8.isChecked():
            value = self.check8.text()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.label.setText(current_time)
            temp_dict = {8: current_time}
            time_dict.update(temp_dict)
            l1.append(8)
            l1.append(current_time)
            l2.append(l1)
            l1 = []
        '''l1.append(current_time)
        l2.append(l1)'''
        print(time_dict)
        print(l2)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
print(time_dict)

