from UiForm.PersonalCreateModel import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys
import pyqtgraph as pg
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

class PersonalUI(QMainWindow,Ui_Form):
  GotoAddline_signal = pyqtSignal()
  GotoAddpoint_signal = pyqtSignal()

  def __init__(self, parent=None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.setupUi(self)
    #self.setStyleSheet("background-color:cyan;")

    self.pw = pg.PlotWidget(self)  # 创建一个绘图控件
    self.pw.resize(300, 200)
    self.pw.move(20, 20)


  def GoToAddPoint(self):
    print('进入加入结点界面')

    self.GotoAddpoint_signal.emit()



  def GoToAddLine(self):
    print('退出界面')
    self.GotoAddline_signal.emit()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = PersonalUI()
    main.show()
    sys.exit(app.exec_())