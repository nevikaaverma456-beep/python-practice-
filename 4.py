#26. Write a program to calculate **simple interest**.[formula:- SI=(P*R*T)/100]    {WHERE:P = Principal (original amount) ;R = Rate of interest (% per year);T = Time (in years);SI = Simple Interest}

p=float(input("principal(original rate):"))
r=float(input("rate of year in %:"))
t=float(input("time (in years:)"))
si=(p*r*t)/100
print("simple interst = ",si)


#27. Write a program to calculate the **total marks** of 5 subjects.

e=float(input("english:"))
h=float(input("hindi:"))
m=float(input("maths:"))
s=float(input("science:"))
c=float(input("computer:"))
add=e+h+m+s+c
print("total marks of all subject: ",add )


#28. Write a program to calculate the **average marks** of 5 subjects.

e=float(input("english:"))
h=float(input("hindi:"))
m=float(input("maths:"))
s=float(input("science:"))
c=float(input("computer:"))
avg=(e+h+m+s+c)/5
print("average marks of all subject: ",avg)


#29. Write a program to calculate **percentage** from marks of 5 subjects. [Percentage:(Obtained marks/Total marks)​×100]:Total marks = maximum marks possible ;Obtained marks = marks you actually scored

e=float(input("english:"))
h=float(input("hindi:"))
m=float(input("maths:"))
s=float(input("science:"))
c=float(input("computer:"))
per=(((e+h+m+s+c)/500)*100)
print("total percentage",per )


#30. Write a program to check whether a student has **passed or failed**.

a=float(input("your marks in exam:"))
if a>=36 and a<=100:
    print("congrulation you are passed in your exam")
elif a<36 and a>=0:
    print("you are failed")
else :
    print("error")

