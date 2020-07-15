
import queue
import stack
import traceback
import copy
class AoNmain:
    def __init__(self, dict):
        self.dict = dict        #网络节点的词典
        self.dictCopy = copy.deepcopy(self.dict)
        self.attackroad = []    #用以生成包含攻击路径的list表
        self.coutroad = 0   #用以统计路径数量
        self.attackStack = [(-3,1)]    #用栈的形式存储攻击路径的数字和概率

    def Analysis_neighbor(self):
        i = 0
        while(i<len(self.dict)-1):

            print('字典信息',i)
            j = -1
            while(j<len(self.dict)-1):
                try:
                   if(self.dict.get(j).get(i)!=None):

                       print("被%d节点攻击的概率为"%j,self.dict.get(j).get(i))

                       j = j+1
                   else:
                       j = j+1
                except Exception:
                    print('字典内没有')
                    j = j+1

            i += 1

    def Analysis_FindAllRoad(self,cinlist,node,coutlist):#字典，元组，列表，列表，表示输入字典，输入的开始节点通常用（-3，1）表示最开始
        try:
            m = node[0] #m记录元祖第一个点，表示节点
            if m!= -2:#用-2表示没有下一跳节点的点 （此处可以改进）
                coutlist[self.coutroad][0]=coutlist[self.coutroad][0]+','+'%d'%m  #词典
                coutlist[self.coutroad][1]=coutlist[self.coutroad][1]*node[1]   #概率

            if ((int(m) in cinlist) == True and cinlist.get(m) != {}):
                self.attackStack.append(node)
                n = cinlist.get(m).popitem()
                self.Analysis_FindAllRoad(cinlist,n,coutlist)   #递归调用

            else:
                if  len(self.attackStack) == 0: #判断出递归
                    print('done')

                else:
                    max1 = len(self.attackStack)-1
                    stacklast = self.attackStack[max1][0]
                    self.coutroad += 1

                    lennode = len(coutlist[self.coutroad-1][0]) #获取前一个路径的信息
                    coutlist.append(['0',1])#生成无用的节点用以拓宽list长度
                    temp = coutlist[self.coutroad-1][0][0:lennode-2] #回朔节点在探查这个节点前的样子

                    coutlist[self.coutroad][0]=temp
                    coutlist[self.coutroad][1] = coutlist[self.coutroad-1][1]/node[1]#概率回朔
                    timebackNode = cinlist.get(stacklast)   #获取栈内信息

                    if timebackNode!={}:#如果栈内存的点有别的出路
                        self.Analysis_FindAllRoad(cinlist,timebackNode.popitem(),coutlist)

                    else:
                        c = self.attackStack.pop()  #如果没有别的出路弹出栈顶元素
                        aNode = c[0]    #节点号
                        proba = c[1]    #概率
                        cinlist[aNode] = copy.deepcopy(self.dictCopy[aNode])    #每当弹出一个结点，恢复这个节点的所有路径
                        b = (-2,proba)
                        self.Analysis_FindAllRoad(cinlist,b,coutlist)




        except Exception:
            traceback.print_exc()


    def NodeToNode(self,node):
        pass


if __name__ == "__main__":
    Anode = {0: 0.8,
             1: 0.4,
             2: 0.9}

    Bnode = {1: 0.7,
             3: 0.3}  # -1表示可以被外部攻击，0.8表示被攻击概率为0.8  1表示b可以攻击节点1 概率为0.7

    Cnode = {3: 0.7}

    Dnode = {1: 0.4,
             4: 0.1}

    Enode = {4: 0.7}

    Fnode = {}

    Origin = {-1: 1}
    listTest = {
        -3: Origin,
        -1: Anode,
        0: Bnode,
        1: Cnode,
        2: Dnode,
        3: Enode,
        4: Fnode
    }
    test = [['-3',1]]
    t1 = AoNmain(listTest)
    t1.Analysis_FindAllRoad(listTest,(-1,1),test)
    print(test)
    print(t1.dict)
    print('ok')