print("STUDENT INFORMATION SYSTEM")
print("-----------------------------------\n")

student_records = {}

while True:
    print("SELECT FROM THE OPTION BELOW \nA- Add Information\nB- Search\nC- Delete a Record\nD- Modify a Record\nE- Exit")
    
    choice = input("Your choice         --->").lower()
    
    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("-----------------------")
        search_code = input("Key search for this student  ").upper()
        first_name = input("Input student first name  ").upper()
        last_name = input("Input student last name  ").upper()
        course = input("Input student course  ").upper()
        email = input("Input student email adress  ").upper()
        isSingle = input("Are you single (true or false) --> ")
        
        student_records = {search_code : [first_name, last_name, course, email, isSingle] }
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'b':
        os.system('cls')
        code = input("input search code ----> ")

        for i in student_record.keys():
            if code in student_records.keys():
                print("record found")
                
                for o in student_records[code].values():

            else:
                print("no found")

        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        print("Editing existing record")
    elif choice == 'e':
        print("System Exit")
        break
    else:
        print("invalid choice")