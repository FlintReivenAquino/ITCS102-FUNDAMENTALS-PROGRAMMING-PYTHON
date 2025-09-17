print("Factorial Program")

num=eval(input("Enter a Number:"))

result=1

for a in range (num, 1, -1):
    result*=a

print("The factorial of",num,"is",result)