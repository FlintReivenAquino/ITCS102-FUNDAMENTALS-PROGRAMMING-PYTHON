print("ODD Number Summation")

result=0

for a in range(1, 11, 1):
    
    number=eval(input("Enter a number: "))
    if number % 2 != 0:
         result+=number

print("The Sum of the ODD Numbers is", result)