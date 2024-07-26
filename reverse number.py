n=7
cout=0
for i in range(1,n+1):
    if (n%i==0):
        cout=cout+1
if cout==2:
    print(n,":prime")
else:
    print(n,"not prime")

            
