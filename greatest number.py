a=int(input('Enter a no.:'))
b=int(input('Enter another no.:'))
c=int(input('Enter last no.:'))
if a > b and a > c:
    print('The greatest no. is '+str(a))
elif b > a and b > c:
    print('The greatest no. is '+str(b))
else:
    print('The greatest no. is '+str(c))
