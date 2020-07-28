from domain.Node import Node
from domain.NodeType import NodeType
from domain.Position import Position
from domain.Vex import Vex


class NetGraph(object):
    def __init__(self, name, nodeList=None, vexList=None, vulneList=None):
        # 去除错误
        if vulneList is None:
            vulneList = []
        if vexList is None:
            vexList = []
        if nodeList is None:
            nodeList = []
        # 图的名称
        self.name = name
        # 节点列表
        self.nodeList = nodeList
        # 节点个数
        self.nodeNum = len(nodeList)
        # 分析结果 attPathList
        self.result = None
        # 边列表
        self.vexList = vexList
        # 边个数
        self.vexNum = len(vexList)
        # 漏洞列表
        self.vulneList = vulneList
        # 漏洞个数
        self.vulneNum = len(vulneList)

    def analyze(self):
        return 0

    def newNode(self, label=None, position=None, vulneList=None, cat=NodeType.PC):
        if label == None:
            # 得到结点默认名
            num = 0
            nodeLabelList = []
            for node in self.nodeList:
                nodeLabelList.append(node.label)
            label = cat.name + str(num)
            while label in nodeLabelList:
                label = cat.name + str(num)
                num = num + 1
        # 默认坐标
        if position == None:
            position = Position(0, 0)

        # 向列表中加入node结点
        self.nodeList.append(Node(label, vulneList, position, cat))
        # 更新结点个数
        self.nodeNum = len(self.nodeList)

    def newVex(self,label = None,start = None,end = None,attTemplateList = None):
        if label == None:
            # 得到边默认名
            num = 0
            vexLabelList = []
            for vex in self.vexList:
                vexLabelList.append(vex.label)
            label = 'vex' + str(num)
            while label in vexLabelList:
                label = 'vex' + str(num)
                num = num + 1
        # 添加边
        self.vexList.append(Vex(label,start,end,attTemplateList))
        # 更新边的个数
        self.vexNum = len(self.vexList)

    def delNode(self,label):
        for node in self.nodeList:
            if node.label == label:
                self.nodeList.remove(node)
                return 0
        return -1

    def delVex(self,label):
        for vex in self.vexList:
            if vex.label == label:
                self.vexList.remove(vex)
                return 0
        return -1


if __name__ == '__main__':
    G = NetGraph('test')
    for i in range(10):
        G.newNode()
        G.newVex()
    G.newNode(None, Position(1, 1), None, NodeType.ROUTER)
    for node in G.nodeList:
        print(node.label)

    print('----------')
    G.delNode('PC3')
    G.delVex('vex1')
    for node in G.nodeList:
        print(node.label)
    for vex in G.vexList:
        print(vex.label)
