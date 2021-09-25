
import sys
import os 
import main


def admin_login():

    main.for_clear()
    username = str(input("Enter admin username :-"))
    password = str(input("\nEnter admin password :-"))
    if username == "admin" and  password == "admin@2" : 
        return True 

def add_student(name,rollno,username,password):
    add = open("student.dat","a+")
    add.write(name + " " +rollno + " " + username + " " + password + "\n")

def admin_screen():
    main.for_clear()
    print("Press\n1. Add Teacher\n2. Add Student\n3. LogOut\n")
    run = True 
    while run : 
        choice = int(input("Enter a Number "))
        if choice == 1 : 
            pass 
        elif choice == 2 :
            Name = str(input("\nEnter Student's Name :- "))
            Roll = str(input("\nEnter student's Roll no :-" ))
            Username = str (input("Enter student username :-"))
            Password = str(input("Enter student password :- "))
            add_student(Name ,Roll,Username,Password)
        elif choice == 3 : 
            run = False 

        else : 
            pass

