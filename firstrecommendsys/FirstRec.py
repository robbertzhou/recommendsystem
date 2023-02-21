# -*- coding:utf-8 -*-

import os
import json
import random
import math

class FirstRec:
    """
    初始化函数：
        filePath: 原始文件路径
        seed: 产生随机数的种子
        k: 选取的近邻用户个数
        nitems: 为每个用户推荐的电影数
    """
    def __init__(self,file_path,seed,k,n_items):
        self.file_path = file_path
        self.seed = seed
        self.k = k
        self.n_items = n_items
        self.users_1000 = self.__select_1000_users()

        train,test = self.__load_and_split_data()
        print("load json")
        json.dump(train,open("../data/train.json","w"))
        json.dump(test,open("../data/test.json","w"))

    def __select_1000_users(self):
        print("随机选择1000个用户")
        if os.path.exists("data/train.json") and os.path.exists("data/test.json"):
            return list()
        else:
            users = set()
            for file in os.listdir(self.file_path):
                one_path = "{}/{}".format(self.file_path,file)
                print("{}".format(one_path))
                with open(one_path,"r") as fp:
                    for line in fp.readlines():
                        if line.strip().endswith(":"):
                            continue
                        userID,_,_ = line.split(",")
                        users.add(userID)
            users_1000 = random.sample(list(users),1000)

            return users_1000

    def __load_and_split_data(self):
        train = dict()
        test = dict()
        if 1 < 0:
            pass
        else:
            random.seed(self.seed)
            for file in os.listdir(self.file_path):
                one_path = "{}/{}".format(self.file_path,file)
                with open(one_path,"r") as fp:
                    for line in fp.readlines():
                        if line.strip().endswith(":"):
                            movieID = line.split(":")[0]
                        else:
                            userID, rate, _ = line.split(",")
                            if userID in self.users_1000:
                                if random.randint(1,50) == 1:
                                    test.setdefault(userID, {})
                                    test[userID][movieID] = int(rate)
                                else:
                                    train.setdefault(userID, {})
                                    train[userID][movieID] = int(rate)
        return train,test


"""
    计算皮尔逊系数：
        rating1：用户1的评分记录：{"movieid":rate1}
        rating2:用户1的评分记录：{"movieid":rate1}
"""
def person(self,rating1,rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 =0
    sum_y2=0
    num = 0
    for key1 in rating1.keys():
        for key2 in rating2.keys():
            num += 1
            x = rating1[kye1]
            y = rating2[key2]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += math.pow(x,2)
            sum_y2 += math.pow(y,2)
    denominator = math.sqrt(sum_x2 - math.pow(sum_x,2) / num) * math.sqrt(sum_y2 - math.pow(sum_y,2) / num )
    if num == 0:
        return 0
    else:
        return (sum_xy - (sum_x*sum_y) / num) /denominator

if __name__ == "__main__":
    fp = "F:\\data\\archive\\test_path"
    seed = 30
    k = 15
    n_items = 20
    f_rec = FirstRec(fp,seed,k,n_items)


