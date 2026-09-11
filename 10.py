#56. Write a program to calculate the **cost of items after applying GST**.

a=int(input("enter your items cost:"))
b=int(input("enter your GST in %:"))
c=(a*b)/100
d=a+c
print(d ,"cost of items after applying GST")


#57. Write a program to check whether a given **year is a leap year**.

a=int(input('enter the year:'))             #2000 → divisible by 4 → ✅ leap year , 1900 → divisible by 4, but ❌ NOT a leap year
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):                                
    print(a ," is leap year")
else :
    print(a, "is not leap year+")


#58. Write a program to check whether three given numbers are **all equal**.

a= float(input("enter 1st num :"))
b= float(input("enter 2nd num :"))
c= float(input("enter 3rd num :"))
if a==b==c:
    print("all three given numbers are equal:") 
else:
    print("they are not equal")


#59. Write a program to check whether a number is a **two-digit number**.

a= int(input("enter a num :"))  
if a>=10 and a<=99:
    print(a ,"is two-digit number")
else :
    print(a, " is not two-digit number")
  
   
   
#60. Write a program to create a simple **login check** using a username and password.

#1ST ANS
a=input("username:")
b=input("password:")

if a=="nevika" :
    if b=="verma":
        print("successfully login")
    else :
        print("your password is wrong")
elif  b=="verma":
     if a=="nevika" :
         print("successfully login")
     else:     
         print("your username is wrong")
else:
    print("both are wrong") 


#2rd ans
a=input("username:")
b=input("password:")
if a=="nevika" and b=="verma":
     print("successfully login")
elif a!="nevika" and b=="verma" :
    print("your username is wrong")
elif b!="verma" and a=="nevika" :
    print("your password is wrong")
else:
    print("both are wrong")