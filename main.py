import tkinter 
from admin import * 
import platform
import student

def for_clear():
    if platform.system() == "Windows" :
        os.system("cls")
    else :
        os.system("clear")


if __name__ == "__main__" :
    print("\t\t\tThis is a attendance Management System ")

    run = True 
    while run :
        print("\nPress :- \n1. Admin Login\n2. Teacher Login\n3. Student Login\n4. Exit")
        choice = int(input("Enter Your Choice :- "))
        if(choice == 1 ):
            if admin_login() :
                admin_screen()
        elif(choice == 2 ):
            pass 
        elif(choice == 3 ):
            if(student.student_login()):
                student.student_screen()
                
        elif(choice == 4 ):
            run = False 
        else:
            print("Enter a valid option ")

