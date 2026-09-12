
#11.Write a program to calculate the area of a circle.[formula:-area= πr2​]
r=float(input("enter a number:"))
a= 3.14*(r*r)
print(a ,"is the area of a circle")

 
#12.Write a program to convert kilometers into meters.
km=float(input("km:"))
m=km*1000
print(m ,"meters")

#13.Write a program to convert hours into minutes.
hour=float(input("hour:"))
min=hour*60
print(min , "minutes")


#14.Write a program to calculate a person's age.
name=input("name:")
a= int(input("birth year:"))
b=int(input("current year:"))
c=b-a
print(name , "'s age = " ,c)


#15.Write a program to check whether a number is positive or negative.
num=float(input("enter a number:"))
if  num >0:
    print(num , "is positive") 
elif num<0:
    print(num , "is negative")
    
else:print(num ,"is zero")

#16.Write a program to check whether a number is even or odd.
num=int(input("enter a num:"))
if num%2==0:
    print(num ,"is even")
else:
    print(num, " is odd")
  
#17.Write a program to find the greater of two numbers.
a=float(input("enter 1st number: "))
b=float(input("enter 2nd number: "))
if a>b:
    print(a ," is greater than " ,b)
elif a<b:
    print(b ," is greater than" ,a )
else:
    print(a ,"equals to " ,b )
    
    
#18.Write a program to find the smaller of two numbers.
a=float(input("enter first num :"))
b=float(input("enter second num:"))
if a<b:
    print(a ,"is smaller than",b)
elif a>b:
    print(b ,"is smaller than", a)
else:
    print(a , "is equals to" ,b)


#19.Write a program to check whether a person is eligible to vote.
name=input("enter your name:")
age=int(input("enter your age:"))
if age>18:
    print("you are eligible for vote")
else :
    print("you are not eligible for vote")


#20.Write a program to check whether a number is zero or non-zero.
num=float(input("enter a num:"))
if num!=0:
    print("the number is non zero")
else :
    print("the num is zero")