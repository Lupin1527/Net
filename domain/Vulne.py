from domain.Level import Level
import random

from domain.attVector import attVector


class Vulne(object):
    def __init__(self, id, description='', attVector=attVector.UNKNOWN, attComplexity=Level.UNKNOWN,
                 certification=False, integrity=Level.UNKNOWN, confidentiality=Level.UNKNOWN, usability=Level.UNKNOWN,
                 score=-1):
        self.id = id  # 编号
        self.description = description  # 描述
        self.attVector = attVector  # 攻击向量 attVector.UNKNOWN/LOCAL/OUTER
        self.attComplexity = attComplexity  # 攻击复杂度 Level.UKNOWN/NONE/LOW/MIDDLE/HIGH
        self.certification = certification  # 用户认证
        self.integrity = integrity  # 完整性影响
        self.confidentiality = confidentiality  # 机密性影响
        self.usability = usability  # 可用性影响
        self.score = score  # 分数
        # 计算漏洞危险等级
        if score >= 7.5:
            self.level = Level.HIGH
        elif score >= 4.5:
            self.level = Level.MIDDLE
        elif score >= 0:
            self.level = Level.LOW
        else:
            self.level = Level.UNKNOWN

        # 随机生成该漏洞被攻击的概率
        if attComplexity == Level.UNKNOWN:
            prob = -1
        elif attComplexity == Level.NONE:
            prob = 1
        else:
            prob = random.uniform(0, 1 / 3) + (3 - attComplexity.value) / 3
        self.prob = round(prob,3)


if __name__ == '__main__':
    v1 = Vulne('CVE-2020-181031', attComplexity=Level.UNKNOWN)
    v2 = Vulne('CVE-2020-181031', attComplexity=Level.NONE)
    v3 = Vulne('CVE-2020-181031', attComplexity=Level.LOW)
    v4 = Vulne('CVE-2020-181031', attComplexity=Level.MIDDLE)
    v5 = Vulne('CVE-2020-181031', attComplexity=Level.HIGH)
    v = [v1, v2, v3, v4, v5]

    for t in v:
        print(t.attComplexity, ' : ', t.prob)
