"""
This script checks if and how many times a variable number of passwords has been leaked.
Run it in the root of the project using:
python src/scripts/password_checker/main.py {password} {passwrd} ...

The script sends only the first five characters of each password to
pwned api. Then it receives all leaked password whose hashes start
with those characters and uses this response locally to check if input password
has been leaked. It never sends your entire password on the internet.
"""

import requests
import hashlib
import sys


# This API receives the first five characters of an SHA-1 hash and
# returns all leaked password hashes whose hashes start with those characters.
def request_api_data(hash_password):
    url = "https://api.pwnedpasswords.com/range/" + hash_password
    response = requests.get(url)
    print(response)
    if response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code}")
    return response


# Check if and how many times a password has been leaked
def get_password_leaks_count(hashes, tail_hash_to_check):
    # Split hashes in hash | count, hash | count
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == tail_hash_to_check:
            return count
    return 0


# Check if password exists in pwned database
def check_password(password):
    # Encoding plain password in Sha-1
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)  # Response->"hash: count, hash: count etc"
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = check_password(password)
        if count:
            print(f"{password} was found {count} times. You should change it")
        else:
            print(f"{password} was not found. You are safe!")
    return "Password leak checked!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))  # take 1 or more arguments.
    # sys.exit stops the program and passes the return value of main() as the process exit code
    # to the operative system.
