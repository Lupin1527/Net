class AttPath(object):
    def __init__(self,path,usedTemplate,attackedNode,prob,consequence):
        # list 攻击路径
        self.path = path
        # list 攻击路径上利用的漏洞 len(usedTemplate) == len(path)-1
        self.usedTemplate = usedTemplate
        # 被攻击的结点
        self.attackedNode = attackedNode
        # 概率
        self.prob = prob
        # 后果
        self.consequence = consequence