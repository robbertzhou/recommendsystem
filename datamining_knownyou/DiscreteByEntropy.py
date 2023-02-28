import numpy as np
import math

class DiscreteEntropy:
    def __init__(self,group,threshold):
        self.maxGroup = group
        self.minINfoThreshold = threshold
        self.result = dict()  # 保存划分结果

    def loadData(self):
        data = np.array(
            [
                [56,1],[87,1],[129,0],[23,0],[342,1],
                [641,1],[63,0],[2764,1],[2323,0],[453,1],
                [10,1],[9,0],[88,1],[222,0],[97,0],
                [2398,1],[592,1],[561,1],[764,0],[121,1]
            ]
        )
        return data

    def calEntropy(self,data):
        numData = len(data)
        labelCounts = {}
        for feature in data:
            oneLabel = feature[-1]
            #如果标签不在新的定义的字典则创建该标签
            labelCounts.setdefault(oneLabel,0)
            labelCounts[oneLabel] += 1

        shannonEnt = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key]) / numData
            shannonEnt -= prob * math.log(prob,2) #其中代表随机事件X为的概率，下面来逐步介绍信息熵的公式来源！

        return shannonEnt

    def split(self,data):
        #inf正无穷大
        minEntropy = np.inf




if __name__ == "__main__":
    dbe = DiscreteEntropy(group=6,threshold=0.5)
    data = dbe.loadData()
    ent = dbe.calEntropy(data)
    print(ent)
