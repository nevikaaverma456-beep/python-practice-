#61. Take a number and print its **double, triple, and half**.

a=int(input("enter a num:"))
b=a*2
print("double:" ,b)
c=a*3
print("triple:",c)
d=a/2
print("half:",d)
  
  
#62. Take a number and print its **square root**.

a=int(input("enter a num for square root:"))
b=1/2
c=a**b
print("square root of ",a , "is " ,c)

#62(2)Take a number and print its **cube root**.

a=int(input("enter a num for cube root:"))
b=1/3
c=a**b
print("cube root of ",a , "is " ,c)
  
   
#63. Take the **length and width** of a room and calculate the area in **square feet and square meters**.[meters = feet × 0.3048]

l=float(input("length(ft):"))
w=float(input("width(ft):"))
ft=l*w
print(ft, "square feet")
m = ft * 0.092903
print(m, "square meter")

#64. Take a person's **birth year** and calculate their approximate age.

a=int(input("enter your birth year: "))
b=int(input("enter the current year:"))
print("your age is:",b-a)

#65. Take the price of an item and quantity, then calculate the **total bill**.

a=str(input("Item name :"))
b=int(input("item price(1kg):"))
c=int(input("Item quantity(in kg):"))
print ( "total bill of the " ,a," is :" ,b*c )
