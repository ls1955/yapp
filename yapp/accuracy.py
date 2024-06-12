import os
import os.path as path
import time

from yapp.encryptions.aes import aes_encrypt, aes_decrypt
from yapp.encryptions.des import des_encrypt, des_decrypt
from yapp.encryptions.rsa import rsa_encrypt, rsa_decrypt


def record_accuracy(encrypt_func, decrypt_func):
    """
    Records the output (Success or Fail) after decrypting password.
    It will append the recorded time into `accuracy/<encryption_function_name>.txt`.
    """
    def wrapper(plaintext):
        encrypted = encrypt_func(plaintext).decode("latin-1")
        result = str(decrypt_func(encrypted.encode("latin-1")))

        is_success = result == plaintext
        write_outcome_to_file(decrypt_func, is_success)

        return result
    return wrapper


base_path = path.dirname(__file__)


def write_outcome_to_file(func, is_success):
    if not os.path.exists(dest_file(func)):
        with open(dest_file(func), "w") as f:
            pass
    with open(dest_file(func), "a") as f:
        f.write(f"{'Success' if is_success else 'Fail'}\n")


def dest_file(func):
    return path.abspath(path.join(base_path, "data", "accuracy", f"{func.__name__}.txt"))


if __name__ == "__main__":
    usernames_file = path.abspath(path.join(base_path, "data", "usernames.txt"))
    with open(usernames_file, "r") as f:
        usernames = f.readlines()
    assert usernames, "usernames.txt is empty."

    passwords_file = path.abspath(path.join(base_path, "data", "passwords.txt"))
    with open(passwords_file, "r") as f:
        passwords = f.readlines()
    assert passwords, "passwords.txt is empty."

    assert len(usernames) == len(passwords), "usernames and passwords should have same length."

    for encrypt_func, decrypt_func in [(aes_encrypt, aes_decrypt), (des_encrypt, des_decrypt), (rsa_encrypt, rsa_decrypt)]:
        try:
            os.makedirs(path.abspath(path.join(base_path, "data", "accuracy")))
        except OSError:
            pass
        # clear previous recorded performance
        try:
            os.remove(dest_file(decrypt_func))
        except FileNotFoundError:
            pass

        for password in passwords:
            record_accuracy(encrypt_func, decrypt_func)(password)
