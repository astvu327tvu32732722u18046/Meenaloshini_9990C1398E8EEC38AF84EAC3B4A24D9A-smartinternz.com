# 
def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
number=int(input("Enter the number:"))
if(number < 0):
    print("factorial does not exist for negative number")
else:
    print("factorial is :",factorial(number ))