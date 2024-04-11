# email=input("Enter your email: ")
# first,last=email.split("@")
#
# list1=[" ",',', '.', ':', ';', '(', ')', '[', ']', '{', '}', '_', '__', "'", '"', '\\', '...']
# valid_mail=True
#
# for elements in first:
#     if elements in list1:
#         valid_mail=False
#         break
#
# if valid_mail and  last=="gmail.com":
#     print("Right Email")
# else:
#     print("Wrong Email")


Email=input("Enter a Email: ")
k,j,d=0,0,0
if len(Email)>=6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count("@")==1):
            if Email[-4]=="." or Email[-3]==".":
                for i in Email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                        else:
                            pass
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")

            else:
                print("Wrong Email 4")
        else:
            print("Wrong mail 3")
    else:
        print("Wrong mail 2")
else:
    print("Wrong mail 1")