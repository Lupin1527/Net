import traceback
import copy

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

Origin = {-1:1}
listTest = {
    -3:Origin,
    -1: Anode,
    0: Bnode,
    1: Cnode,
    2: Dnode,
    3: Enode,
    4: Fnode
}
i = 0
j = 1
import  stack
import trace
print(listTest)
listTestCopyyyy = copy.deepcopy(listTest)
attackroad =[]
test = [['-3',1]]
stack1 = [(-3,1)]
coutroad = 0

def NodeToNode(cinlist,node,coutlist,stackbox):
    try:
        global coutroad
        m = node[0]
        if m!=-2:
            #print(node)
            coutlist[coutroad][0]=coutlist[coutroad][0]+','+'%d'%m
            coutlist[coutroad][1]=coutlist[coutroad][1]*node[1]


        if ((int(m) in cinlist) == True and cinlist.get(m)!={}):
            stackbox.append(node)
            n = cinlist.get(m).popitem()

            #coutlist[coutroad]=coutlist[coutroad]+(["%d->%d"%(m,n[0]),node[1]*n[1]])
            NodeToNode(cinlist,n,coutlist,stackbox)
        else:
            if  len(stackbox) == 0 :
                print('done')
            else:
                max1 = len(stackbox)-1
                stacklast = stackbox[max1][0]
                coutroad += 1

                lenname = len(coutlist[coutroad-1][0])
                coutlist.append(['0',1])
                temp = coutlist[coutroad-1][0][0:lenname-2]

                coutlist[coutroad][0]=temp

                coutlist[coutroad][1]=coutlist[coutroad-1][1]/node[1]
                timebackNode = cinlist.get(stacklast)
                #print(timebackNode)
                if timebackNode!={}:#如果这个不为空，直接读取下一个
                    #print(timebackNode.popitem())
                    NodeToNode(cinlist,timebackNode.popitem(),coutlist,stackbox)
                else:
                    c = stackbox.pop()#弹出栈顶元素
                    a = c[0]    #节点好
                    proba = c[1]    #概率
                    cinlist[a] = copy.deepcopy(listTestCopyyyy[a]) #每当往回走一步，回朔这个节点所有子节点的访问路径
                    #print(stack)
                    b = (-2,proba)
                    NodeToNode(cinlist,b,coutlist,stackbox)



#存在问题经过节点会使用掉节点的路径
#计算数值有问题



            return 'Done'

    except Exception as result:
        traceback.print_exc()











a = (-1,1)
#print(a)


NodeToNode(listTest,a,test,stack1)
print(test)



print('test')
