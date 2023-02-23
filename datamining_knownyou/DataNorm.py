# -*- coding:utf-8 -*-

import numpy as np
import math

class DataNorm:
    def __init__(self):
        self.arr = [1,2,3,4,5,6,7,8,9]
        self.x_max = max(self.arr)
        self.x_min = min(self.arr)
        self.x_mean = sum(self.arr) / len(self.arr)
        self.x_std = np.std(self.arr)  #标准差


    def min_max(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x - self.x_min) / (self.x_max - self.x_min),4))
        print("经过min_max标准化后的数据：{}".format(arr_))

    def z_score(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round ((x - self.x_mean) / self.x_std,4))
        print("经过z score 后：{}".format(arr_))

    def mean(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x - self.x_mean) / (self.x_max - self.x_min),4 ))
        print("经过均值归一 后：{}".format(arr_))

if __name__ == "__main__":
    dn = DataNorm()
    dn.min_max()
    dn.z_score()
    dn.mean()