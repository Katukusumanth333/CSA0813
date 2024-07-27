def fact(n):
    fact=1
    for i in range(1,n+1):
         fact=fact*i
         return fact
        n=3
        print("factorial of{}is{}".format(n,fact(n)))
