def greeter(yourname):
  print(f"Hi {yourname}, How are you? ")

def summation(q):
  
  sum = 0
  
  for w in range(q,0,-1):
    sum += w
  
  print(f"The sum of {q} is {sum}")

greeter("Flint")
greeter("Aquino")

summation(15)