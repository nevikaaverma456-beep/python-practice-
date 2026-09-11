#51. Write a program to check whether a person's age is **between 18 and 60**.

a=int(input("enter a person's age:"))
if a>=18 and a<=60 :
    print("person's age is between 18 and 60")
else :
    print("person's age is not between 18 and 60")
    
#52. Write a program to check whether a number is **positive, negative, or zero**.

a=float(input("enter a number: "))
if a>0:
    print("num is positive")
elif a<0:
    print("num is negative")
else:
    print("num is zero")

#53. Write a program to assign a **grade based on marks**.

a= float(input("enter your marks:"))
if a>=91 and a<=100:
    print("Grade A+")
elif a>=81 and a<=90:
    print("Grade A")
elif a>=61 and a<=80:
    print("Grade B")
elif a>=46 and a<=60 :
    print("Grade C") 
elif a>=35 and a<=45:
    print("Grade D")
elif a>=0 and a<35:
    print("Fail")
else :
    print("error")    

 
#54. Write a program to calculate **salary after adding a bonus**.[Bonus = Salary × Bonus% / 100] and [Gross Salary = Salary + Bonus]

a=int(input("enter your salary:"))
b=int(input(" enter your bonus in %:"))
c=(a*b)/100
print("bonus: " ,c)
d=c+a
print("salary+bonus:" ,d)


#55. Write a program to calculate **salary after deducting tax**.

a=int(input("enter your salary:"))
b=int(input("enter your tax amount:"))
c=a-b
print(c , " is your salary after deducting tax")

