import random
import time
from logo import display_logo2
import os

LIGHT_GREEN = "\033[1;32m"  # Light green color
ORANGE = "\033[1;33m"
GOLD = "\033[1;33m" 
ITALIC_RED = "\033[3;31m" 
ITALIC_GREEN = "\033[1;3;32m"
LIGHT_CYAN_BOLD = "\033[1;36m" 
RESET = "\033[0m"  # Reset styling


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def getpass() :
    os.system("clear")
    display_logo2()
    print(f"\n{ORANGE}****************welcome to the password generator*****************{RESET}")
    
    while True : 
        letters_num = int(input(f"\n1-\n  {LIGHT_CYAN_BOLD}How many latters you want in your password : {RESET}"))
        numbers_num = int(input(f"2-\n  {LIGHT_CYAN_BOLD}How many numbers you want in your password : {RESET}")) # this the better version of generating password for now 
        symbols_num = int(input(f"3-\n  {LIGHT_CYAN_BOLD}How many symbols you want in ur password : {RESET}"))

        password = ""
        counter = 0
        sizeofpassword = letters_num + numbers_num + symbols_num
        rand = random.randint(1,3) 
        while counter < sizeofpassword :
            random_num = rand
            match random_num :
                case 1 :
                    if letters_num > 0 :
                        letter_num = random.randint(0,52)
                        password += letters[letter_num]
                        letters_num -= 1
                        rand = random.randint(1,3) 
                    else :
                        rand = random.randint(2,3) 
                        counter = counter -1
                case 2 :
                    if numbers_num > 0 :
                        number_num = random.randint(0,9)
                        password += numbers[number_num]
                        numbers_num -= 1
                        rand = random.randint(1,3) 
                    else :
                        rand = random.choice([1, 3])
                        counter = counter -1
                case 3 :
                    if symbols_num > 0 :
                        symbol_num = random.randint(0,8)
                        password += symbols[symbol_num]
                        symbols_num -= 1
                        rand = random.randint(1,3) 
                    else :
                        rand = random.randint(1, 2)
                        counter = counter -1
                        
            counter = counter + 1

        print(f"\n-{LIGHT_GREEN}Your password is => {RESET} <{ORANGE} {password} {RESET}>")
        choice = input(f"  \n+ {ITALIC_GREEN}To restart press {RESET}<{ITALIC_RED}Enter{RESET}>{ITALIC_GREEN}, to end enter 'n' <> {RESET} ")
        if choice.lower() == 'n' or choice.lower() == 'no' :
            print(f"\n   {ITALIC_RED}Returning to main menu...{RESET}\n")
            time.sleep(2)  # Wait for 2 seconds 
            return
