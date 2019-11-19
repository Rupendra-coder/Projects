min_num = int(input("Enter minimum nmber"))
max_num = int(input("Enter maximum number"))
for i in range(min_num, max_num + 1):
    if i % 2 == 0:
        print(i)