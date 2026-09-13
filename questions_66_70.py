
#66. Take a total bill amount and number of people, then calculate the **amount each person should pay**.

a=int(input("total bill amount:"))
b=int(input("num of people:"))

print(a/b ,"per person ")
 
#67. Take a number of days and convert it into **weeks and remaining days**.

days=int(input("number of days:"))

week= days//7
rd= days %7

print(week ,"weeks")
print(rd ,"remaining days")


#68. Take a number of minutes and convert it into **hours and remaining minutes**.
min=int(input("minutes:"))

hour=min //60 
rm=min % 60

print(hour ,"hours")
print(rm ,"remaining minutes")
  
  
#69. Take a number of seconds and convert it into **hours, minutes, and seconds**.[ex 1hr1min25 sec]
sec=int(input("seconds:"))

hours=sec//3600
rm=sec%3600
min=rm//60
rs= rm%60

print(hours, " hours")
print(min,"minutes")
print(rs,"seconds")


#70. Take marks of **6 subjects** and calculate total, average, and percentage.

a=float(input("english:"))
b=float(input("hindi:"))
c=float(input("sciene:"))
d=float(input("sst:"))
e=float(input("maths:"))
f=float(input("sanskrit:"))

maximum_marks=int(input("maximum marks in one subject:"))
total=a+b+c+d+e+f
percentage=(total/(maximum_marks*60))*100


print("Obtained marks in all subjects: ",total )
print("remaining marks: ",(maximum_marks*6)-total )
print("average marks : " ,total /6 )
print("percentage:" ,percentage )
