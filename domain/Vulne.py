class Vulne(object):
    def __init__(self,id,description,attVector,attComplexity,integrity,confidentiality,usability):
        self.id = id    # 编号
        self.description = description  # 描述
        self.attVector = attVector  # 攻击向量
        self.attComplexity = attComplexity  # 攻击复杂度
        self.integrity = integrity  # 完整性影响
        self.confidentiality = confidentiality  # 机密性影响
        self.usability = usability  # 可用性影响


