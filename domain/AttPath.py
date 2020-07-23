class AttPath(object):
    def __init__(self,path,usedVulne):
        # list 攻击路径
        self.path = path
        # list 攻击路径上利用的漏洞 len(usedVulne) == len(path)-1
        self.usedVulne = usedVulne
