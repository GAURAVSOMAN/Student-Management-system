import main 



def student_login() :
    j ,k = 0 ,0  
    uname = str(input("Enter Username :- "))
    student_login.username = uname 
    passwd = str(input("Enter Password :- "))
    student_login.password = passwd
    cred = open("student.dat",'r').read()
    

    for i in cred.split() :
        if i == uname :
            break 
        else :
            j = j + 1 
    for passw in cred.split():
        if passw == passwd  and k == j + 1 :
            return True 
        else :
            k = k + 1 

def change_password():
    j = 0 
    k = 0
    file = open("student.dat").read()
    change = open("student.dat",'a')
    if(student_login()):
        changed_password = str(input("Enter New password "))
        for words in file.split():
            if student_login.username == words :
                break 
            else :
                j = j + 1 
        for word in file.split():
            k = k + 1
            if k == j + 2   :
                pass 

def student_screen():
    main.for_clear()
    print("Press \n1. Change Password ")
    choice = int(input("Enter Your Choice :- "))
    if choice == 1 :
        change_password()
    else :
        pass 



        
                
    
    
    


        
    

        


