# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Fri Apr 27 16:33:09 2018
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(400, 475)
        MainWindow.setMinimumSize(QtCore.QSize(400, 475))
        MainWindow.setMaximumSize(QtCore.QSize(400, 475))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.displayLCD = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        font.setPointSize(25)
        self.displayLCD.setFont(font)
        self.displayLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayLCD.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.displayLCD.setObjectName(_fromUtf8("displayLCD"))
        self.verticalLayout_2.addWidget(self.displayLCD)
        self.numpad = QtGui.QHBoxLayout()
        self.numpad.setObjectName(_fromUtf8("numpad"))
        self.numpadL = QtGui.QVBoxLayout()
        self.numpadL.setObjectName(_fromUtf8("numpadL"))
        self.b9 = QtGui.QPushButton(self.centralwidget)
        self.b9.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b9.setFont(font)
        self.b9.setObjectName(_fromUtf8("b9"))
        self.numpadL.addWidget(self.b9)
        self.b4 = QtGui.QPushButton(self.centralwidget)
        self.b4.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b4.setFont(font)
        self.b4.setObjectName(_fromUtf8("b4"))
        self.numpadL.addWidget(self.b4)
        self.b1 = QtGui.QPushButton(self.centralwidget)
        self.b1.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b1.setFont(font)
        self.b1.setObjectName(_fromUtf8("b1"))
        self.numpadL.addWidget(self.b1)
        self.bplusmin = QtGui.QPushButton(self.centralwidget)
        self.bplusmin.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.bplusmin.setFont(font)
        self.bplusmin.setObjectName(_fromUtf8("bplusmin"))
        self.numpadL.addWidget(self.bplusmin)
        self.numpad.addLayout(self.numpadL)
        self.numpadM = QtGui.QVBoxLayout()
        self.numpadM.setObjectName(_fromUtf8("numpadM"))
        self.b8 = QtGui.QPushButton(self.centralwidget)
        self.b8.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b8.setFont(font)
        self.b8.setObjectName(_fromUtf8("b8"))
        self.numpadM.addWidget(self.b8)
        self.b5 = QtGui.QPushButton(self.centralwidget)
        self.b5.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b5.setFont(font)
        self.b5.setObjectName(_fromUtf8("b5"))
        self.numpadM.addWidget(self.b5)
        self.b2 = QtGui.QPushButton(self.centralwidget)
        self.b2.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b2.setFont(font)
        self.b2.setObjectName(_fromUtf8("b2"))
        self.numpadM.addWidget(self.b2)
        self.b0 = QtGui.QPushButton(self.centralwidget)
        self.b0.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b0.setFont(font)
        self.b0.setObjectName(_fromUtf8("b0"))
        self.numpadM.addWidget(self.b0)
        self.numpad.addLayout(self.numpadM)
        self.numpadR = QtGui.QVBoxLayout()
        self.numpadR.setObjectName(_fromUtf8("numpadR"))
        self.b7 = QtGui.QPushButton(self.centralwidget)
        self.b7.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b7.setFont(font)
        self.b7.setObjectName(_fromUtf8("b7"))
        self.numpadR.addWidget(self.b7)
        self.b6 = QtGui.QPushButton(self.centralwidget)
        self.b6.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        font.setKerning(True)
        self.b6.setFont(font)
        self.b6.setObjectName(_fromUtf8("b6"))
        self.numpadR.addWidget(self.b6)
        self.b3 = QtGui.QPushButton(self.centralwidget)
        self.b3.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.b3.setFont(font)
        self.b3.setObjectName(_fromUtf8("b3"))
        self.numpadR.addWidget(self.b3)
        self.bcomma = QtGui.QPushButton(self.centralwidget)
        self.bcomma.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.bcomma.setFont(font)
        self.bcomma.setObjectName(_fromUtf8("bcomma"))
        self.numpadR.addWidget(self.bcomma)
        self.numpad.addLayout(self.numpadR)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addB = QtGui.QPushButton(self.centralwidget)
        self.addB.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.addB.setFont(font)
        self.addB.setObjectName(_fromUtf8("addB"))
        self.verticalLayout.addWidget(self.addB)
        self.subractB = QtGui.QPushButton(self.centralwidget)
        self.subractB.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.subractB.setFont(font)
        self.subractB.setObjectName(_fromUtf8("subractB"))
        self.verticalLayout.addWidget(self.subractB)
        self.multiplyB = QtGui.QPushButton(self.centralwidget)
        self.multiplyB.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.multiplyB.setFont(font)
        self.multiplyB.setObjectName(_fromUtf8("multiplyB"))
        self.verticalLayout.addWidget(self.multiplyB)
        self.divideB = QtGui.QPushButton(self.centralwidget)
        self.divideB.setMinimumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(50)
        self.divideB.setFont(font)
        self.divideB.setObjectName(_fromUtf8("divideB"))
        self.verticalLayout.addWidget(self.divideB)
        self.numpad.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.numpad)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ac = QtGui.QPushButton(self.centralwidget)
        self.ac.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(25)
        self.ac.setFont(font)
        self.ac.setObjectName(_fromUtf8("ac"))
        self.horizontalLayout_2.addWidget(self.ac)
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(25)
        self.back.setFont(font)
        self.back.setObjectName(_fromUtf8("back"))
        self.horizontalLayout_2.addWidget(self.back)
        self.ansB = QtGui.QPushButton(self.centralwidget)
        self.ansB.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(25)
        self.ansB.setFont(font)
        self.ansB.setObjectName(_fromUtf8("ansB"))
        self.horizontalLayout_2.addWidget(self.ansB)
        self.calculateB = QtGui.QPushButton(self.centralwidget)
        self.calculateB.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(25)
        self.calculateB.setFont(font)
        self.calculateB.setObjectName(_fromUtf8("calculateB"))
        self.horizontalLayout_2.addWidget(self.calculateB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Calculator", None))
        self.displayLCD.setText(_translate("MainWindow", "0", None))
        self.b9.setText(_translate("MainWindow", "9", None))
        self.b4.setText(_translate("MainWindow", "4", None))
        self.b1.setText(_translate("MainWindow", "1", None))
        self.bplusmin.setText(_translate("MainWindow", "+/-", None))
        self.b8.setText(_translate("MainWindow", "8", None))
        self.b5.setText(_translate("MainWindow", "5", None))
        self.b2.setText(_translate("MainWindow", "2", None))
        self.b0.setText(_translate("MainWindow", "0", None))
        self.b7.setText(_translate("MainWindow", "7", None))
        self.b6.setText(_translate("MainWindow", "6", None))
        self.b3.setText(_translate("MainWindow", "3", None))
        self.bcomma.setText(_translate("MainWindow", ",", None))
        self.addB.setText(_translate("MainWindow", "+", None))
        self.subractB.setText(_translate("MainWindow", "-", None))
        self.multiplyB.setText(_translate("MainWindow", "*", None))
        self.divideB.setText(_translate("MainWindow", "/", None))
        self.ac.setText(_translate("MainWindow", "AC", None))
        self.back.setText(_translate("MainWindow", "<-", None))
        self.ansB.setText(_translate("MainWindow", "ANS", None))
        self.calculateB.setText(_translate("MainWindow", "=", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

