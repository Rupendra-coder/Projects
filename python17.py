#to print how many items among sets are repeated,unique,unrepeated
f1={'apple','banana','orange','mango'}
f2={'apple','peach','guava','banana'}
f3={'apple','watermelon','guava','pineapple'}

a=f1.intersection(f2)       # intersection between f1 and f2 is assigned to a
b=f1.intersection(f3)       # intersection between f1 and f3 is assigned to b
c=f3.intersection(f2)       # intersection between f2 and f3 is assigned to c
d=f1.intersection(f2,f3)    # intersection between all three sets is assigned to d
e=a.union(b,c,d)            # gives the union value of all the intersection value(a to d), therefore e gives all the values that are repeated
print('No. of repeated items=',len(e))
print('The repeated items are:',e)

f=f1.union(f2,f3)           # gives the union vale of all the three sets
g=f.difference(e)           # removes all the intersection value(e) from the union of three sets(f), therefore g gives unique value
print('No. of unique items=',len(g))
print('The unique items are:',g)

print('The unrepeated items are:',f)

