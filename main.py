from MainUi import *
from calres import *
from math import *
from PyQt5.QtCore import QThread,QPoint
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

from functools import lru_cache,cache
@cache
@lru_cache




class Window(QMainWindow,QThread):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.cal_exit.clicked.connect(self.close)
        self.ui.cal_minimize.clicked.connect(self.showMinimized)
        self.ui.butt_1.clicked.connect(self.num1)
        self.ui.butt_2.clicked.connect(self.num2)
        self.ui.Butt_3.clicked.connect(self.num3)
        self.ui.butt_4.clicked.connect(self.num4)
        self.ui.butt_5.clicked.connect(self.num5)
        self.ui.butt_6.clicked.connect(self.num6)
        self.ui.butt_7.clicked.connect(self.num7)
        self.ui.butt_8.clicked.connect(self.num8)
        self.ui.butt_9.clicked.connect(self.num9)
        self.ui.Butt_0.clicked.connect(self.num0)
        self.ui.butt_00.clicked.connect(self.num00)
        self.ui.butt_plus.clicked.connect(self.plus)
        self.ui.butt_minus.clicked.connect(self.minus)
        self.ui.butt_multiply.clicked.connect(self.multi)
        self.ui.butt_divide.clicked.connect(self.divide)
        self.ui.butt_equal.clicked.connect(self.complute)
        self.ui.butt_C.clicked.connect(self.clearall)
        self.ui.butt_clearlastnum.clicked.connect(self.clearlast)
        self.ui.butt_sin.clicked.connect(self.sine)
        self.ui.butt_cos.clicked.connect(self.cosine)
        self.ui.butt_tan.clicked.connect(self.tangent)
        self.ui.butt_openbrac.clicked.connect(self.openb)
        self.ui.butt_closebrac.clicked.connect(self.closeb)
        self.ui.Butt_dot.clicked.connect(self.dotpoint)
    def num1(self):
        a=self.ui.number_show_text.text()
        a=a+"1"
        self.ui.number_show_text.setText(f"{a}")
    def num2(self):
        a=self.ui.number_show_text.text()
        a=a+"2"
        self.ui.number_show_text.setText(f"{a}")
    def num3(self):
        a=self.ui.number_show_text.text()
        a=a+"3"
        self.ui.number_show_text.setText(f"{a}")
    def num4(self):
        a=self.ui.number_show_text.text()
        a=a+"4"
        self.ui.number_show_text.setText(f"{a}")
    def num5(self):
        a=self.ui.number_show_text.text()
        a=a+"5"
        self.ui.number_show_text.setText(f"{a}")
    def num6(self):
        a=self.ui.number_show_text.text()
        a=a+"6"
        self.ui.number_show_text.setText(f"{a}")
    def num7(self):
        a=self.ui.number_show_text.text()
        a=a+"7"
        self.ui.number_show_text.setText(f"{a}")
    def num8(self):
        a=self.ui.number_show_text.text()
        a=a+"8"
        self.ui.number_show_text.setText(f"{a}")
    def num9(self):
        a=self.ui.number_show_text.text()
        a=a+"9"
        self.ui.number_show_text.setText(f"{a}")
    def num0(self):
        a=self.ui.number_show_text.text()
        a=a+"0"
        self.ui.number_show_text.setText(f"{a}")
    def num00(self):
        a=self.ui.number_show_text.text()
        a=a+"00"
        self.ui.number_show_text.setText(f"{a}")
    def dotpoint(self):
        a=self.ui.number_show_text.text()
        a=a+"."
        self.ui.number_show_text.setText(f"{a}")
    def plus(self):
        a=self.ui.number_show_text.text()
        try:
            x=a[-1]
        except:
            x=""
        if ("+" in x) or (x=="") or ("-" in x) or ("*" in x) or ("/" in x):
            a=a+""
        else:
            a=a+"+"
            self.ui.number_show_text.setText(f"{a}")
    def minus(self):
        a=self.ui.number_show_text.text()
        try:
            y=a[-1]
        except:
            y=""
        if ("-" in y) or (y=="") or ("+" in y) or ("*" in y) or ("/" in y):
            a=a+""
        else:
            a=a+"-"
            self.ui.number_show_text.setText(f"{a}")
    def multi(self):
        a=self.ui.number_show_text.text()
        try:
            z=a[-1]
        except:
            z=""
        if ('*' in z) or (z=="") or ("+" in z) or ("-" in z) or ("/" in z):
            a=a+""
        else:
            a=a+"*"
            self.ui.number_show_text.setText(f"{a}")
    def divide(self):
        a=self.ui.number_show_text.text()
        try:
            i=a[-1]
        except:
            i=""
        if ("/" in i) or (i=="") or ("+" in i) or ("-" in i) or ("*" in i):
            a=a+""
        else:
            a=a+"/"
            self.ui.number_show_text.setText(f"{a}")
    def clearall(self):
        self.ui.number_show_text.setText("")
    def clearlast(self):
        a=self.ui.number_show_text.text()
        try:
            mo=a[-1]
        except:
            mo=""
        try:
            if("n" in mo) or ("s" in mo):
                b=a[:len(a)-3]
                self.ui.number_show_text.setText(f"{b}")
                self.ui.butt_00.setEnabled(True)
                self.ui.Butt_0.setEnabled(True)
                self.ui.butt_1.setEnabled(True)
                self.ui.butt_2.setEnabled(True)
                self.ui.Butt_3.setEnabled(True)
                self.ui.butt_4.setEnabled(True)
                self.ui.butt_5.setEnabled(True)
                self.ui.butt_6.setEnabled(True)
                self.ui.butt_7.setEnabled(True)
                self.ui.butt_8.setEnabled(True)
                self.ui.butt_9.setEnabled(True)
                self.ui.butt_divide.setEnabled(True)
                self.ui.butt_minus.setEnabled(True)
                self.ui.butt_multiply.setEnabled(True)
                self.ui.butt_plus.setEnabled(True)
                self.ui.butt_equal.setEnabled(True)
                self.ui.butt_closebrac.setEnabled(True)
                self.ui.Butt_dot.setEnabled(True)
            else:
                b=a.rstrip(a[-1])
                self.ui.number_show_text.setText(f"{b}")
        except:
            self.ui.number_show_text.setText("")
    def sine(self):
        a=self.ui.number_show_text.text()
        try:
            j=a[-1]
        except:
            j=""
        if ("+" in j) or ("-" in j) or ("*" in j) or ("/" in j)  or (j == ""):
            a=a+"sin"
            self.ui.number_show_text.setText(f"{a}")
            self.ui.butt_00.setEnabled(False)
            self.ui.Butt_0.setEnabled(False)
            self.ui.butt_1.setEnabled(False)
            self.ui.butt_2.setEnabled(False)
            self.ui.Butt_3.setEnabled(False)
            self.ui.butt_4.setEnabled(False)
            self.ui.butt_5.setEnabled(False)
            self.ui.butt_6.setEnabled(False)
            self.ui.butt_7.setEnabled(False)
            self.ui.butt_8.setEnabled(False)
            self.ui.butt_9.setEnabled(False)
            self.ui.butt_divide.setEnabled(False)
            self.ui.butt_minus.setEnabled(False)
            self.ui.butt_multiply.setEnabled(False)
            self.ui.butt_plus.setEnabled(False)
            self.ui.butt_equal.setEnabled(False)
            self.ui.butt_closebrac.setEnabled(False)
            self.ui.Butt_dot.setEnabled(False)
        else:
            a=a+""
    def cosine(self):
        a=self.ui.number_show_text.text()
        try:
            k=a[-1]
        except:
            k=""
        if ("+" in k) or ("-" in k) or ("*" in k) or ("/" in k)   or (k=="") :
            a=a+"cos"
            self.ui.number_show_text.setText(f"{a}")
            self.ui.butt_00.setEnabled(False)
            self.ui.Butt_0.setEnabled(False)
            self.ui.butt_1.setEnabled(False)
            self.ui.butt_2.setEnabled(False)
            self.ui.Butt_3.setEnabled(False)
            self.ui.butt_4.setEnabled(False)
            self.ui.butt_5.setEnabled(False)
            self.ui.butt_6.setEnabled(False)
            self.ui.butt_7.setEnabled(False)
            self.ui.butt_8.setEnabled(False)
            self.ui.butt_9.setEnabled(False)
            self.ui.butt_divide.setEnabled(False)
            self.ui.butt_minus.setEnabled(False)
            self.ui.butt_multiply.setEnabled(False)
            self.ui.butt_plus.setEnabled(False)
            self.ui.butt_equal.setEnabled(False)
            self.ui.butt_closebrac.setEnabled(False)
            self.ui.Butt_dot.setEnabled(False)
        else:
            a=a+""
    def tangent(self):
        a=self.ui.number_show_text.text()
        try:
            l=a[-1]
        except:
            l=""
        if ("+" in l) or ("-" in l) or ("*" in l) or ("/" in l) or (l==""):
            a=a+"tan"
            self.ui.number_show_text.setText(f"{a}")
            self.ui.butt_00.setEnabled(False)
            self.ui.Butt_0.setEnabled(False)
            self.ui.butt_1.setEnabled(False)
            self.ui.butt_2.setEnabled(False)
            self.ui.Butt_3.setEnabled(False)
            self.ui.butt_4.setEnabled(False)
            self.ui.butt_5.setEnabled(False)
            self.ui.butt_6.setEnabled(False)
            self.ui.butt_7.setEnabled(False)
            self.ui.butt_8.setEnabled(False)
            self.ui.butt_9.setEnabled(False)
            self.ui.butt_divide.setEnabled(False)
            self.ui.butt_minus.setEnabled(False)
            self.ui.butt_multiply.setEnabled(False)
            self.ui.butt_plus.setEnabled(False)
            self.ui.butt_equal.setEnabled(False)
            self.ui.butt_closebrac.setEnabled(False)
            self.ui.Butt_dot.setEnabled(False)
        else:
            a=a+""
    def openb(self):
        a=self.ui.number_show_text.text()
        try:
            p=a[-1]
        except:
            p=""
        if ("n"  in p) or ("s" in p):
            a=a+"("
            self.ui.number_show_text.setText(f"{a}")
            self.ui.butt_00.setEnabled(True)
            self.ui.Butt_0.setEnabled(True)
            self.ui.butt_1.setEnabled(True)
            self.ui.butt_2.setEnabled(True)
            self.ui.Butt_3.setEnabled(True)
            self.ui.butt_4.setEnabled(True)
            self.ui.butt_5.setEnabled(True)
            self.ui.butt_6.setEnabled(True)
            self.ui.butt_7.setEnabled(True)
            self.ui.butt_8.setEnabled(True)
            self.ui.butt_9.setEnabled(True)
            self.ui.butt_divide.setEnabled(True)
            self.ui.butt_minus.setEnabled(True)
            self.ui.butt_multiply.setEnabled(True)
            self.ui.butt_plus.setEnabled(True)
            self.ui.butt_equal.setEnabled(True)
            self.ui.butt_closebrac.setEnabled(True)
            self.ui.Butt_dot.setEnabled(True)
        else:
            a=a+""
    def closeb(self):
        a=self.ui.number_show_text.text()
        try:
            q=a[-1]
        except:
            q=""
        if ("(" in q)or ("+" in q )or ("-" in q) or ("*" in q )or ("/" in q) or (q==""):
            a=a+""
        else:
            a=a+")"
            self.ui.number_show_text.setText(f"{a}")
            
    def complute(self):
        a=self.ui.number_show_text.text()
        try:
            z=a[-1]
        except:
            z=""
        try:
            if("+" in z) or ("-" in z) or ("*" in z) or ("/" in z):
                b=a.rstrip(a[-1])
                self.ui.number_show_text.setText(f"{b}")
                result=self.ui.number_show_text.text()
                result1=str(eval(result))
                self.ui.number_show_text.setText(f"{result1}")
            else:
                result=self.ui.number_show_text.text()
                result1=str(eval(result))
                self.ui.number_show_text.setText(f"{result1}")
        except:
            self.ui.erroe_show.setText("use open and close braces")

    def mousePressEvent(self,event):
        self.oldPosition=event.globalPos()
    def mouseMoveEvent(self,event):
        delta=QPoint(event.globalPos()-self.oldPosition)
        self.move(self.x()+delta.x(),self.y()+delta.y())
        self.oldPosition=event.globalPos()
    
app = QApplication(sys.argv)
gui = Window()
gui.show()
sys.exit(app.exec_())