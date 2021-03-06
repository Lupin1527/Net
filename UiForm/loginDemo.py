from zxcfile.loginInterFace import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


class Main(QMainWindow,Ui_MainWindow):
  show_register_signal = pyqtSignal()
  show_contact_signal = pyqtSignal(str,str)

  def __init__(self, parent=None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.setupUi(self)
    #self.setStyleSheet("background-color:cyan;")


  def ShowContact(self):
    print('联系人界面')
    a = self.lineEdit.text()
    b = self.lineEdit_2.text()
    self.show_contact_signal.emit(a,b)



  def ShowRegister(self):
    print('弹出界面')
    self.show_register_signal.emit()

  def ShowAgain(self):
    print('重新输入')

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
