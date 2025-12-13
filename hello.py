x=input("Whats your name ?")
print ('Hello\n "World!"',x)
## checking number is even or odd 

x=int (input("Enter the number to check whether it is even or odd:" ))
if (x%2)==0:
    print ("The number is even")
else:               
    print ("The number is odd")


# checking number is positive or negative
y=int (input("Enter the number to check whether it is positive or negative:" ))
if y>=0:
    print("The number is positive")
else:
    print("the number is negative")
    # largest of three number 

    
    a=int(input("Enter the 1st number "))
    b=int(input("Enter the 2nd number "))
c=int(input("Enter the 3rd number "))
if a>b and a>c:
    print (" The largest Number is a:",a)
elif b>c:
    print ("The largest number is b: ",b)
else:
    print ("The largest number is c",c)