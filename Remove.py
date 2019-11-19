# l=[1,2,3,4,5]
# for i in range l:
#     if l(i)==3:
#         del(l[3])
#     break
# print(l)

l=[1,2,3,4,5,6,7,8,9]
b=len(l)
print(b)
for items in l:
    if items % 2 == 1:
        l.remove(items)
    print(l)