from PyQt4 import QtGui, QtCore
import sys

#design file
import ui

class calculator(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(calculator, self).__init__(parent)
        self.setupUi(self)
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = calculator()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()