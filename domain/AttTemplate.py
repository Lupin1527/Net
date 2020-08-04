class AttTemplate(object):
    # premise is a AttTemplate class
    '''
    前提有三种：
    1.premise == None：能被访问
    2.type(premise[i]) == AttTemplate:漏洞组合
    3.type(premise[i]) == str:从特定结点访问
    '''
    def __init__(self,vulne,premise,consequence,prob):
        self.vulne = vulne
        self.premise = premise
        self.consequence = consequence
        self.prob = prob