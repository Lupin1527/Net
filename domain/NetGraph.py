from domain.AttTemplate import AttTemplate
from domain.Consequence import Consequence
from domain.Node import Node
from domain.NodeType import NodeType
from domain.Position import Position
import jsonpickle as jp


class NetGraph(object):
    def __init__(self, name, nodeList=None, attTemplate=None):
        # 去除错误
        if attTemplate is None:
            attTemplate = []
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
        # 攻击模版表
        self.attTemplate = attTemplate

    # 获得攻击者结点
    def getAttacker(self):
        for node in self.nodeList:
            if node.cat == NodeType.ATTACKER:
                return node

    def newNode(self, label=None, position=None, AttTemplateList=None, cat=NodeType.PC):
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
        self.nodeList.append(Node(label, AttTemplateList, position, cat))
        # 更新结点个数
        self.nodeNum = len(self.nodeList)

    # 添加结点
    def addNode(self, node):
        if isinstance(node, Node):
            self.nodeList.append(node)
            self.nodeNum = self.nodeNum + 1
        elif isinstance(node, list) and len(node) > 0 and isinstance(node[0], Node):
            for n in node:
                self.addNode(n)
        else:
            return -1

    # def newVex(self,label = None,start = None,end = None,attTemplateList = None):
    #     if label == None:
    #         # 得到边默认名
    #         num = 0
    #         vexLabelList = []
    #         for vex in self.vexList:
    #             vexLabelList.append(vex.label)
    #         label = 'vex' + str(num)
    #         while label in vexLabelList:
    #             label = 'vex' + str(num)
    #             num = num + 1
    #     # 添加边
    #     self.vexList.append(Vex(label,start,end,attTemplateList))
    #     # 更新边的个数
    #     self.vexNum = len(self.vexList)
    # 通过label删除node
    def delNodeByLabel(self, label):
        if isinstance(label, str):
            for node in self.nodeList:
                if node.label == label:
                    self.nodeList.remove(node)
                    return 0
            return -1
        elif isinstance(label, list) and len(label) > 0 and isinstance(label[0], str):
            for l in label:
                self.delNodeByLabel(l)
        else:
            return -1

    # 通过label获取node
    def getNodeByLabel(self, label):
        if isinstance(label, str):
            for n in self.nodeList:
                if n.label == label:
                    return n
            print("no node's label is " + label)
            return None
        elif isinstance(label, list) and len(label) > 0 and isinstance(label[0], str):
            nodes = []
            for l in label:
                nodes.append(self.getNodeByLabel(l))
            return nodes
        else:
            return None

    # 分析漏洞
    def analyze(self, K):
        attacker = self.getAttacker()


if __name__ == '__main__':
    G = NetGraph('test')
    V1 = AttTemplate('V1', None, Consequence.CONTROL, 0.8)
    V2 = AttTemplate('V2', None, Consequence.CONTROL, 0.4)
    V3 = AttTemplate('V3', None, Consequence.CONTROL, 0.9)
    V4 = AttTemplate('V4', ['B'], Consequence.CONTROL, 0.7)
    V5 = AttTemplate('V5', ['D'], Consequence.CONTROL, 0.4)
    V6 = AttTemplate('V6', ['B'], Consequence.CONTROL, 0.3)
    V7 = AttTemplate('V7', ['C'], Consequence.CONTROL, 0.7)
    V8 = AttTemplate('V8', ['E'], Consequence.CONTROL, 0.7)
    V9 = AttTemplate('V9', ['D'], Consequence.CONTROL, 0.1)

    nodeA = Node('A', ['B', 'C', 'D'], cat=NodeType.ATTACKER)
    nodeB = Node('B', ['C', 'E'], ["V1"])
    nodeC = Node('C', ['E'], ["V2", "V4", "V5"])
    nodeD = Node('D', ['C', 'F'], ["V3"])
    nodeE = Node('E', ['F'], ["V6", "V7"])
    nodeF = Node('F', [], ["V8", "V9"])

    G.addNode([nodeA, nodeB, nodeC, nodeD, nodeE, nodeF])
    G.attTemplate = [V1, V2, V3, V4, V5, V6, V7, V8, V9]

    print(G)
    for node in G.nodeList:
        print(node)

    G.delNodeByLabel(['A', 'B'])

    print("---------")
    for node in G.nodeList:
        print(node)
