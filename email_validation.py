email=input("Enter your email: ")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
         #isalpha checks is ith index is an alpha character or not e.g (a-z)
        if ("@" in email) and (email.count("@")==1):
            if (email[-1:-11:-1][::-1]=="isrt.ac.bd"):
                for i in email: 
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1    
                    elif i.isdigit():
                        continue
                    elif i=="_" or i==".":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("Avoid space and use lowercase and also do not use other special character except _ and .")         
            else:
                print("Shoud've ended the mail with isrt.ac.bd")
        else:
            print("Should've inputted one @")

    else:
        print("First character should be an alpha character e.g (a-z)")
    
else:
    print("Too short")

        
        