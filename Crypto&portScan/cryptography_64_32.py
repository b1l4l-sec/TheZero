import base64
from logo import display_logo2
import os
import time

LIGHT_GREEN = "\033[1;32m"  # Light green color
ORANGE = "\033[1;33m"
GOLD = "\033[1;33m" 
ITALIC_RED = "\033[3;31m" 
ITALIC_GREEN = "\033[1;3;32m"
LIGHT_CYAN_BOLD = "\033[1;36m" 
RESET = "\033[0m"  # Reset styling

# Function to encode data to Base64
def encode_base64(data):
    data_bytes = data.encode('utf-8')
    encoded_data = base64.b64encode(data_bytes)
    return encoded_data.decode('utf-8')  # Convert bytes back to string

# Function to decode data from Base64
def decode_base64(encoded_data):
    encoded_bytes = encoded_data.encode('utf-8')
    decoded_bytes = base64.b64decode(encoded_bytes)
    return decoded_bytes.decode('utf-8')  # Convert bytes back to string

# Function to encode data to Base32
def encode_base32(data):
    data_bytes = data.encode('utf-8')
    encoded_data = base64.b32encode(data_bytes)
    return encoded_data.decode('utf-8')  # Convert bytes back to string

# Function to decode data from Base32
def decode_base32(encoded_data):
    encoded_bytes = encoded_data.encode('utf-8')
    decoded_bytes = base64.b32decode(encoded_bytes)
    return decoded_bytes.decode('utf-8')  # Convert bytes back to string

# Main function for Base64 and Base32 encoding/decoding
def cryptography_x64():
    os.system("clear")
    display_logo2()
    print(f"\n{LIGHT_CYAN_BOLD}Welcome to Cryptography x64! Please choose an option : {RESET}🔐🛡️ \n")
    print(f"{LIGHT_GREEN}  [1] Encode to Base64")
    print(" [2] Decode from Base64")
    print("  [3] Encode to Base32")
    print(" [4] Decode from Base32")
    print(f"  [5] Back to Menu{RESET}")
    
    try:
        choice = int(input(f"\n{ORANGE}Enter your choice <3 {RESET} "))
        
        if choice == 1:
            data = input(f"\n   {GOLD}Enter the text to encode to Base64 <3 {RESET} ")
            encoded_data = encode_base64(data)
            print(f"   {ITALIC_GREEN}Encoded (Base64):{RESET} {encoded_data}")
            print(f"   {ITALIC_GREEN}Done Buddy 💻 💻 {RESET}")
        
        elif choice == 2:
            encoded_data = input(f"\n   {GOLD}Enter the Base64 string to decode <3 {RESET} ")
            decoded_data = decode_base64(encoded_data)
            print(f"   {ITALIC_GREEN}Decoded (Base64):{RESET}  {decoded_data}")
            print(f"   {ITALIC_GREEN}Done Buddy 💻 💻 {RESET}")
        
        elif choice == 3:
            data = input(f"   \n{GOLD}Enter the text to encode to Base32 <3 {RESET} ")
            encoded_data = encode_base32(data)
            print(f"   {ITALIC_GREEN}Encoded (Base32):{RESET} {encoded_data}")
            print(f"   {ITALIC_GREEN}Done Buddy 💻 💻 {RESET}")
        
        elif choice == 4:
            encoded_data = input(f"   {GOLD}Enter the Base32 string to decode <3 {RESET} ")
            decoded_data = decode_base32(encoded_data)
            print(f"   {ITALIC_GREEN}Decoded (Base32):{RESET} {decoded_data}")
            print(f"   {ITALIC_GREEN}Done Buddy 💻 💻 {RESET}")
        
        elif choice == 5:
            print(f"\n   {ITALIC_GREEN}Returning to main menu...{RESET}\n")
            time.sleep(2)  # Wait for 2 seconds
            return  # This will exit the cryptography_x64 function and return to the main menu
                
        else:
            print(f"\n{LIGHT_GREEN}Invalid choice! Please enter 1, 2, 3, or 4.{RESET}")
        input(f"\n\n   {LIGHT_CYAN_BOLD}Press{RESET} <{ITALIC_RED}Enter{RESET}> {LIGHT_CYAN_BOLD}to return to the menu if you got your result...... {RESET}")
    except ValueError:
        print(f"\n       {ITALIC_RED}Invalid input! Please enter a valid number. ⚠️ {RESET}")
