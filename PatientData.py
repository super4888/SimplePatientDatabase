from colorama import Fore

import time

def mainmenu(patientstatus, username):
    global firstchoice
    print(Fore.YELLOW + "Hello, " + username + " What would you like to do today?")
    print(Fore.YELLOW + """
    1. Check patient data
    2. Add or Modify patient data
    3. Shutdown
    """)
    mainchoice = input(Fore.YELLOW + "Select Your Choice >> ")
    if mainchoice == "1":
        print(patientstatus)
        firstchoice = input(Fore.YELLOW + "Return to main menu? (Press Enter): ")
        if firstchoice == "e" or "EE":
            mainmenu(patientstatus, username)
    if mainchoice == "2":
        print(Fore.YELLOW + """
        1. Add Patient Data
        2. Update Patient Data
        3. Remove Patient Data
        """)
        secondchoice = input(Fore.YELLOW + "Select Your Choice >> ")
        if secondchoice == "1":
            adddataname = input("Add Patient name: ")
            adddatastatus = input("Add Patient Status: ")
            patientstatus[adddataname] = adddatastatus
            print("Patient Added!")
            secondchoicereturn = input("Return to main menu? (Press Enter): ")
            if secondchoicereturn == "e" or "ee":
                mainmenu(patientstatus, username)


def hospitalterminalstartup(user, password, username, pwd, patientstatus):
    if user == username:
        if password == pwd:
            print(Fore.YELLOW + "Logged in")
            mainmenu(patientstatus, username)

    else:
        print("Invalid Username or Password")


PatientStatus = {

}

username = "super"
pwd = "super221009"

terminallogin = input(Fore.CYAN + "Enter your Username: ")
terminalpass = input(Fore.CYAN + "Enter your Password: ")

hospitalterminalstartup(terminallogin, terminalpass, username, pwd, PatientStatus)
