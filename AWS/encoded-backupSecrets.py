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

def getSecrets():
    secretDict = {}
    tagDict = {}
    secretsArray = []
    region_name = "eu-west-1"
    secrets = []
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
        )
    client = session.client('secretsmanager')
    response = client.list_secrets()
    secrets.extend(response['SecretList'])
    while 'NextToken' in response:
        response = client.list_secrets(NextToken=response['NextToken'])
        secrets.extend(response['SecretList'])
    for secret in secrets:
        tagList=secret['Tags']
        tagDict = {}
        decodedDict={}
        secretDict = {}

        # Generate a list of tags for the secret
        for tag in tagList:
          tagDict.update({tag["Key"]:tag["Value"]})
        
        # Get the decoded secret as a JSON string
        decodedSecret = decodeSecret(secret['Name'])

        # Now convert the JSON to a dict
        decodedDict=json.loads(decodedSecret)

        # Finally generate a full dict of the resuts
        try:
            secretDict.update({"Name":secret["Name"],"Description":secret["Description"],"secrets":decodedDict,"tags":tagDict})
        except:
            secretDict.update({"Name":secret["Name"],"Description":"No_Description","secrets":decodedDict,"tags":tagDict})
        secretsArray.append(secretDict)

    return secretsArray

def decodeSecret(secret_name):
    region_name = "eu-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        print (e.response)
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS key.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return decoded_binary_secret



def writeEncryptedData(data, file_name, key=None):
    """
    Encrypts a dictionary and writes the encrypted data to a file.
    :param data: dictionary to encrypt
    :param file_name: name of the file to write the encrypted data to
    :param key: encryption key, if not provided a new key will be generated
    :return: encryption key
    """
    if not key:
        key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    with open(file_name, 'wb') as f:
        json_data = json.dumps(data)
        encrypted_text = cipher_suite.encrypt(json_data.encode())
        f.write(encrypted_text)
    return key

def writeKey(key):
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)


def main ():
    secretsArray = getSecrets ()
    key=writeEncryptedData(secretsArray,jsonFile)
    writeKey (key)


if __name__ == '__main__':
    main()

