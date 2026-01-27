import os
from cryptography.fernet import Fernet

EXTENSION = ".LOCKED"

def get_desktop_path():
    home = os.environ.get('USERPROFILE')
    paths = [
        os.path.join(home, 'Desktop'),
        os.path.join(home, 'OneDrive', 'Desktop')
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return None

def manual_decrypt():
    print("--- MASTERLock Manual Recovery Tool ---")
    desktop = get_desktop_path()
    
    if not desktop:
        print("Error: Could not find Desktop folder.")
        return

    key_input = input("Enter your Recovery Key: ").strip().encode()
    
    try:
        f = Fernet(key_input)
        count = 0
        
        for root, dirs, files in os.walk(desktop):
            for name in files:
                if name.endswith(EXTENSION):
                    filepath = os.path.join(root, name)
                    original_path = filepath.replace(EXTENSION, "")
                    
                    try:
                        with open(filepath, "rb") as _file:
                            data = _file.read()
                        
                        decrypted_data = f.decrypt(data)
                        
                        with open(original_path, "wb") as _file:
                            _file.write(decrypted_data)
                        
                        os.remove(filepath)
                        count += 1
                        print(f"[OK] Restored: {name}")
                    except Exception:
                        print(f"[FAIL] Could not decrypt {name}")
        
        print(f"\nFinished! {count} files restored.")
        
    except Exception:
        print("ERROR: Invalid Key Format.")

if __name__ == "__main__":
    manual_decrypt()
    input("\nPress Enter to exit...")