d={}
while True:
    print("MENU\n1.Add New Student\n2.Search a Student\n3.Update Details\n4.Delete Student Details\n5.Exit\n")
    ch=int(input("Enter Your Choice :"))
    if ch==1:
        rlno=int(input("Enter the Roll Number :"))
        name=input("Enter the Student Name :")
        mark1=float(input("Enter the Mark obtained in Computer Science :"))
        mark2=float(input("Enter the Mark obtained in English :"))
        mark3=float(input("Enter the Mark obtained in Chemistry :"))
        d[rlno]=[name,mark1,mark2,mark3]
    elif ch==2:
        search=input("Enter the Roll number of the student to be searched :")
        for i in d:
            if search==i:
                print("Name :",d[i][0])
                print("Mark of Computer Science :"d[i][1])
                print("Mark of English :",d[i][2])
                print("Mark of Chemistry :"d[i][3])
                break
        else:
            print("Student not found")
    elif ch==3:
        modify=int(input("Enter the Roll Number of the student to modify :"))
        for i in d:
            if modify==i:
                rlno=int(input("Enter the Roll Number :"))
                name=input("Enter the Student Name :")
                mark1=float(input("Enter the Mark obtained in Computer Science :"))
                mark2=float(input("Enter the Mark obtained in English :"))
                mark3=float(input("Enter the Mark obtained in Chemistry :"))
                break
        else:
            print("Student not found")
    elif ch==4:
        delete=int(input("Enter the Student Roll Number to be deleted :"))
        for i in d:
            if delete==i:
                del d[delete]
                break
        else:
            print("Student not found")

    elif ch==5:
        print(d)

    elif ch==6:
        break
    else:
        print("Invalid Choice")
        
                
        
                
