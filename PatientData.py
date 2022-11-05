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
        returntomenu(patientstatus, username)
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
            returntomenu(patientstatus, username)
        if secondchoice == "2":
                updatepatientaskname = input("Which Patient do you wanna modify: ")
                if updatepatientaskname in patientstatus:
                    print(Fore.YELLOW + """
                    1. Change Patient Name
                    2. Change Patient Status
                    3. Change Patient Name and Status
                    """)
                    updatepatientchoice = input(Fore.YELLOW + "Select Your Choice >> ")
                    if updatepatientchoice == "1":
                            try:
                                updatepatientchangename = input("Change patient name to: ")
                                patientstatus[updatepatientchangename] = patientstatus[updatepatientaskname]
                                del patientstatus[updatepatientaskname]
                                print("Success!")
                                returntomenu(patientstatus, username)
                            except:
                                print("Changing Name failed")
                                returntomenu(patientstatus, username)
                    if updatepatientchoice == "2":
                        updatepatientchangestatus = input("Change patient's status to: ")
                        try:
                            patientstatus[updatepatientaskname] = updatepatientchangestatus
                            print("Success!")
                            returntomenu(patientstatus, username)
                        except:
                            print("Changing Status Failed")
                            returntomenu(patientstatus, username)
                else:
                    print("Patient not found")
                    returntomenu(patientstatus, username)
                if updatepatientchoice == "3":
                    try:
                        updatepatientchangename2 = input("Change patient name to: ")
                        updatepatientchangestatus2 = input("Change patient's status to: ")
                        patientstatus[updatepatientchangename2] = patientstatus[updatepatientaskname]
                        del patientstatus[updatepatientaskname]
                        patientstatus[updatepatientaskname] = updatepatientchangestatus2
                        print("Changing Name and Status Success!")
                        returntomenu(patientstatus, username)
                    except:
                        print("Failed to change name or status")
                        returntomenu(patientstatus, username)


def returntomenu(patientstatus, username):
    returntomenu = input("Return to main menu? (Press Enter): ")
    if returntomenu == "e" or "EE":
        mainmenu(patientstatus, username)

def hospitalterminalstartup(user, password, username, pwd, patientstatus):
    if user == username:
        if password == pwd:
            print(Fore.YELLOW + "Logged in")
            mainmenu(patientstatus, username)

    else:
        print("Invalid Username or Password")
        hospitalterminalstartup(terminallogin, terminalpass, username, pwd, PatientStatus)

PatientStatus = {

}

username = "super"
pwd = "super221009"

terminallogin = input(Fore.CYAN + "Enter your Username: ")
terminalpass = input(Fore.CYAN + "Enter your Password: ")

hospitalterminalstartup(terminallogin, terminalpass, username, pwd, PatientStatus)
