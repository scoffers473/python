#!/usr/bin/env python3

import json
import boto3
import base64
import os
from botocore.exceptions import ClientError
import urllib3
from cryptography.fernet import Fernet


# Deefine the outfile
jsonFile="backup.json"
keyFile="key.key"

from cryptography.fernet import Fernet

def decrypt_file(filename, key):
    # Given a filename (str) and key (bytes), it decrypts the file and writes it
    f = Fernet(key)
    with open(filename, "rb") as file:
        # Read the encrypted data
        encrypted_data = file.read()
    # Decrypt data
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Invalid key - unable to decrypt file.")
        return
    # Write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def readKey(keyFile):
    with open(keyFile, "rb") as kF:
        key=kF.read()
    return(key)

def main ():
    key=readKey(keyFile)
    decrypt_file(jsonFile,key)

if __name__ == '__main__':
    main()

