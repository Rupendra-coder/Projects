#practice question
l1=['1','2','3','4']
l2=['a','b','c','d']
d=[]
b=len(l1)
n=1
for i in range(b):
    for j in range(b-1,-1,-1):
        c=l1[i]+l2[j]
        d.append(c)
while n<len(d)-11:
    del d[1]
while n<len(d)-7:
    del d[2]
while n<len(d)-3:
    del d[3]
print(d)