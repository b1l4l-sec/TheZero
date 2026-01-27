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



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']



def start():
    new_pos = 0
    mssg_analysed = ""
    type = input(f"\n1- {LIGHT_CYAN_BOLD}Enter 'encode' or 'decode' :{RESET} ").lower()
    mssg_to_analyse = input(f"   2- {LIGHT_CYAN_BOLD}Enter ur message please  :{RESET} ").lower()
    num_jump = int(input(f"      3- {LIGHT_CYAN_BOLD}Enter the shift number :{RESET} "))
    for letter in mssg_to_analyse :
        position = letters.index(letter)
        match type :
            case "encode"  : 
                new_pos = position + num_jump
            case "decode" : 
                new_pos = position - num_jump
            case _: 
                print(f"\n{ORANGE}    Choose just encode or decode Buddy <3{RESET}\n")
                time.sleep(2)
                break
        mssg_analysed += letters[new_pos]
    if type == "encode" or type == "decode" :
        print(f"\n{LIGHT_GREEN}-Your result is =>{RESET} <{GOLD} {mssg_analysed} {RESET}>")


def caesor():
    os.system("clear")
    display_logo2()
    while True :
        start()
        choice = input(f"  \n+ {ITALIC_GREEN}To restart press {RESET}<{ITALIC_RED}Enter{RESET}>{ITALIC_GREEN}, to end enter 'n' <> {RESET} ")
        if choice.lower() == 'n' or choice.lower() == 'no' :
            print(f"\n   {ITALIC_RED}Returning to main menu...{RESET}\n")
            time.sleep(2)  # Wait for 2 seconds 
            return
            

#print("END /_\ ")


    


