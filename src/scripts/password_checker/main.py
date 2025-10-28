import requests
import hashlib


# This API receives the first five characters of an SHA-1 hash and
# returns all leaked passwords whose hashes start with those characters.
def request_api_data(hash_password):
    url = "https://api.pwnedpasswords.com/range/" + hash_password
    response = requests.get(url)
    print(response)
    if response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code}")
    return response


def read_res(response):
    print(response.text)


# Check if password exists in pwned database
def check_password(password):
    # Encoding plain password in Sha-1
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return read_res(response)


check_password("password123")
