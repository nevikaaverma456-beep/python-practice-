#41. Write a program to check whether a number is **greater than, less than, or equal to 50**.

a=float(input("enter a number:"))
if a<50:
    print(a,"is smaller than 50")
elif a>50:
    print(a, "is greater than 50")
else :
   print(a, "is equal to 50")
   
   
#42. Write a program to check whether a number is **divisible by 2**.

a=float(input("enter a num :"))
if a%2==0:
    print(a ," is divisible by 2")
else :
    print(a, "is not divisible by 2")


#43. Write a program to check whether a number is **divisible by 10**.

a=float(input("enter a num :"))
if a%10==0:
    print(a ," is divisible by 10")
else :
    print(a, "is not divisible by 10")


#44. Write a program to find the **absolute value** of a number. [always gives positive numbers]

a=float(input("enter a number:"))
if a<0:
    a=-a
    print(a)
else:
    print(a)


#45. Write a program to swap the values of **two variables**.

a=34
b=2
a,b=b,a
print(a)
print(b)
