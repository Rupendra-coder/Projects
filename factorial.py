#Hello

a=int(input('Enter a no.:'))
c=1
print('The factorial of '+str(a)+' is:')
for i in range(a):
    c=a*c
    a=a-1
print(c)
