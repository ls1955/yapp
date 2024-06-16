import os
import os.path as path
import time

try:
    from encryptions.aes import aes_encrypt, aes_decrypt
    from encryptions.des import des_encrypt, des_decrypt
    from encryptions.rsa import rsa_encrypt, rsa_decrypt
except ModuleNotFoundError:
    from yapp.encryptions.aes import aes_encrypt, aes_decrypt
    from yapp.encryptions.des import des_encrypt, des_decrypt
    from yapp.encryptions.rsa import rsa_encrypt, rsa_decrypt


base_path = path.dirname(__file__)


def write_outcome_to_file(func, is_success):
    if not os.path.exists(dest_file(func)):
        with open(dest_file(func), "w") as f:
            pass
    with open(dest_file(func), "a") as f:
        f.write(f"{'Success' if is_success else 'Fail'}\n")


def dest_file(func):
    if isinstance(func, str):
        return path.abspath(path.join(base_path, "data", "accuracy", f"{func}_decrypt.txt"))
    return path.abspath(path.join(base_path, "data", "accuracy", f"{func.__name__}.txt"))
