from domain.Node import Node
from domain.NodeType import NodeType


class NetGraph(object):
    def __init__(self,name,nodeList=[]):
        # 图的名称
        self.name = name
        # 节点列表
        self.nodeList = nodeList
        # 节点个数
        self.nodeNum = len(nodeList)
        # 分析结果 attPathList
        self.result = None

    def analyze(self):


    def newNode(self,position,cat=NodeType.PC):
        num = self.nodeNum
        self.nodeNum = len(self.nodeList)
        nodeLabelList = []
        for node in self.nodeList:
            nodeLabelList.append(node.label)
        defaultNodeLabel = cat.name+str(num)
        while defaultNodeLabel in nodeLabelList:
            defaultNodeLabel = cat.name+str(++num)

        self.nodeList.append(Node(defaultNodeLabel)



