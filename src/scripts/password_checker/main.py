"""
This script checks if and how many times a password has been leaked.
Run it in the root of the project using:
python src/scripts/password_checker/main.py

The script sends only the first five characters of the password to
pwned api. Then it receives all leaked password whose hashes start
with those characters and uses this response locally to check if input password
has been leaked. It never sends your entire password on the internet.
"""

import requests
import hashlib
import getpass


# The pwned API receives the first five characters of an SHA-1 hash and
# returns all leaked password whose hashes start with those characters.
def request_api_data(hash_password):
    url = "https://api.pwnedpasswords.com/range/" + hash_password
    response = requests.get(url)
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


# Hashes the password, call the pwned api, run and return leaks count
def check_password(password):
    # hashing password in Sha-1
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)  # Response->"hash: count, hash: count etc"
    return get_password_leaks_count(response, tail)


if __name__ == "__main__":
    password = getpass.getpass("Enter password: ")
    count = check_password(password)
    if count:
        print(f"{password} was found {count} times. You should change it")
    else:
        print(f"{password} was not found. You are safe!")
