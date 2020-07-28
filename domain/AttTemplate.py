class AttTemplate(object):
    # premise is a AttTemplate class
    def __init__(self,vulne,premise,consequence,prob):
        self.vulne = vulne
        self.premise = premise
        self.consequence = consequence
        self.prob = prob