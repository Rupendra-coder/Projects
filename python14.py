# to ask the user to enter a roll no. and print the corresponding name from dictionary
info={'rollno':[1,2,3,4,5], 'name':['Shahil','Anuj','Saurav','Bishnu','Hari']}
a=info["rollno"]
b=info["name"]
# print(a[2],b[2])

x=int(input('Enter your roll no.'))
for i in range(len(a)):
    if a[i]==x:
        y=i
print('Your name is',b[y])
