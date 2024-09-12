def empdetails():
    a=""
    f=open("E:\\TEXT FILES\\employeedetails.txt","w")
    print("1:Add Employee,2:Details,3:Exit")
    while True:
        ch=int(input("Enter the choice :"))
        if ch==1:
            n=int(input("Enter the no.of employees :"))
            for i in range(n):
                empno=input("Enter the employee number :")
                name=input("Enter the employee name :")
                salary=input("Enter the salary :")
                a=empno+" "+name+" "+salary
                f.write(a)
    
        if ch==2:
            f=open("E:\\TEXT FILES\\employeedetails.txt","r")
            st=f.read()
            print(st)
            f.close()
        if ch==3:
            break
empdetails()
