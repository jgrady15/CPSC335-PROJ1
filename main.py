import os
import sys
import time
import sqlite3

def animation(string):
    os.system('cls')

    i = 0
    while i < 2:
        print(string + '.')
        i += 1
        time.sleep(0.75)
        os.system('cls')

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

# ######################################################################
# Actual Code Below
# ######################################################################
def user_menu(database, username, users, passwords):
    def upload_purchase():
        def refresh_purchase_entry():
            os.system('cls')
            print(f"CURRENTLY SIGNED IN AS {username}")
            print("-------------------------------------------------------")
            print("----------- WELCOME TO OUR PAYMENT PLATFORM -----------")
            print("-------------------------------------------------------")
            print(" _____________________________________________________ ")
            print("|                                                     |")
            print("|   DATE SHOULD BE LIKE: 11/26/1998                   |")
            print("|   AMOUNT IS 2 DECIMAL PLACES                        |")
            print("|                                                     |")
            print("| <E> ABORT PURCHASE                                  |")
            print("| <Q> EXIT                                            |")
            print("|_____________________________________________________|")
            print("\n")

        refresh_purchase_entry()
        date = input("ENTER DATE: ")
        os.system('cls')

        if date.lower() == "e" or date.lower() == "exit":
            user_menu(database, username, users, passwords)

        def check_card() -> str:
            os.system('cls')
            print(f"CURRENTLY SIGNED IN AS {username}")
            print("-------------------------------------------------------")
            print("----------- WELCOME TO OUR PAYMENT PLATFORM -----------")
            print("-------------------------------------------------------")
            print(" _____________________________________________________ ")
            print("|                                                     |")
            print("| <1> AMEX CARD                                       |")
            print("| <2> VISA CARD                                       |")
            print("| <3> DISCOVER CARD                                   |")
            print("| <E> ABORT PURCHASE                                  |")
            print("| <Q> EXIT                                            |")
            print("|_____________________________________________________|")
            print("\n")
            card = input("ENTER CARD TYPE: ")

            fee = 0
            if card == "1":
                card = "amex"
                fee = 1.08
            elif card == "2":
                card = "visa"
                fee = 1.1
            elif card == "3":
                card = "discover"
                fee = 1.05
            elif card == "e" or card == "exit":
                user_menu(database, username, users, passwords)
            elif card == "q" or card == "quit":
                print("EXITING TERMINAL SCREEN")
                time.sleep(0.5)
                sys.exit()
            else:
                animation("INVALID CARD TYPE")
                check_card()
            
            return (card, fee)
        
        temp = check_card()
        card = temp[0]
        fee = temp[1]
        
        refresh_purchase_entry()
        amount = input("ENTER AMOUNT OF PURCHASE: ")
        os.system('cls')

        if amount.lower() == "e" or amount.lower() == "exit":
            user_menu(database, username, users, passwords)
        
        os.system('cls')
        print(f"CURRENTLY SIGNED IN AS {username}")
        print("-------------------------------------------------------")
        print("----------- WELCOME TO OUR PAYMENT PLATFORM -----------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <1> PAID                                            |")
        print("| <2> DUE                                             |")
        print("| <E> ABORT PURCHASE                                  |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
        status = input("ENTER STATUS: ")

        amount = (float(amount) * fee) * 1.02
        connection.execute(f"INSERT INTO PURCHASES (date_id, card, amount, user_id, status) VALUES ('{date}', '{card}', {amount}, '{username}', '{status}')")
        database.commit()
        animation("SUCCESSFULLY ENTERED PURCHASE, RETURNING TO USER MENU")

    def refresh_user_menu():
        os.system('cls')
        print(f"CURRENTLY SIGNED IN AS {username}")
        print("-------------------------------------------------------")
        print("----------- WELCOME TO OUR PAYMENT PLATFORM -----------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <1> DISPLAY USER INFORMATION                        |")
        print("| <2> UPLOAD NEW PURCHASE                             |")
        print("| <3> DISPLAY CHEAPEST TRANSACTION                    |")
        print("| <4> DISPLAY MOST EXPENSIVE TRANSACTION              |")
        print("| <5> DISPLAY PAYMENT HISTORY                         |")
        print("| <6> DISPLAY ALL PURCHASES MADE                      |")
        print("| <E> LOGOUT                                          |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
    
    while True:
        refresh_user_menu()
        connection = database.cursor()
        command = input("WHAT WOULD YOU LIKE TO DO? ")
        os.system('cls')
        
        if command.lower() == "e" or command.lower() == "exit":
            animation("SIGNING OUT")
            login_menu(database, users, passwords)
        
        elif command.lower() == "q" or command.lower() == "quit":
            print("EXITING TERMINAL SCREEN")
            time.sleep(0.5)
            sys.exit()
        
        elif command == "1": 
            connection.execute(f"SELECT * FROM USERS WHERE username='{username}'")
            user_data = list(sum(connection.fetchall(), ()))
            print("USERNAME:\t", user_data[0])
            print("FULL NAME:\t", user_data[2])
            print("PHONE NUMBER:\t", user_data[3])
            print("ADDRESS:\t", user_data[4])

            connection.execute(f"SELECT SUM(amount) FROM PURCHASES WHERE user_id='{username}' AND STATUS='1'")
            paid = list(sum(connection.fetchall(), ()))
            print("AMOUNT PAID:\t", format(float(paid[0]), '.2f'))

            connection.execute(f"SELECT SUM(amount) FROM PURCHASES WHERE user_id='{username}' AND STATUS='2'")
            due = list(sum(connection.fetchall(), ()))
            print("AMOUNT DUE:\t",format(float(due[0]), '.2f'))
            time.sleep(5)
        
        elif command == "2":
            upload_purchase()

        elif command == "3":
            print("-------------------------------------------------------")
            print("-------------- LEAST EXPENSIVE PURCHASE ---------------")
            print("-------------------------------------------------------")
            connection.execute(f"SELECT date_id, card, min(amount) FROM PURCHASES WHERE user_id='{username}'")
            row = list(sum(connection.fetchall(), ()))
            print("DATE OF PURCHASE:\t", row[0])
            print("CARD TYPE:\t\t", row[1])
            print("AMOUNT SPENT:\t\t", format(float(row[2]), '.2f'))
            time.sleep(4)
        
        elif command == "4":
            print("-------------------------------------------------------")
            print("--------------- MOST EXPENSIVE PURCHASE ---------------")
            print("-------------------------------------------------------")
            connection.execute(f"SELECT date_id, card, max(amount) FROM PURCHASES WHERE user_id='{username}'")
            row = list(sum(connection.fetchall(), ()))
            print("DATE OF PURCHASE:\t", row[0])
            print("CARD TYPE:\t\t", row[1])
            print("AMOUNT SPENT:\t\t", format(float(row[2]), '.2f'))
            time.sleep(4)
        
        elif command == "5":
            os.system('cls')
            print(f"CURRENTLY SIGNED IN AS {username}")
            print("-------------------------------------------------------")
            print("----------- WELCOME TO OUR PAYMENT PLATFORM -----------")
            print("-------------------------------------------------------")
            print(" _____________________________________________________ ")
            print("|                                                     |")
            print("| <1> DISPLAY ALL PAID                                |")
            print("| <2> DISPLAY ALL DUE                                 |")
            print("| <E> BACK TO LOGIN MENU                              |")
            print("| <Q> EXIT                                            |")
            print("|_____________________________________________________|")
            print("\n")
            command = input("WHAT WOULD YOU LIKE TO DO? ")
            
            os.system("cls")
            if command.lower() == "e" or command.lower() == "exit":
                animation("SIGNING OUT")
                login_menu(database, users, passwords)
            
            elif command.lower() == "q" or command.lower() == "quit":
                print("EXITING TERMINAL SCREEN")
                time.sleep(0.5)
                sys.exit()
            elif command == "1":
                connection.execute(f"SELECT date_id, card, amount FROM PURCHASES WHERE user_id='{username}' AND STATUS='1'")
                row = list(sum(connection.fetchall(), ()))
                print("------------------------------------------")
                while row:
                    date = row.pop(0)
                    card = row.pop(0)
                    amount = row.pop(0)
                    print("DATE OF PURCHASE:\t", date)
                    print("CARD TYPE:\t\t", card)
                    print("AMOUNT PAID:\t", format(float(amount), '.2f'))
                    print("------------------------------------------")
                
            elif command == "2":
                connection.execute(f"SELECT date_id, card, amount FROM PURCHASES WHERE user_id='{username}' AND STATUS='2'")
                row = list(sum(connection.fetchall(), ()))
                print("------------------------------------------")
                while row:
                    date = row.pop(0)
                    card = row.pop(0)
                    amount = row.pop(0)
                    print("DATE OF PURCHASE:\t", date)
                    print("CARD TYPE:\t\t", card)
                    print("AMOUNT PAID:\t", format(float(amount), '.2f'))
                    print("------------------------------------------")
            time.sleep(4)
        
        elif command == "6":
            connection.execute(f"SELECT date_id, card, amount, status FROM PURCHASES WHERE user_id='{username}' ORDER BY date_id ASC")
            row = list(sum(connection.fetchall(), ()))
            print("------------------------------------------")
            while row:
                date = row.pop(0)
                card = row.pop(0)
                amount = row.pop(0)
                status = row.pop(0)
                print("DATE OF PURCHASE:\t", date)
                print("CARD TYPE:\t\t", card)
                print("AMOUNT SPENT:\t\t", format(float(amount), '.2f'))
                if status == "1":
                    print("STATUS:\t\t\t PAID")
                else:
                    print("STATUS:\t\t\t DUE")
                print("------------------------------------------")
            time.sleep(4)
        
        else:
            animation("INVALID COMMAND")

def login_menu(database, users, passwords):
    def refresh_login():
        os.system('cls')
        print("-------------------------------------------------------")
        print("-------------------- LOGIN SCREEN ---------------------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <E> GO BACK                                         |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
        
    refresh_login()
    username = input("ENTER IN USERNAME: ")
    os.system('cls')
    
    check_input(username)

    refresh_login()
    password = input("ENTER IN PASSWORD: ")
    os.system('cls')

    check_input(password)

    if username in users:
        i = users.index(username.lower())
        if password == passwords[i]:
            animation(f"WELCOME {username}\n\n\tLOADING USER MENU")
            user_menu(database, username, users, passwords)

    animation("USERNAME OR PASSWORD WAS INVALID, PLEASE TRY AGAIN")
    login_menu(database, users, passwords)

def signup_menu(database, users):
    def refresh_signup():
        os.system('cls')
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
        signup_menu(database, users)

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

    database.cursor().execute('''
            INSERT INTO USERS (username, password, name, phone, address, amt_due, amt_paid) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (username, password, full_name, p_number, p_address, 0.00, 0.00))
    database.commit()

    animation("SUCCESSFULLY SIGNED UP, RETURNING TO MAIN MENU")
    
    main()

def card_faq_menu():        
    os.system('cls')
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
    os.system('cls')
    check_input(command)
    
def main():
    try:
        database = sqlite3.connect("database.db")
        connection = database.cursor()
        connection.execute("SELECT username FROM USERS")
        users = list(sum(connection.fetchall(), ()))

        connection.execute("SELECT password FROM USERS")
        passwords = list(sum(connection.fetchall(), ()))

        print(users, passwords)
    except:
        print(sqlite3.Error)
    time.sleep(2)

    running = True
    while running:
        os.system('cls')
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
        os.system('cls')

        if command == "1":
            if not users:
                animation("NO EXISTING USERS, RETURNING TO MAIN MENU")
            else:
                login_menu(database, users, passwords)
        
        elif command == "2":
            signup_menu(database, users)
        
        elif command == "3":
            card_faq_menu()

        elif command.lower() == "q" or command.lower() == "quit":
            running = False
            time.sleep(0.5)
            sys.exit()
        else:
            animation("INVALID COMMAND")

if __name__ == "__main__":
    main()