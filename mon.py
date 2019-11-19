#to find name from roll no
l = {'roll no': [1,2,3,4], 'name': ['Anil', 'ram', 'shyam', 'hari', 'weeb']}
r = l['roll no']
n = l['name']
# print{r[2],n[2]}
temp = 0
data = int(input('enter your roll no '))
for i in range(len(r)):
    if r[i] == data:
        temp = i
print(n[temp])

# del(name['Anil'])
# for key in l.items():
#     print(key)