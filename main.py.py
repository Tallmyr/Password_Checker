from distutils.util import strtobool
from getpass import getpass
from password_checker import hash_password, check_password


def Main():
    """Run Terminal version of Password Checker"""
    loop = True
    print("Welcome to Password Checker")
    while loop:
        hash = hash_password(getpass("Enter Password to test: "))
        result = check_password(hash)
        print_output(result)
        loop = strtobool(
            input(
                "Do you wish to test another password? " "[Yes, y] / [No, n] "
            ).lower()
        )


def print_output(result: int):
    """Print result to console. Accepts an int or None"""
    if result is not None:
        print(f"WARNING: Your password was found {result} times!")
    else:
        print("Your Password was not found, that is great news!")


if __name__ == "__main__":
    Main()
