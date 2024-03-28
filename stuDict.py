print("STUDENT MANAGEMENT SYSTEM")
studentdata = {}
def addfun():
    
        studict = {}
        stuid = input("Enter student Id: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        course = input("Enter Your Course: ")
        
        studict["Name"] = name
        studict["Age"] = age
        studict["Course"] = course
        studentdata[stuid] = studict
def showfun():
     print(studentdata)


while True:
    
    userinput = input("What do you want to do? \n-add \n-update \n-delete \n-show \n-exit\n ")
    if userinput == "add":
         addfun()
    elif userinput == "update":
        stuid = input("What Student id to update : ")
        if stuid in studentdata:
          student = studentdata[stuid]
          newinput = input("what do you want to update? \n-Name \n-Age \n-Course :\n")
          
          if newinput == "Name":
               value = input("Enter new name : ")
               student["Name"] = value
          elif newinput == "Age":
               value = input("Enter new Age : ")
               student["Age"]  = value
          elif newinput == "Course":
               value = input("Enter new Course : ")
               student["Course"] = value

    elif userinput == "delete":
             stuid = input("enter id to delete : ")
             if stuid in studentdata:
                  del studentdata[stuid]
    elif userinput == "show":
            showfun()      
    elif userinput == "exit":
        print("Program Exited")
        break
