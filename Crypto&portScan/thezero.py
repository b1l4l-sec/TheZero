import os
from logo import display_logo1
from portsscanner import scan
from cryptography_64_32 import cryptography_x64
from encode_decode import caesor
from password import getpass
import time

RED_BOLD_ITALIC = "\033[3;1;31m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_PURPLE = "\033[1;35m"
RESET = "\033[0m"

def main():

    while True:
        os.system("clear")

        display_logo1()
        print(f"{RED_BOLD_ITALIC}Every master was once a beginner. Every hero was once a zero.{RESET}\n")
        print(f"{LIGHT_GREEN}  [1]  Ports Scanner*")
        print(f"  [2]  Cryptography x64")
        print(f"  [3]  Encode & Decode (shift number)")
        print(f"  [4]  Generate a strong password")
        print(f"  [5]  Exit {RESET}")
        print("\n\n")

        try:
            choice = int(input(f"{LIGHT_PURPLE}Your choice please <3{RESET} "))

            if choice == 1:
                scan()
            elif choice == 2:
                cryptography_x64()
            elif choice == 3:
                caesor()
            elif choice == 4:
               getpass()
            elif choice == 5:
                print(f"\n   {RED_BOLD_ITALIC}Exiting The ZERO, See you next time...\n b1l4l-sec | TheZero v2.0{RESET}\n")
                time.sleep(3)
                os.system("clear")
                return
            else:
                print(f"{LIGHT_GREEN}Invalid choice! Please enter 1 or 2.{RESET}")
        except ValueError:
            print(f"{LIGHT_GREEN}Please enter a valid number!{RESET}")
        except KeyboardInterrupt:
            print("\n\n\033[1;31m[!] Exiting TheZero... See you next time! <3\033[0m\n")
            exit(0)



if __name__ == "__main__":
    main()
