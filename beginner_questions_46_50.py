
#46. Write a program to find the **last digit** of a number.

a=int(input("enter a num :"))
b=a%10

print(b, "is the last digit of ",a)

   
#47. Write a program to find the **first digit** of a two-digit number.

a=int(input("enter a num:"))

if a>=10 and a<=99:
    b=a//10    
    print(b)
else :
    print("error")
    

#48. Write a program to calculate the **sum of two numbers and then multiply the result by 2**.

a=int(input("enter first num:"))
b=int(input("enter second num:"))

c=a+b
print("addition of ", a, "and",b ," is :",c )

d=c*2
print(c," multiple by 2 than ans ", d)



#49. Write a program to calculate the **total cost of 3 products**.

a=int(input("total cost of first product:"))
b=int(input("total cost of second product:"))
c=int(input("total cost of third product:"))

print("total cost of three products" ,a+b+c)

#50. Write a program to calculate the **average of three numbers**.

a=float(input("enter a num:"))
b=float(input("enter 2nd num:"))
c=float(input("enter 3rd num:"))

avg=(a+b+c)/3
print("average : " ,avg)