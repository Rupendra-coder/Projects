#for i in range(10, 1, -1):
 #   print(i)
#
# for i in range(1, 100+1, 2):
#     print(i)

#find prime number in certain range
primes = []
n = int(input("enter a number"))
for n in range(2, n):
    ans = True
    for i in range(2, n):
        if n %i == 0:
            ans = False
            break
        if ans ==True:
                primes.append(n)
                print(primes)
