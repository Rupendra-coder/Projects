#removes odd elements from the list
L=[1,2,3,4,5,6]
b=len(L)
print(b)
for items in L:
    if items % 2 == 1:
         L.remove(items)
print(L)


