#comment

name = input("insert your name ->" )
student = input("are you a student? (yes/no) --> ")
fare = eval(input("payment ->"))

if student == "yes" :
          discount = fare * .12
          print("Hi", name , "student discount is", discount)
else:
          print("Sorry", name , "you're not eligible for student discount")