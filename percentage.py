a = float(input("enter your percentage"))
if a >= 90:
    temp = "A+"
elif (a >= 80) and (a < 90):
    temp = "A"
elif (a >= 70) and (a < 80):
    temp = "B+"
else:
    temp = "not available"
print(temp)

