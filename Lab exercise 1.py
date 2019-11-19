# 3.to find how many apples each student gets and how many apples there will be in the basket
# n=int(input('Enter no. of students:'))
# k=int(input('Enter no. of apples:'))
# if k>n:
#     a=k//n
#     print('The no. of apples each student will get is:',a)
#     b=k-(n*a)
#     print('The no. of apples remaining in the basket is:',b)
# else:
#     print('The no. of students is more than no. of apples. Please enter the value so that no. of apples is more than no. of students.')


# 4.to find how many hours and minutes are displayed in 24h clock
# n=int(input('Enter the no. of minutes that has passed since midnight:'))
# if n>60:
#     h=n//60
#     m=n-(h*60)
# else:
#     h=0
#     m=n
# print('The time now is',h, m )


# 5.to print the smallest possible number of desks that can be purchased
# a=int(input('Enter no. of students in classroom a:'))
# b=int(input('Enter no. of students in classroom b:'))
# c=int(input('Enter no. of students in classroom c:'))
# if a%2==0:
#     d1=a/2
# else:
#     d1=(a+1)/2
# if b%2==0:
#     d2=b/2
# else:
#     d2=(b+1)/2
# if c%2==0:
#     d3=c/2
# else:
#     d3=(c+1)/2
# print('Desks in classroom a: ',int(d1))
# print('Desks in classroom b: ',int(d2))
# print('Desks in classroom c: ',int(d3))


# 6.to print out body mass index
m=float(input('Enter your mass:'))
h=float(input('Enter your height in meter:'))
bmi=m/(h**2)
print(bmi,(' kg/m^2'))


