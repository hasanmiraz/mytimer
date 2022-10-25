from datetime import datetime
from time import sleep
from mytimer import MyTimer
import pickle

x= input("input ")
p = []
while(x=="a"):
    y = input("y= ")
    t = MyTimer(y)
    t.start_t()
    p.append(t)
    print(t.start_time)
    x = input("input ")

print(p)
for i in p:
    print(i.start_time)

MyTimer.write_t(p)

from_file = MyTimer.read_t()
print("this is from file: ")
for i in from_file:
    print(i.debug_data())
    
# with open("file.pkl",'wb') as file:
#     pickle.dump(p,file)
# 
# with open('file.pkl','rb') as file:
#     x = pickle.load(file)
# 
# print(x[0].start_time)
# print(datetime.now()-datetime.now())
# print(time.localtime()-time.localtime())

