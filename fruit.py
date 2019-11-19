f1 ={'Apple', 'Orange', 'Banana', 'Peach',}
f2 ={'Apple', 'Orange', 'Mango', 'Grapes'}
f3 ={'Avogado', 'Apple', 'Orange','Carrot'}
f =f1.intersection(f2)
print(f.intersection(f3))
f4=f1.union(f2)
print(f4.symmetric_difference(f3))
print(f4.union(f3))