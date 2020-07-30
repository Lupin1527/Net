
from Nodetest.Node import *
from Nodetest.bsl import *
import copy
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
        self.result = [['a',1]]
        # 边列表
        self.vexList = vexList
        # 边个数
        self.vexNum = len(vexList)
        # 漏洞列表
        self.vulneList = vulneList
        # 漏洞个数
        self.vulneNum = len(vulneList)
        self.uselist = copy.deepcopy(self.vexList) #深复制边列表
        self.stack = []#栈
        self.roadnum = 0#生成路径个数


    def analyze(self,startNode):
        boolnum = 0
        nextNode = startNode
        if self.stack==[]:#如果栈为空
            return 1;
       # self.stack.append(startNode)
        #print(self.stack)
        for vex in self.uselist:        #进入循环判断是否有下一跳结点（遍历vex）
            if vex.start.label==startNode.label:
                boolnum = 1
                nextNode = vex.end
                self.delVexInUseList(vex.label)
                self.stack.append([vex,vex.attTemplateList.prob])
                #print(startNode.label)
                #print(vex.end.label)
                #print(vex.attTemplateList.prob)
               # self.result.append(['a',1])
                self.result[self.roadnum][0] = self.result[self.roadnum][0]+"+"+vex.end.label
                self.result[self.roadnum][1] = self.result[self.roadnum][1]*vex.attTemplateList.prob

               # print(self.result)
                break
        if boolnum == 1:#存在下一跳结点
            self.analyze(nextNode)

        else :#不存在下一跳结点
            m = copy.deepcopy(self.result[self.roadnum])
            self.result.append(m)
            self.roadnum = self.roadnum+1
            record = self.stack.pop()#弹出栈顶元素
            print(record[0].label)
            lennode = len(self.result[self.roadnum][0])
            temp = self.result[self.roadnum][0][0:lennode-2]
            self.result[self.roadnum][0] = temp
            self.result[self.roadnum][1] = self.result[self.roadnum][1]/record[1]
            #回朔所有用过的边
            for vex in self.vexList:
                if record[0].end.label == vex.start.label:
                    self.uselist.append(vex)
            #self.uselist.append(record[0])
            self.analyze(record[0].start)



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

    def delVexInUseList(self, label):
        for vex in self.uselist:
            if vex.label == label:
                self.uselist.remove(vex)
                return 0
        return -1

    def NodeGet(self,nodelabel):
        for node in self.nodeList:
            if node.label == nodelabel:
                return node
        return -1

    def VexGet(self,vexlabel):
        for vex in self.vexList:
            if vex.label == vexlabel:
                return vex
        return -1






if __name__ == '__main__':
    attA = AttTemplate('SSHproblem','no','no',0.8)
    attB = AttTemplate('SSHproblem', 'no', 'no', 0.4)
    attC = AttTemplate('HttpProblem','no','no',0.9)
    attD = AttTemplate('SMTPproblem','no','no',0.4)
    attE = AttTemplate('1433Problem','no','no',0.7)
    attF = AttTemplate('ShellProblem','no','no',0.3)
    attG = AttTemplate('bagProblem','no','no',0.1)
    G = NetGraph('test')
    G.newNode('a',None,'hard',NodeType.ATTACKER)
    NodeA = G.NodeGet('a')
    G.newNode('b',None,'test',NodeType.PC)
    NodeB = G.NodeGet('b')
    G.newNode('c',None,'test',NodeType.PC)
    NodeC = G.NodeGet('c')
    G.newNode('d',None,'test',NodeType.PC)
    NodeD = G.NodeGet('d')
    G.newNode('e',None,'test',NodeType.PC)
    NodeE = G.NodeGet('e')
    G.newNode('f',None,'test',NodeType.PC)
    NodeF = G.NodeGet('f')
    G.newVex('Vex0',NodeA,NodeB,attA)
    Vex0 = G.VexGet('Vex0')
    G.newVex('Vex1',NodeA,NodeC,attB)
    G.newVex('Vex2',NodeA,NodeD,attC)
    G.newVex('Vex3',NodeB,NodeE,attF)
    G.newVex('Vex4',NodeB,NodeC,attD)
    G.newVex('Vex5',NodeC,NodeE,attE)
    G.newVex('Vex6',NodeD,NodeC,attE)
    G.newVex('Vex7',NodeD,NodeF,attG)
    G.newVex('Vex8',NodeE,NodeF,attE)
   # print(G.nodeList)
  #  print(G.vexList)
    #G.result=[['a',1]]
    G.stack = [[Vex0,1]]

    G.uselist = copy.deepcopy(G.vexList)
    print(G.uselist)
    G.analyze(NodeA)
    print(G.result)
