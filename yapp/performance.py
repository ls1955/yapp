import os
import os.path as path
import time

from encryptions.aes import aes_encrypt
from encryptions.des import des_encrypt
from encryptions.rsa import rsa_encrypt


def record_performance(encrypt_function):
    """
    Records the time taken (in seconds) taken to complete the function.
    It will append the recorded time into `perf/<encryption_function_name>.txt`.
    """
    def wrapper(plaintext):
        init_time = time.time()
        result = encrypt_function(plaintext)
        runtime = time.time() - init_time

        write_time_to_file(encrypt_function, runtime)

        return result
    return wrapper


base_path = path.dirname(__file__)


def write_time_to_file(func, runtime):
    with open(dest_file(func), "a") as f:
        # round runtime to 5 decimal place
        f.write(f"{runtime:.5f}\n")


def dest_file(func):
    return path.abspath(path.join(base_path, "data", "perf", f"{func.__name__}.txt"))


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

    for func in [aes_encrypt, des_encrypt, rsa_encrypt]:
        try:
            os.makedirs(path.abspath(path.join(base_path, "perf")))
        except OSError:
            pass
        # clear previous recorded performance
        try:
            os.remove(dest_file(func))
        except FileNotFoundError:
            pass

        for password in passwords:
            record_performance(func)(password)
