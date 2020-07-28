class Vex(object):
    def __init__(self,label=None,start=None,end=None,attTemplateList=None):
        # 边的标签
        self.label = label
        # 变得起始点
        self.start = start
        # 边的末端点
        self.end = end
        # 边的攻击模版列表
        self.attTemplateList = attTemplateList
