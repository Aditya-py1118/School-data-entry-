students=[]
while True:
 print(" Choose an option to continue:\n1.Add a new record\n2.Search a record\n3.Display all records\n4.Delete a record.")
 c=int(input(" Enter your desired choice here:"))
 if c==1:
    name=input("Enter the name of the student:")
    clas=int(input("Enter the class:"))
    R_no=int(input("Enter the assigned serial/roll number: "))
    record=[name,clas,R_no]
    students.append(record)
    print("record added successfully")
 elif c==2:
    roll=int(input("Enter the roll number to find the student:"))
    found=False

    for i in range(len(students)):
        if students[i][2]==roll:
            print("Record found:\n")
            print("Name:",students[i][0],"\n","Class:",students[i][1],"\n","Roll-no:",students[i][2],"\n")
            found=True
        else:
            print("Record not found\n")
            break
 elif c==3:
    if len(students)==0:
       print("No records found.\n")
    else:
       print("\nAll Records:")
       for i in range(len(students)):
           print(f"{i+1}.Name:{students[i][0]},Class:{students[i][1]},Roll-No.:{students[i][2]}")
           print()
 elif c==4:
    roll=int(input("Enter the Roll-no to delete the record of the student:"))
    found=False
    for i in range(len(students)):
        if students[i][2]==roll:
            students.pop(i)
            print("Record deleted successfully")    
            found=True 
            break
        else:
            print("NO record was found\n(please recheck the roll-no that you entered)")
                    