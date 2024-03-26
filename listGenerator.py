grocerylist = []
print("WELCOME TO GROCERY STORE")
while True:
    
    userinput = input("Tell Us What To Do :\n- Add \n- Delete \n- Show \n- Exit \nEnter Your Choice: ")
    if userinput=="Add":
        newitem = input("What Do You Want To Add ? ")
        grocerylist.append(newitem)
    elif userinput=="Delete":
        delitem = input("What Do You Want To Delete ? ")    
        grocerylist.remove(delitem)
    elif userinput=="Show":
        print(grocerylist)
    elif userinput=="Exit":
        print("Program Exited , Thanks for Using..")
        break
    else:
        print("Invalid Input , Please Try Another Operation..") 






   


    