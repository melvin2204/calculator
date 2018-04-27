from PyQt4 import QtGui, QtCore
import sys

#design file
import ui

class calculator(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(calculator, self).__init__(parent)
        self.setupUi(self)
        self.b1.clicked.connect(lambda: self.addNum(1))
        self.b2.clicked.connect(lambda: self.addNum(2))
        self.b3.clicked.connect(lambda: self.addNum(3))
        self.b4.clicked.connect(lambda: self.addNum(4))
        self.b5.clicked.connect(lambda: self.addNum(5))
        self.b6.clicked.connect(lambda: self.addNum(6))
        self.b7.clicked.connect(lambda: self.addNum(7))
        self.b8.clicked.connect(lambda: self.addNum(8))
        self.b9.clicked.connect(lambda: self.addNum(9))
        self.b0.clicked.connect(lambda: self.addNum(0))
        self.back.clicked.connect(lambda: self.removeNum())
        self.ac.clicked.connect(lambda: self.clear())
        self.calcuteButton.clicked.connect(calculate)

    #vars
    firstValue = ""
    calculationType = ""
    secondValue = ""

    def calculate(self):
        return;

    def removeNum(self):
        self.firstValue = self.firstValue[:-1]
        print(self.firstValue)

    def clear(self):
        self.firstValue = ""
        self.calculationType = ""
        self.secondValue = ""
        print("Cleared")

    def addNum(self,int):
        int = str(int)
        if len(self.firstValue) < 10:
            self.firstValue = self.firstValue + int
        print(self.firstValue)

    def updateDisplay(self):
        return
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = calculator()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()