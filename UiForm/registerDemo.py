import sys
from zxcfile.register import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


class Main(QMainWindow,Ui_Form):
  exit_register_signal = pyqtSignal()
  add_contact_signal = pyqtSignal(str)

  def __init__(self, parent=None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.setupUi(self)
    #self.setStyleSheet("background-color:cyan;")



  def exit_register(self):
      self.exit_register_signal.emit()

  def addPro(self):
      name = self.lineEdit
      self.add_contact_signal.emit(name)



if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
