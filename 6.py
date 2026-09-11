#36. Write a program to check whether a number is **between 10 and 50**.

num=float(input("enter a num:"))
if num>10 and num<50:
    print(num ," is between 10 and 50")
else :
    print(num ," is not between 10 and 50")    
    
    
#37. Write a program to calculate the **discount amount** on a product.[discount amount=(marked price*discount percentage)/100]

mp=int(input("enter price of the item:"))
dp=float(input("enter the discount percentage(in %):"))
da=(mp*dp)/100
print(da ," ,this is your item discount amount")

 
#38. Write a program to calculate the **final price after discount**.

mp=int(input("enter price of the item:"))
dp=float(input("enter the discount percentage(in %):"))
da=(mp*dp)/100
print(da ," ,this is your item discount amount")
p=mp-da
print(p ," ,this is your item finap price")


#39. Write a program to calculate the **electricity bill** based on units consumed. [The basic formula is:Electricity Bill =Units Consumed *rate per unit ]

u= float(input("write unit consumed:"))
r=7/100
e=u*r
print("electricity bill based on unit conssumed:", e)
 

#40. Write a program to create a simple **calculator** using two numbers and an operator.

a=float(input("enter first num:"))
c=input()
b=float(input("enter second num:"))

if c== "+":
    print("ans is ", a+b)
elif c=="-":
    print("ans is ", a-b)
elif c=="*":
    print("ans is ", a*b)
elif c=="/" and b==0 :
    print("error :division by zero")
elif c=="/":
    print("ans is",a/b)

else:
    print("error")