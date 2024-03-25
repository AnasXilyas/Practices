name = input("enter your Name :")
print("Name =", name)
Password = input("enter your Password:")
print("Password =", Password)
ConfrimPass = input("Confirn your password:")

if name in Password or name[::-1] in Password:
    print("password cannot be same as name or reverse.")

else:
    if len(Password) >= 8 :
        print("password is strong")
        if Password == ConfrimPass :
            print("welcome")
        else:
            print("password error")
    
    else:
        print("password is weak")




