#print key and its value as square of its key
# d=dict()
# for x in range(1,5):
#     d[x]=x**2
# print(d)

# #merge dictionary
# # d1={'a':100,'b':200}
# # d2={'x':300,'y':200}
# # d=d1.copy()
# # d.update(d2)
# # print(d)

#create a dict, add datas like, roll_no, name, marks, along with gender, now i want to print all the names and marks whose gender is male, how would you do that?
dict={'roll no':[1,2,3,4,5], 'name':['ram','hari','sita','gita','krishna'], 'mark':[87,85,78,79,89],'gen':['male','male','female','female','male']}
for i in range(len(dict['roll no'])):

    if dict['gen'][i]=='male':
        print(dict['name'][i])
        print(dict['mark'][i])


