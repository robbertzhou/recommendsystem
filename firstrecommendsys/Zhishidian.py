import random
import json
import os
print(os.getcwd())
# users = set()
# with open("F:\\data\\archive\\combined_data_1.txt","r") as fp:
#     for line in fp.readlines():
#         if line.strip().endswith(":"):
#             continue
#         userID,_,_ = line.split(",")
#         users.add(userID)
# lt = list(users)
# print(lt[1])

train = dict()
train.setdefault("33",{})
train["33"]["001"] = 4
train["33"]["002"] = 5
# train["003"] = "4"
# train["001"] = "2"
json.dump(train,open("../data/train.json","w"))
# train.setdefault("33",{})[movieID] = "ee"
# print(train)

# with open("F:\\data\\archive\\combined_data_1.txt","r") as fp:
#     # id = fp.readline().split(":")[0]
#     # print("myid is:",id)
#     movieID = ""
#     for line in fp.readlines():
#         if line.strip().endswith(":"):
#             movieID = line.split(":")[0]
#         else:
#             try:
#                 userID, rate, _ = line.split(",")
#                 print(random.randint(1,50))
#             except Exception as e:
#                 print(line)

        # print("test",line)