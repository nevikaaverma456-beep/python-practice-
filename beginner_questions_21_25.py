#21. Write a program to check whether a number is **divisible by 5**.
a=float(input("Enter a number:"))
if a % 5==0:
     print(a,"is divisible by 5")
else :
    print(a ,"is not divisible by 5")


#22. Write a program to check whether a number is **divisible by both 3 and 5**.
num=float(input("enter a number:"))
if num%5==0 and num%3==0:     #used and: because the number must be divisible by both.
    print(num ,"num is divisible by 3 and 5")
else:
    print(num ,"num is not divisible by 3 and 5")
    
    
#23. Write a program to find the **largest of three numbers**.
a=float(input("enter 1st num:"))
b=float(input("enter 2nd num:"))
c=float(input("enter 3rd num:"))
if a>b and a>c :
    print(a, " is largest num")
elif b>a and b>c:
    print(b," is largest num:")
elif c>a and c>b :
    print(c ,"is a largest number")
else :
    print("error")


#24. Write a program to find the **smallest of three numbers**.
a=float(input("enter 1st num:"))
b=float(input("enter 2nd num:"))
c=float(input("enter 3rd num:"))
if a<b and a<c:
    print(a," is smallest")
elif b<a and b<c:
    print(b, " is smallest num")
else:
    print(c," is smallest num")



#25. Write a program to check whether a person is **eligible for a driving license** based on age.
name=input("Enter your name:")
age=float(input("Enter your age:"))
if age>=18:
    print(name , ", you are eligible for driving license")
else :
    print(name, ", you are not eligible for driving license")

