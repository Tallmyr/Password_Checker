import requests
import hashlib
import re
from distutils.util import strtobool
from getpass import getpass


def Main():
    loop = True
    print("Welcome to Password Checker")
    while loop:
        hash = hash_password(getpass("Enter Password to test: "))
        result = checkpassword(hash)
        print(result)
        loop = strtobool(
            input(
                "Do you wish to test another password? " "[Yes, y] / [No, n] "
            ).lower()
        )


def hash_password(password: str):
    return hashlib.sha1(password.encode()).hexdigest().upper()


def checkpassword(hash: str):
    # Take password input, hash, convert to text and make upper case
    front = hash[:5]  # First 5 letters
    back = hash[5:]  # rest of string

    # request the list of hashes
    pwlist = requests.get("https://api.pwnedpasswords.com/range/" + front)
    regex = r"{}:([0-9]*)".format(back)  # build regex
    result = re.search(regex, pwlist.text)

    if result is not None:  # If nothing found result is None
        return result.group(1)
    else:
        return None



if __name__ == "__main__":
    Main()
