class AttPath(object):
    def __init__(self,path,usedTemplate):
        # list 攻击路径
        self.path = path
        # list 攻击路径上利用的漏洞 len(usedTemplate) == len(path)-1
        self.usedTemplate = usedTemplate
