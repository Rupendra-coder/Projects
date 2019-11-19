# info={'rollno':[1,2,3,4,5], 'name':['Shahil','Anuj','Saurav','Bishnu','Hari']}
# info.update({'grade':['A','B','C','A','A']})
# print(info)

# a={'Anuj':1,'Bishnu':2}
# b={'Sanjay':3}
# a.update(b)
# print(a)

#to merge multiple no. of dictionaries using loop
# dic1={'no1':10,'no2':20}
# dic2={'no3':10,'no4':20}
# dic4={'no5':10,'no6':20}
# dic3={}
# for d in (dic1,dic2):
#     print(d)
#     dic3.update(d)
# print(dic3)

#to check if key is present in dictionary
# if 'no1' in dic1:
#         print('Key is present in dictionary')
# else:
#         print('Key is not present')

#to print key and its value as square of its keys
#d={}
# for v in range(1,5):
#     d[v]=v**2
# print(d)

#merge dictionary
# d1={'a':100,'b':200}
# d2={'x':300,'y':400}
# d=d1.copy()
# d.update(d2)
# print(d)

#to create dict add different datas and print all the names and marks whose gender is male
d={'name':['Shahil','Hari','Anuj','Sita'],'rollno':[1,2,3,4],'marks':[88,90,87,90],'Gender':['M','M','M','F']}
for i in range(len(d['rollno'])):
    if d['Gender'][i]=='M':
        print(d['name'][i])
        print(d['marks'][i])




