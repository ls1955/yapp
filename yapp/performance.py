import os
import os.path as path
import time

try:
    from encryptions.aes import aes_encrypt
    from encryptions.des import des_encrypt
    from encryptions.rsa import rsa_encrypt
except ModuleNotFoundError:
    from yapp.encryptions.aes import aes_encrypt
    from yapp.encryptions.des import des_encrypt
    from yapp.encryptions.rsa import rsa_encrypt

base_path = path.dirname(__file__)


def write_time_to_file(func, runtime):
    print(func, runtime)
    with open(dest_file(func), "a") as f:
        # round runtime to 5 decimal place
        f.write(f"{runtime:.5f}\n")


def dest_file(func):
    if isinstance(func, str):
        return path.abspath(path.join(base_path, "data", "perf", f"{func.lower()}_encrypt.txt"))
    return path.abspath(path.join(base_path, "data", "perf", f"{func.__name__}.txt"))
