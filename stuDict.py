print("STUDENT MANAGEMENT SYSTEM")
studentdata = {}

while True:
    
    userinput = input("What do you want to do? \n-add \n-update \n-delete \n-show \n-exit\n ")
    if userinput == "add":
        stuid = input("Enter student Id: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        course = input("Enter Your Course: ")
        studentdata["Stuid"] = stuid
        studentdata["Name"] = name
        studentdata["Age"] = age
        studentdata["Course"] = course

    elif userinput == "update":
        toupd = input("What do you want to update \"stuid\" \"name\" \"age\" \"course\" : ")
        if "stuid" in toupd:
            newid = input("Enter new Id : ")
            studentdata["Stuid"] = newid
        elif "name" in toupd:
            newname = input("Enter new Name : ")
            studentdata["Name"] = newname
        elif "age" in toupd:
            newage = input("Enter new Age : ")
            studentdata["Age"] = newage
        elif "course" in toupd:
            newcourse = input("Enter new Course : ")
            studentdata["Course"] = newcourse
        else:
            print("Wrong Input")
    elif userinput == "delete":
        todel = input("enter what do you want to delete \"stuid\" \"name\" \"age\" \"course\" : ")
        if "stuid" in todel:
            del studentdata["Stuid"]
        elif "name" in todel:
            del studentdata["Name"]
        elif "age" in todel:
            del studentdata["Age"]
        elif "course" in todel:
            del studentdata["Course"]
        else:
            print("Wrong Input")
    elif userinput == "show":
        print(studentdata)        
    elif userinput == "exit":
        print("Program Exited")
        break
