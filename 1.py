#nested decision in python
#mukkti-decision program

print("*****Welcome To Netflix******")

name=input("Enter your name")
email=input("Type your email")
password=input("Password")
age=int(input("Enter your age"))

if age>=18:
    print(f"Dear{name}Welcome to Netflix")
    if email=="faisalhayat665@gmail.com" and password=="Admin123":
        print(f"Dear{name},Welcome to Netflix Sessions,please slect")
    elif email=="faisalhayat@gmail.com" and password=="Admin000":
        print(f"Dear{name},Welcome to Netflix Sessions,please slect")
    elif email=="faisal123@gmail.com" and password=="Hat123":
        print(f"Dear{name},Not fine")
    
    else:
        print(f"Dear{name}Login invalid!")
    
else:
    print(f"Dear{name},please let it go")
    
    








