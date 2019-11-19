L1=[1,"red",2,3]
L2=["apple","orange","banana"]
L5=L2+L1                        #adds L2 and L1
print(L5)
L3=["php","python","Java"]
L4=[]
L4.extend(L1)                   #adds each element of L1 at the end of L4
L1.extend(L2)                   #adds each element of L2 at the end of L1
print(L1)
L2.extend(L4)
print(L2)
L3.append("QBASIC")
print(L3)
L4.remove("red")
print(L4)

