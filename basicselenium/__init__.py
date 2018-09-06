from  functools import reduce
n=[1,2,3,4]
r=[1,2,4,23]

re= reduce(lambda x,y: y+x ,n)
print(re)