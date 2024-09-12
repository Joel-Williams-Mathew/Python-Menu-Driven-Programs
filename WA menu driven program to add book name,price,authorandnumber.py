d={}
while True:
    print("MENU\n1.Add New Book\n2.Search a Book\n3.Update Details\n4.Delete Book Information\n5.Exit\n")
    ch=int(input("Enter Your Choice :"))
    if ch==1:
        number=int(input("Enter the Book Number :"))
        name=input("Enter the Book Name :")
        author=input("Enter the Author of the Book :")
        price=input("Enter the Price of the Book :")
        d[name]=[number,author,price]
    elif ch==2:
        sbn=input("Enter the Book Name to Search :")
        for i in d:
            if sbn==i:
                print("Book Name :",i,"\nOther Details :",d[i])
                break
        else:
            print("Not found")
    elif ch==3:
        
        sbn=input("Enter the Book Name to be updated :")
        for i in d:
            if sbn==i:
                number=int(input("Enter the Book Number :"))
                author=input("Enter the Author of the Book :")
                pricee=input("Enter the Price of the Book :")
                d[sbn]=[number,author,price]
                break
        else:
            print("Not found")
    elif ch==4:
        sbn=input("Enter the Book Name to be deleted :")
        for i in d:
            if sbn==i:
                del d[sbn]
                break
        else:
            print("Not found")
        
    elif ch==5:
        break
    else:
        print("invalid choice")

print(d)
            
