from UiForm.AddPiontUI import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


class AddpointUi(QMainWindow,Ui_AddPoint):
  Acceptpoint_signal = pyqtSignal(str,str,str,str)
  Rejectpoint_signal = pyqtSignal()

  def __init__(self, parent=None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.setupUi(self)
    #self.setStyleSheet("background-color:cyan;")


  def acceptPoint(self):
    print('进入主界面')
    a = self.NameEdit.text() #结点名字
    b = self.vulneListEdit.text() #结点漏洞
    c = self.posEdit.text() #结点坐标
    d = self.catEdit.text() #结点的类型
    self.Acceptpoint_signal.emit(a,b,c,d)



  def reject_exit(self):
    print('退出界面')
    self.Rejectpoint_signal.emit()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = AddpointUi()
    main.show()
    sys.exit(app.exec_())
