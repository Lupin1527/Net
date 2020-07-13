Anode = {0:0.8,
         1:0.4,
         2:0.9}

Bnode = {1:0.7,
         3:0.3}#-1表示可以被外部攻击，0.8表示被攻击概率为0.8  1表示b可以攻击节点1 概率为0.7


Cnode = {3:0.7}

Dnode = {1:0.4,
         4:0.1}

Enode = {4:0.7}

Fnode = {}

listTest = {
    -1: Anode,
    0: Bnode,
    1: Cnode,
    2: Dnode,
    3: Enode,
    4: Fnode
}
import queue
import stack

class AoNmain:
    def __init__(self, dict):
        self.dict = dict

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

    def Analysis_FindAllRoad(self):
        externalNode = self.dict.get(-1)    #外部节点设为开始点
        print(externalNode)
        i = 0
        while(i<len(externalNode)):
            try:
                pass

            except Exception:
                print('Error')


t1 = AoNmain(listTest)
t1.Analysis_FindAllRoad()