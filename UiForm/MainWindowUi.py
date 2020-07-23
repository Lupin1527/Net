import sys
from UiForm.PersonalCreateModelDemo import *
from UiForm.AddPiontUIDemo import *
from UiForm.AddLineUiDemo import *
from PyQt5.QtWidgets import QApplication


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

if __name__ == '__main__':

    #创建窗口类别
    app = QApplication(sys.argv)
    personalUI_pane = PersonalUI()
    AddPoint_pane = AddpointUi(personalUI_pane)
    AddLineUi_pane = AddLineUi(personalUI_pane)

    #创建图类别
    mainGraph = Graph()
    personalUI_pane.pw.addItem(mainGraph)

    #创建具体的图
    pos = np.array([
        [0, 0],
        [10, 0],
        [0, 10],
        [10, 10],
        [5, 5],
        [15, 5]
    ], dtype=float)
    #print(type(pos))
    ## Define the set of connections in the graph
    adj = np.array([
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 2],
        [1, 4],
        [2, 4],
        [3, 2],
        [4, 5],

    ])
    #  adj = np.append(adj,[[0,4]],axis=0)

    #  print(adj)
    ## Define the symbol to use for each node (this is optional)
    symbols = ['o', 'o', 'o', 'o', 'o', 'o'] #list

    #print(type(symbols))

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
        #(244,233,233,233,1)

    ], dtype=[('red', np.ubyte), ('green', np.ubyte), ('blue', np.ubyte), ('alpha', np.ubyte), ('width', float)])
    print(lines)

    for i in lines:
        m = i[4]
        # print('%s'%m)
        # print(i)
    ## Define text to show next to each symbol
    texts = ["Point %d" % i for i in range(6)]    #list
   # print(type(texts))

    ## Update the graph
    mainGraph.setData(pos=pos, adj=adj, pen=lines, size=1, symbol=symbols, pxMode=False, text=texts)



    #创建槽
    def showGotoAddline():
        AddLineUi_pane.show()


    def showGotoAddPoint():
        AddPoint_pane.show()

    def Addline(startpoint,endpoint,posibility):
        print(int(startpoint))
        print(int(endpoint))
        #
        global adj,lines
        adj = np.append(adj,[[int(startpoint),int(endpoint)]],axis=0)
        adddline = np.array([
        (255, 0, 0, 255, 10),
    ], dtype=[('red', np.ubyte), ('green', np.ubyte), ('blue', np.ubyte), ('alpha', np.ubyte), ('width', float)])
        lines = np.append(lines,adddline,axis=0)
        print(lines)
        mainGraph.setData(pos=pos, adj=adj, pen=lines, size=1, symbol=symbols, pxMode=False, text=texts)



        AddLineUi_pane.hide()

    def ExitAddLineUi():
        AddLineUi_pane.hide()

    def Addpoint(name, vulne, position, cat):
        print(name)
        print(vulne)
        print(tuple(position))
        print(cat)
        global pos,symbols,texts
        pos = np.append(pos, [[15, 10]], axis=0)
       # print(pos)

        symbols.append('o')
       # print(symbols)
        texts.append('new point')
        mainGraph.setData(pos=pos, adj=adj, pen=lines, size=1, symbol=symbols, pxMode=False, text=texts)
        AddPoint_pane.hide()

    def ExitAddpointUi():
        AddPoint_pane.hide()


    #结尾
    personalUI_pane.GotoAddline_signal.connect(showGotoAddline)
    personalUI_pane.GotoAddpoint_signal.connect(showGotoAddPoint)

    AddLineUi_pane.AcceptLine_signal.connect(Addline)
    AddLineUi_pane.RejectLine_signal.connect(ExitAddLineUi)

    AddPoint_pane.Acceptpoint_signal.connect(Addpoint)
    AddPoint_pane.Rejectpoint_signal.connect(ExitAddpointUi)



    personalUI_pane.show()
    sys.exit(app.exec_())