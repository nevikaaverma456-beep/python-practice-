#31. Write a program to convert **Celsius to Fahrenheit**.[f=(c*9/5)+32]

c=float(input("enter a celsius temperature :"))
f=(c*(9/5)) +32
print(c ,"celsius to fahrenheit",f)             
              
              
                      
#32. Write a program to convert **Fahrenheit to Celsius**.[°C=(°F-32)×5/9]

f=float(input("enter the fahernhit temperature:"))
c=(f-32)*(5/9) 
print(f, "fahrenheit",c)
 

#33. Write a program to calculate the **square** of a number.

n=int(input("enter a number:"))
square=n*n
print(n ,"square num is ", square)
 
 
#34. Write a program to calculate the **cube** of a number.

n=int(input("enter a number:"))
cube=(n*n)*n
print(n ,"cube num is ", cube)


#35. Write a program to check whether a number is **greater than 100**.

num=float(input("enter a num:"))
if num>100 :
    print (num ,"the num is greater than 100")
else :
    print (num ,"the num is not greater than 100" )

