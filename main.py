import os
import sys
import time

def animation(string):
    os.system('clear')

    i = 0
    while i < 2:
        print(string + '.')
        i += 1
        time.sleep(0.75)
        os.system('clear')

        print(string + '...')
        i += 1
        time.sleep(0.75)

def check_input(command):
    if command.lower() == "e" or command.lower() == "exit":
        animation("LOADING MAIN MENU")
        main()
    elif command.lower() == "q" or command.lower() == "quit":
        print("EXITING TERMINAL SCREEN")
        time.sleep(0.5)
        sys.exit()



def user_menu():
    def refresh_user_menu():
        os.system('clear')
        print("-------------------------------------------------------")
        print("------------ WELCOME VALUED CUSTOMER ^.^ --------------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("|                                                     |")
        print("| <1> DISPLAY USER INFORMATION                        |")
        print("| <2> UPLOAD NEW PURCHASE                             |")
        print("| <4> DISPLAY CHEAPEST TRANSACTION                    |")
        print("| <5> DISPLAY MOST EXPENSIVE TRANSACTION              |")
        print("| <6> DISPLAY PAYMENT HISTORY                         |")
        print("| <6> DISPLAY ALL PURCHASES MADE                      |")
        print("| <E> ABORT LOGIN                                     |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
    
    while True:
        refresh_user_menu()
        command = input("WHAT WOULD YOU LIKE TO DO? ")
        os.system('clear')
        check_input(command)

def login_menu():
    def refresh_login():
        os.system('clear')
        print("-------------------------------------------------------")
        print("-------------------- LOGIN SCREEN ---------------------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <E> ABORT LOGIN                                     |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
        
    refresh_login()
    username = input("ENTER IN USERNAME: ")
    os.system('clear')
    
    check_input(username)
    if username not in users:
        animation("USER DOES NOT EXIST, RETURNING TO LOGIN SCREEN")
        login_menu()

    refresh_login()
    password = input("ENTER IN PASSWORD: ")
    os.system('clear')

    # TODO: Create a 2D List to store user information, and a dictionary for payment stuff
    check_input(password)

    animation(f"WELCOME {username}\n\n\tLOADING USER MENU")
    user_menu(username)

def signup_menu():
    def refresh_signup():
        os.system('clear')
        print("-------------------------------------------------------")
        print("------------------- SIGN UP SCREEN --------------------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <E> ABORT LOGIN                                     |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
    
        
    refresh_signup()
    username = input("ENTER IN USERNAME: ")

    check_input(username)
    if username.lower() in users:
        animation("USER ALREADY EXISTS, PLEASE USE A DIFFERENT USERNAME")
        signup_menu()
    
    def pw_step() -> str:
        refresh_signup()
        password = input("ENTER IN PASSWORD: ")
        check_input(password)
        if len(password) < 5:
            animation("PASSWORD IS TOO SHORT, MUST BE LONGER THAN 5 CHARACTERS")
            pw_step()

        return password

    password = pw_step()

    refresh_signup()
    full_name = input("ENTER IN FULL NAME: ")
    check_input(full_name)

    refresh_signup()
    p_number = input("ENTER IN PHONE NUMBER: ")
    check_input(p_number)

    refresh_signup()
    p_address = input("ENTER IN PERSONAL ADDRESS: ")
    check_input(p_address)

    f = open('data.txt', 'a')
    f.write(username + '\n')
    f.write(password + '\n')
    f.write(full_name + '\n')
    f.write(p_number + '\n')
    f.write(p_address + '\n')
    f.close()

    animation("SUCCESSFULLY SIGNED UP, RETURNING TO MAIN MENU")
    main()

def card_faq_menu():        
    os.system('clear')
    print("-------------------------------------------------------")
    print("------------------- CARD FAQ MENU ---------------------")
    print("-------------------------------------------------------")
    print(" _____________________________________________________ ")
    print("|                                                     |")
    print("|         SUPPORTED CARDS AND TRANSACTION FEES        |")
    print("|                                                     |")
    print("|  AMEX --------------------------------------- 0.8%  |")
    print("|  VISA --------------------------------------- 1.0%  |")
    print("|  DISCOVER ----------------------------------- 0.5%  |")
    print("|  CONVENIENCE FEE ---------------------------- 0.2%  |")
    print("|                                                     |")
    print("| <E> BACK TO MAIN MENU                               |")
    print("| <Q> EXIT                                            |")
    print("|_____________________________________________________|")
    print("\n")
    command = input("WHAT WOULD YOU LIKE TO DO? ")
    os.system('clear')
    check_input(command)
    
def main():
    f =  open('data.txt', 'r')
    users = f.readlines()
    f.close()

    print(users)

    running = True
    while running:
        os.system('clear')
        print("-------------------------------------------------------")
        print("----------- WELCOME TO OUR PAYMENT PLATFORM -----------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <1> LOGIN                                           |")
        print("| <2> SIGN UP                                         |")
        print("| <3> VIEW SUPPORTED CARDS                            |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
        command = input("WHAT WOULD YOU LIKE TO DO? ")
        os.system('clear')

        if command == "1":
            if not users:
                animation("NO EXISTING USERS, RETURNING TO MAIN MENU")
            else:
                animation("LOADING LOGIN SCREEN")
                login_menu()
        
        elif command == "2":
            animation("LOADING SIGN UP SCREEN")
            signup_menu(users)
        
        elif command == "3":
            animation("LISTING SUPPORTED CARDS")
            card_faq_menu()

        elif command.lower() == "q" or command.lower() == "quit":
            running = False
            print("EXITING TERMINAL SCREEN")
            time.sleep(0.5)
            sys.exit()
        else:
            animation("INVALID COMMAND")

if __name__ == "__main__":
    main()