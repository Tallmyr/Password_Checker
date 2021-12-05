import hashlib
import re
from typing import Optional

import requests


def hash_password(password: str) -> str:
    """Take password input, hash, convert to text and make upper case"""
    return hashlib.sha1(password.encode()).hexdigest().upper()


def check_password(hash: str) -> Optional[int]:
    """Takes a hashed string,
    split and send to pwnedpasswords
    and return an int or None"""

    front = hash[:5]  # First 5 letters
    back = hash[5:]  # rest of string

    # request the list of hashes
    pwlist = requests.get("https://api.pwnedpasswords.com/range/" + front)
    regex = r"{}:([0-9]*)".format(back)  # build regex
    result = re.search(regex, pwlist.text)

    if result is not None:  # If nothing found result is None
        return result.group(1)
