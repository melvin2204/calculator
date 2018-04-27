from PyQt4 import QtGui, QtCore
import sys

#design file
import ui

class calculator(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(calculator, self).__init__(parent)
        self.setupUi(self)
        #numpad
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
        #remove num
        self.back.clicked.connect(lambda: self.removeNum())
        #clear
        self.ac.clicked.connect(lambda: self.clear())
        #calculate
        self.calculateB.clicked.connect(self.calculate)
        #comma
        self.bcomma.clicked.connect(self.comma)
        #functions
        self.addB.clicked.connect(lambda: self.edit("+"))
        self.divideB.clicked.connect(lambda: self.edit("/"))
        self.multiplyB.clicked.connect(lambda: self.edit("*"))
        self.subractB.clicked.connect(lambda: self.edit("-"))
        #ans
        self.ansB.clicked.connect(self.ans)


    #vars
    firstValue = ""
    calculationType = ""
    secondValue = ""
    result = ""

    def ans(self):
        self.firstValue = self.result
        self.updateDisplay()

    def comma(self):
        if not "." in self.firstValue:
            self.firstValue = self.firstValue + "."

    def edit(self,type):
        if len(self.firstValue) == 0:
            self.secondValue = "0"
        else:
            self.secondValue = self.firstValue
        self.firstValue = ""
        self.calculationType = type

    def calculate(self):
        if len(self.secondValue) == 0:
            return
        firstValue = float(self.firstValue)
        calcationType = self.calculationType
        secondValue = float(self.secondValue)
        result = 0
        self.firstValue = ""
        self.calculationType = ""
        self.secondValue = ""
        if calcationType == "-":
            result = secondValue - firstValue
        elif calcationType == "+":
            result = secondValue + firstValue
        elif calcationType == "/":
            result = secondValue / firstValue
        elif calcationType == "*":
            result = secondValue * firstValue
        if int(str(result).split(".")[1]) == 0:#comma is zero
            result = int(result)
        self.result = str(round(result,4))
        self.displayLCD.setText(str(round(result,5)))


    def removeNum(self):
        self.firstValue = self.firstValue[:-1]
        self.updateDisplay()

    def clear(self):
        self.firstValue = ""
        self.calculationType = ""
        self.secondValue = ""
        self.updateDisplay()
        print("Cleared")

    def addNum(self,int):
        int = str(int)
        intLen = len(self.firstValue)
        doubleLen = 0
        if "." in self.firstValue:
            intLen = len(self.firstValue.split(".")[0])
            doubleLen = len(self.firstValue.split(".")[1])
        if intLen < 10 and doubleLen < 5:
            self.firstValue = self.firstValue + int
        self.updateDisplay()

    def updateDisplay(self):
        val = self.firstValue.replace('.',',')
        if len(self.firstValue) == 0:
            val = "0"
        self.displayLCD.setText(val)
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = calculator()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()