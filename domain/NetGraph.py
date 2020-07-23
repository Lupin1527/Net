class NetGraph(object):
    def __init__(self,name,nodeList):
        # 图的名称
        self.name = name
        # 节点列表
        self.nodeList = nodeList
        # 节点个数
        self.nodeNum = len(nodeList)
        # 分析结果 attPathList
        self.result = None

    def analyze(self):



