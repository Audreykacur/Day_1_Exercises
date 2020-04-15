


num = int(input("enter a number to see if it is even or odd: "))

if (num%4)==0:
    print ('{0} is a multiple of 4'.format(num))
elif (num%2)==0:
    print ('{0} is Even'.format(num))
else:
    print('{0} is Odd'.format(num))

num1 = int(input("enter a number to divide: "))
num2 = int(input("enter a number to divide by: "))

if (num1%num2)==0:
    print ('{0}/{1} divides evenly'.format(num1,num2))
else:
    print ("{0}/{1} does not divide evenly".format(num1,num2))
