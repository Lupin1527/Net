import traceback
from queue import Queue
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
        self.result = [['0',1]]
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

        self.routeToVex = []#用来处理中间函数的（可以删，但暂时没想好怎么改）

        self.attractVex = []#用来记录攻击结点的所有路径


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
            #print(record[0].label)
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

    def WhoGetTheNode(self,node):  #得到所有到该结点的路径
        try:
            for route in self.result:
                length = len(route[0])
                if(length!=0):
                    needNumber = route[0][length-1]
                #print(needNumber)
                if(node.label == needNumber):
                    #print(route)
                    self.routeToVex.append(route[0])
            for route in self.routeToVex:
                roulen = len(route)

                while((roulen-2)>0):
                    #print(route[roulen-1],route[roulen-3])
                    endNode = (route[roulen-1])
                    startNode = (route[roulen-3])
                    for vex in self.vexList:
                        if(vex.end.label == endNode):
                            if(vex.start.label == startNode):
                                self.attractVex.append(vex)
                    roulen = roulen -2



        except Exception:
            traceback.print_exc()





if __name__ == '__main__':
    attA = AttTemplate('SSHproblem','no','no',0.8)
    attB = AttTemplate('SSHproblem', 'no', 'no', 0.4)
    attC = AttTemplate('HttpProblem','no','no',0.9)
    attD = AttTemplate('SMTPproblem','no','no',0.4)
    attE = AttTemplate('1433Problem','no','no',0.7)
    attF = AttTemplate('ShellProblem','no','no',0.3)
    attG = AttTemplate('bagProblem','no','no',0.1)
    G = NetGraph('test')
    G.newNode('0',None,'hard',NodeType.ATTACKER)
    NodeA = G.NodeGet('0')
    G.newNode('1',None,'test',NodeType.PC)
    NodeB = G.NodeGet('1')
    G.newNode('2',None,'test',NodeType.PC)
    NodeC = G.NodeGet('2')
    G.newNode('3',None,'test',NodeType.PC)
    NodeD = G.NodeGet('3')
    G.newNode('4',None,'test',NodeType.PC)
    NodeE = G.NodeGet('4')
    G.newNode('5',None,'test',NodeType.PC)
    NodeF = G.NodeGet('5')
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
    G.analyze(NodeA)
    G.WhoGetTheNode(NodeC)
    for vex in G.attractVex:
        print(vex.label)