from domain.NodeType import NodeType
from domain.Position import Position
import jsonpickle as jp


class Node(object):
    def __init__(self, label, nextNode=None, VulneList=None, pos=Position(0, 0), cat=NodeType.PC):
        self.label = label
        # nextLabel
        self.next = nextNode
        self.VulneList = VulneList
        self.pos = pos
        self.cat = cat  # PC SERVER ROUTER ATTACKER

    def __str__(self):
        return self.label


if __name__ == '__main__':
    nodeA = Node('A', ['B', 'C', 'D'], cat=NodeType.ATTACKER)
    nodeB = Node('B', ['C', 'E'])
    nodeC = Node('C', ['E'])
    nodeD = Node('D', ['C', 'F'])
    nodeE = Node('E', ['F'])
    nodeF = Node('F', [])
