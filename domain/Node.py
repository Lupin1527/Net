from domain.NodeType import NodeType
from domain.Position import Position
import jsonpickle as jp


class Node(object):
    def __init__(self,label,dst=[],vulne=[],pos=Position(0,0),cat=NodeType.PC):
        self.label = label
        self.dst = dst
        self.vulneList = vulne
        self.pos = pos
        self.cat = cat  # PC SERVER ROUTER ATTACKER
        



if __name__ == '__main__':
    node1 = Node('pc1',[],[],Position(0,0),NodeType.SERVER)
    node2 = Node('pc2',[{'pc1',0.8}],[],Position(1,1),NodeType.PC)
