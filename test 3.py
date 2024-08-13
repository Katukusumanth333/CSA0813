def anagram(a,b):
    a=a.lower()
    b=b.lower()
    return sorted(a)==sorted(b)
a=input("enter the first word : ")
b=input("enter the second word : ")
if anagram(a,b):
    print(a,"and",b,' are anagrams')
else:
    print(a,"and",b,'are not anagrams')




def multiplication(n):
    for i in range(1, 11):
        print(f"{n}*{i}={n * i}")
multiplication(4)



def reverse_string():
    A = input("Enter a string: ")
    reversed_string = A[::-1]
    return reversed_string
reversed_output = reverse_string()
print("Reversed String:", reversed_output)



def numbers(a):
    return(a)
a=[1,0,2,9,3,8]
a.sort()
print("the ascending order is ", a)
print("the descnding order is ", a[::-1])

