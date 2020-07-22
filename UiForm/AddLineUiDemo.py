from UiForm.AddLineUI import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


class AddLineUi(QMainWindow,Ui_Form):
  AcceptLine_signal = pyqtSignal(str,str,str)
  RejectLine_signal = pyqtSignal()

  def __init__(self, parent=None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.setupUi(self)
    #self.setStyleSheet("background-color:cyan;")


  def AcceptLine(self):
    print('进入主界面')
    a = self.lineEdit.text() #起始结点
    b = self.lineEdit_2.text() #终止结点
    c = self.lineEdit_3.text() #概率
    self.AcceptLine_signal.emit(a,b,c)



  def RejectLine(self):
    print('退出界面')
    self.RejectLine_signal.emit()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = AddLineUi()
    main.show()
    sys.exit(app.exec_())
