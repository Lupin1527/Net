from PyQt5.QtWidgets import QApplication, QWidget
import sys
import pyqtgraph as pg
import numpy as np
from mainWindow import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt, pyqtSignal, QPropertyAnimation, QPoint, QAbstractAnimation, QEasingCurve,QLine
from PyQt5.QtCore import Qt, pyqtSignal



from pyqtgraph.Qt import QtCore, QtGui
#from testForDraw import *
class Graph(pg.GraphItem):#graph类
    def __init__(self):
        self.dragPoint = None
        self.dragOffset = None
        self.textItems = []
        pg.GraphItem.__init__(self)
        self.scatter.sigClicked.connect(self.clicked)

    def setData(self, **kwds):
        self.text = kwds.pop('text', [])
        self.data = kwds
        if 'pos' in self.data:
            npts = self.data['pos'].shape[0]
            self.data['data'] = np.empty(npts, dtype=[('index', int)])
            self.data['data']['index'] = np.arange(npts)
        self.setTexts(self.text)
        self.updateGraph()

    def setTexts(self, text):
        for i in self.textItems:
            i.scene().removeItem(i)
        self.textItems = []
        for t in text:
            item = pg.TextItem(t)
            self.textItems.append(item)
            item.setParentItem(self)    #这个决定了节点的字

    def updateGraph(self):
        pg.GraphItem.setData(self, **self.data)
        for i, item in enumerate(self.textItems):
            item.setPos(*self.data['pos'][i])

    def mouseDragEvent(self, ev):
        if ev.button() != QtCore.Qt.LeftButton:
            ev.ignore()
            return

        if ev.isStart():
            # We are already one step into the drag.
            # Find the point(s) at the mouse cursor when the button was first
            # pressed:
            pos = ev.buttonDownPos()
            pts = self.scatter.pointsAt(pos)
            if len(pts) == 0:
                ev.ignore()
                return
            self.dragPoint = pts[0]
            ind = pts[0].data()[0]
            self.dragOffset = self.data['pos'][ind] - pos
        elif ev.isFinish():
            self.dragPoint = None
            return
        else:
            if self.dragPoint is None:
                ev.ignore()
                return

        ind = self.dragPoint.data()[0]
        self.data['pos'][ind] = ev.pos() + self.dragOffset
        self.updateGraph()
        ev.accept()

    def clicked(self, pts):
        print("clicked: %s" % pts)


class win(QMainWindow,Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

        AddPoint_signal = pyqtSignal()
        AddLine_signal = pyqtSignal()


        test = Graph()

        self.resize(1000,500)
        self.pw = pg.PlotWidget(self)  # 创建一个绘图控件
        self.pw.resize(600,400)
        self.pw.move(20,20)
        self.pushButton.move(800,200)
        self.pushButton_2.move(800,250)
        self.Startlabel.move(808,280)
        self.startpoint.move(858,285)
        self.EndLabel.move(808,305)
        self.EndPoint.move(858,315)

        self.pw.addItem(test)
        ## Define positions of nodes

        pos = np.array([
            [0, 0],
            [10, 0],
            [0, 10],
            [10, 10],
            [5, 5],
            [15, 5]
        ], dtype=float)
        ## Define the set of connections in the graph
        adj = np.array([
            [0, 1],
            [0, 2],
            [0, 3],
            [1, 2],
            [1, 4],
            [2, 4],
            [3, 2],
            [4, 5]
        ])

        ## Define the symbol to use for each node (this is optional)
        symbols = ['o', 'o', 'o', 'o', 'o', 'o']

        ## Define the line style for each connection (this is optional)
        lines = np.array([
            (255, 0, 0, 255, 22),
            (255, 0, 255, 255, 2),
            (255, 0, 255, 255, 3),
            (255, 255, 0, 255, 2),
            (255, 0, 0, 255, 1),
            (255, 255, 255, 255, 4),
            (255, 255, 255, 255, 4),
            (255, 255, 255, 255, 4),

        ], dtype=[('red', np.ubyte), ('green', np.ubyte), ('blue', np.ubyte), ('alpha', np.ubyte), ('width', float)])
        for i in lines:
            m = i[4]
            # print('%s'%m)
            #print(i)
        ## Define text to show next to each symbol
        texts = ["Point %d" % i for i in range(6)]

        ## Update the graph
        test.setData(pos=pos, adj=adj, pen=lines, size=1, symbol=symbols, pxMode=False, text=texts)

        #要将pyqtgraph的图形添加到pyqt5的部件中，我们首先要做的就是将pyqtgraph的绘图方式由window改为widget。PlotWidget方法就是通过widget方法进行绘图的
         # 在绘图控件中绘制图形

    def AddPoint(self):
        newpiont = Graph()
        self.pw.addItem(newpiont)
        pos = np.array([
            [1, 1]
        ], dtype=float)

        ## Define the set of connections in the graph

        ## Define the symbol to use for each node (this is optional)
        symbols = ['o']

        ## Define the line style for each connection (this is optional)
        lines = np.array([
        ], dtype=[('red', np.ubyte), ('green', np.ubyte), ('blue', np.ubyte), ('alpha', np.ubyte), ('width', float)])
        #for i in lines:
         #   m = i[1]
            # print('%s'%m)
          #  print(i)
        ## Define text to show next to each symbol
        texts = ["new point"]

        newpiont.setData(pos=pos,  pen=lines, size=1, symbol=symbols, pxMode=False, text=texts)

        #self.AddPoint_signal.emit()

    def AddLine(self):
        print(type(self.test))

        #self.AddLine_signal.emit()


if __name__=='__main__':
    app=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(app.exec_())