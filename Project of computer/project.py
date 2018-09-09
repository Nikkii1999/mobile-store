Total_Amount=0
def MBrand1():
                global Total_Amount 
                r=[]
                Stock=[]
                while True:
                    print "Select Your Model"
                    f=open("Samsung.txt" ,"r")
                    while True:
                        rec = f.readline()
                        if not rec :
                            break
                        l=rec.split("#")
                        r.append(l)
                        Stock.append(l[0])
                        print l[0],l[1]
                    print
                    Model=raw_input("Enter Your Model")
                    if Model in Stock :
                        while True:
                            print "Colours Available Are:"
                            print "1.Black"
                            print "2.White"
                            print "3.Gold"
                            Colour = raw_input("Enter Your Colour")
                            if Colour in ["1","2","3"]:
                                for i in range(len(r)):
                                    if r[i][0] == Model:
                                        print "You Have To Pay Rs:",r[i][2],"For This Item"
                                        y=int(r[i][2])
                                        Total_Amount=Total_Amount+y
                                        break
                                break
                            else:
                                print "Wrong Colour Input Try Again"
                        break        
                    else:
                        print "Wrong Model Input Try Again"
                        
def MBrand2():
        global Total_Amount
        r=[]
        Stock=[]
        while True:
                print "Select Your Model"
                f=open("Nokia.txt","r")
                while True:
                    rec = f.readline()
                    if not rec :
                        break
                    l=rec.split("#")
                    r.append(l)
                    Stock.append(l[0])
                    print l[0],l[1]
                print
                Model=raw_input("Enter Your Model")
                if Model in Stock:
                    while True:
                        print "Colours Available Are:"
                        print "1.Black"
                        print "2.White"
                        print "3.Red"
                        Colour = raw_input("Enter Your Colour")
                        if Colour in ["1","2","3"]:
                            for i in range(len(r)):
                                if r[i][0] == Model:
                                    print "You Have To Pay Rs:",r[i][2],"For This Item"
                                    y=int(r[i][2])
                                    Total_Amount=Total_Amount+y
                                    break
                            break
                        else:
                            print "Wrong Colour Input Try Again"
                    break    
                else:
                    print "Wrong Model Input Try Again"
                    
def MBrand3():
        global Total_Amount
        r=[]
        Stock=[]
        while True:
                print "Select Your Model"
                f=open("Micromax.txt" ,"r")
                while True:
                    rec = f.readline()
                    if not rec :
                        break
                    l=rec.split("#")
                    r.append(l)
                    Stock.append(l[0])
                    print l[0],l[1]
                print
                Model=raw_input("Enter Your Model")
                if Model in Stock:
                    while True:
                        print "Colours Available Are:"
                        print "1.Black"
                        print "2.White"
                        print "3.Gold"
                        Colour = raw_input("Enter Your Colour")
                        if Colour in ["1","2","3"]:
                            for i in range(len(r)):
                                if r[i][0] == Model:
                                    print "You Have To Pay Rs:",r[i][2],"For This Item"
                                    y=int(r[i][2])
                                    Total_Amount=Total_Amount+y
                                    break
                            break
                        else:
                            print "Wrong Colour Input Try Again"
                    break        
                else:
                    print "Wrong Model Input Try Again"
                    
def MBrand4():
        global Total_Amount
        r=[]
        Stock=[]
        while True:
                print "Select Your Model"
                f=open("Htc.txt" ,"r")
                while True:
                    rec = f.readline()
                    if not rec :
                        break
                    l=rec.split("#")
                    r.append(l)
                    Stock.append(l[0])
                    print l[0],l[1]
                print
                Model=raw_input("Enter Your Model")
                if Model in Stock:
                    while True:
                        print "Colours Available Are:"
                        print "1.Black"
                        print "2.White"
                        print "3.Blue"
                        Colour = raw_input("Enter Your Colour")
                        if Colour in ["1","2","3"]:
                            for i in range(len(r)):
                                if r[i][0] == Model:
                                    print "You Have To Pay Rs:",r[i][2],"For This Item"
                                    y=int(r[i][2])
                                    Total_Amount=Total_Amount+y
                                    break
                            break
                        else:
                            print "Wrong Colour Input Try Again"
                    break        
                else:
                    print "Wrong Model Input Try Again"
                    
def TBrand1():
        global Total_Amount
        Stock=[]
        r=[]
        while True:
                print "Select Your Model"
                f=open("Apple.txt" ,"r")
                while True:
                    rec = f.readline()
                    if not rec :
                        break
                    l=rec.split("#")
                    r.append(l)
                    Stock.append(l[0])
                    print l[0],l[1]
                print
                Model=raw_input("Enter Your Model")
                if Model in Stock:
                    while True:
                        print "Colours Available Are:"
                        print "1.Black"
                        print "2.White"
                        print "3.Rose Gold"
                        Colour = raw_input("Enter ur Colour")
                        if Colour in ["1","2","3"]:
                            for i in range(len(r)):
                                if r[i][0] == Model:
                                    print "You Have To Pay Rs:",r[i][2],"For This Item"
                                    y=int(r[i][2])
                                    Total_Amount=Total_Amount+y
                                    break
                            break
                        else:
                            print "Wrong Colour Input Try Again"
                    break    
                else:
                    print "Wrong Model Input Try Again"
                    
def TBrand2():
        global Total_Amount
        Stock=[]
        r=[]
        while True:
                print "Select Your Model"
                f=open("Lenovo.txt","r")
                while True:
                        rec = f.readline()
                        if not rec :
                            break
                        l=rec.split("#")
                        r.append(l)
                        Stock.append(l[0])
                        print l[0],l[1]
                print
                Model=raw_input("Enter Your Model")
                if Model in Stock:
                        while True:
                            print "Colours Available Are:"
                            print "1.Black"
                            print "2.white"
                            Colour = raw_input("Enter Your Colour")
                            if Colour in ["1","2"]:
                                for i in range(len(r)):
                                    if r[i][0] == Model:
                                        print "You Have To Pay Rs:",r[i][2],"For This Item"
                                        y=int(r[i][2])
                                        Total_Amount=Total_Amount+y
                                        break
                                break
                            else:
                                print "Wrong Input Colour Try Again"
                        break
                else:
                        print "Wrong Input Model Try Again"
                        
def TBrand3():
            global Total_Amount 
            r=[]
            Stock=[]
            while True:
                    print "Select Your Model"
                    f=open("Dell.txt" ,"r")
                    while True:
                        rec = f.readline()
                        if not rec :
                            break
                        l=rec.split("#")
                        r.append(l)
                        Stock.append(l[0])
                        print l[0],l[1]
                    print
                    Model=raw_input("Enter Your Model")
                    if Model in Stock:
                        while True:
                            print "Colours Available Are:"
                            print "1.Black"
                            print "2.White"
                            Colour = raw_input("Enter Your Colour")
                            if Colour in ["1","2"]:
                                for i in range(len(r)):
                                    if r[i][0] == Model:
                                        print "You Have To Pay Rs:",r[i][2],"For This Item"
                                        y=int(r[i][2])
                                        Total_Amount=Total_Amount+y
                                        break
                                break
                            else:
                                print "Wrong Input Colour Try Again"
                        break
                    else:
                        print "Wrong Input Model Try Again"
                        
def TBrand4():
            global Total_Amount 
            r=[]
            Stock=[]
            while True:
                    print "Select Your Model"
                    f=open("Microsoft.txt" ,"r")
                    while True:
                        rec = f.readline()
                        if not rec :
                            break
                        l=rec.split("#")
                        r.append(l)
                        Stock.append(l[0])
                        print l[0],l[1]
                    print
                    Model=raw_input("Enter Your Model")
                    if Model in Stock:
                        while True:
                            print "Colours Available Are:"
                            print "1.Black"
                            print "2.White"
                            Colour = raw_input("Enter Your Colour")
                            if Colour in ["1","2"]:                            
                                for i in range(len(r)):
                                    if r[i][0] == Model:
                                        print "You Have To Pay Rs:",r[i][2],"For This Item"
                                        y=int(r[i][2])
                                        Total_Amount=Total_Amount+y
                                        break
                                break
                            else:
                                print "Wrong Input Colour Try Again"
                        break
                    else:
                        print "Wrong Input Model Try Again"
                        
def Update_Price(Name):
                import os
                fs=open(Name,"r")
                ft=open("Sample.txt","w")
                nm=raw_input("Enter The Name Of Modle")
                while True:
                    rec=fs.readline()
                    if not rec :
                        break
                    l=rec.split("#")
                    if l[1]==nm:
                        price=raw_input("Enter The updated price")
                        s=""
                        s=s+l[0]+"#"+l[1]+"#"+str(price)+'\n'
                        rec=s
                        print "Price Has Been Updated"
                        break
                    else:
                        print "Model Name Not Matched With Any Present Stock"
                ft.write(rec)
                fs.close()
                ft.close()
                os.remove(Name)
                os.rename("Sample.txt",Name)
def Delete_Stock(Name):
        import os
        fs=open(Name,"r")
        ft=open("Sample.txt","w")
        Model_Number=raw_input("Enter The Modle Number You Want To Remove")
        while True:
            rec=fs.readline()
            if not rec :
                break
            l=rec.split("#")
            if l[0]<>Model_Number:
                ft.write(rec)
        print "The Record Has Been Deleted"
        fs.close()
        ft.close()
        os.remove(Name)
        os.rename("Sample.txt",Name)
        
def Add_Stock(Name):
    import os
    fs=open(Name,"r")
    ft=open("Sample.txt","w")
    p=8
    c=0
    while True:
        rec=fs.readline()
        if not rec :
            break
        c=c+1
        ft.write(rec)
        if c==7:
            Model_Name=raw_input("Enter A Model Name To Add")
            Model_Price=raw_input("Enter Price Of The Model")
            ft.write("8"+"#"+Model_Name+"#"+Model_Price+'\n')
            print "Record Added"
    fs.close()
    ft.close()
    os.remove(Name)
    os.rename("Sample.txt",Name)


def Billing(x):
    if x<=15000:
        print "No Discount"
        print "Amount To Be Paid =",x
    elif x>15000 and x<=30000:
        x=x-(x*0.10)
        print "Discount Applied To Your Bill is 10%"
        print "Total Amount To Be Paid =",x
    elif x>30000 and x<=60000:
        x=x-(x*0.15)
        print "Discount Applied To Your Bill is 15%"
        print "Amount To Be Paid =",x
    else:
        x=x-(x*0.20)
        print "Discount Applied To Your Bill is 20%"
        print "Amount To Be Paid =",x

def Manager():
    while True:
        print "Which File would You Like To Operate On:"
        print "1.Samsung"
        print "2.Nokia"
        print "3.Micromax"
        print "4.Htc"
        print "5.Apple"
        print "6.Lenovo"
        print "7.Dell"
        print "8.Microsoft"
        print "9.Accessories"
        file_Name=int(raw_input("Which File would You Like To Operate On:"))
        if file_Name==1:
            Name="Samsung.txt"
            break
        elif file_Name==2:
            Name="Nokia.txt"
            break
        elif file_Name==3:
            Name="Micromax.txt"
            break
        elif file_Name==4:
            Name="Htc.txt"
            break
        elif file_Name==5:
            Name="Apple.txt"
            break
        elif file_Name==6:
            Name="Lenevo.txt"
            break
        elif file_Name==7:
            Name="Dell.txt"
            break
        elif file_Name==8:
            Name="Microsoft.txt"
            break
        else:
            print "Wrong File Input"
    while True:
        print "You Would Like to:"
        print "1.Update Price"
        print "2.Add New Stock"
        print "3.Delete Stock"
        ch=int(raw_input("Enter Your Choice"))
        if ch==1:
            Update_Price(Name)
        elif ch==2:
            Add_Stock(Name)
        elif ch==3:
            Delete_Stock(Name)
        else:
            print"Wrong Input"
        choice=raw_input("Do You Want Continue?")
        if choice=="y":
            continue
        else:
            break

def Customer():
    print "WELCOME TO TECH WORLD"
    while True:
            print "You Would Like To Buy ?"
            print "1. Mobile Phones"
            print "2. Tablets"
            print "3. Mobile Accesories"
            Requirement=int(raw_input("Enter Your Requirement"))
            if Requirement==1:
                    while True:
                            print "Select Your Brand"
                            f=open("Mobile_Brands.txt","r")
                            while True:
                                rec = f.readline()
                                if not rec :
                                    break
                                print rec,
                            print
                            f.close()
                            Brand = int(raw_input("Enter Your Brand"))
                            if Brand==1:
                                    MBrand1()
                                    break
                            elif Brand==2:
                                    MBrand2()
                                    break
                            elif Brand==3:
                                    MBrand3()
                                    break
                            elif Brand==4:
                                    MBrand4()
                                    break
                            else:
                                    print "Wrong Brand Input"
            elif Requirement==2:
                    while True:
                            print "Select Your Brand"
                            f=open("Tablet_Brands.txt","r")
                            while True:
                                rec = f.readline()
                                if not rec :
                                    break
                                print rec,
                            print
                            f.close()
                            Brand = int(raw_input("Enter Your Brand"))
                            if Brand==1:
                                    TBrand1()
                                    break
                            elif Brand==2:
                                    TBrand2()
                                    break
                            elif Brand==3:
                                    TBrand3()
                                    break
                            elif Brand==4:
                                    TBrand4()
                                    break
                            else:
                                print "Wrong Brand Input"
            elif Requirement==3:
                        global Total_Amount
                        while True:
                            print "Accersories Available Are:"
                            r=[]
                            f=open("Accersories.txt" ,"r")
                            while True:
                                rec=f.readline()
                                if not rec :
                                    break
                                l=rec.split("#")
                                r.append(l)
                                print l[0],l[1]
                            print
                            Model=raw_input("Enter Your Accersories Choice")
                            if Model in["1","2","3","4","5"]:                            
                                for i in range(len(r)):
                                    if r[i][0] == Model:
                                        print "You Have To Pay Rs:",r[i][2],"For This Item"
                                        y=int(r[i][2])
                                        Total_Amount=Total_Amount+y
                                        break
                                break
                            else:
                                    print "Wrong Accersories Input Try Again"
            else:
                        print "Wrong Input"                
            choice=raw_input("Do You want Something Else?")
            if choice=="y":
                    continue
            else:
                    break
    print "Your Total Bill Amount =",Total_Amount
    Billing(Total_Amount)
    Total_Amount=0

def Mobile_store():                                       
    while True:
        print"Log In To Website As "
        print"1.Manager"
        print"2.Customer"
        You=int(raw_input("Enter Your Choice"))
        if You==1:
            Manager()
        elif You==2:
            Customer()
        else:
            print "Wrong Input"
Mobile_store()

