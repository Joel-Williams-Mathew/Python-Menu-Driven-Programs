d={}
while True:
    print("MENU\n1.Add new\n2.Search\n3.Display\n4.Exit\n")
    ch=int(input("Enter your choice :"))
    if ch==1:
        name=input("Enter the name :")
        salary=float(input("Enter the salary :"))
        d[name]=salary
    elif ch==2:
        snm=input("Enter the name to search :")
        for i in d:
            if snm==i:
                print("Name :",i,"\nSalary :",d[i])
                break
        else:
            print("Not found")
    elif ch==3:
        for i in d:
            print(i,"-",d[i])
    else:
        break









