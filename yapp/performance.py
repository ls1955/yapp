import os.path as path
import time

from encryptions.aes import aes_encrypt

def record_performance(func):
    """
    Records the time taken (in seconds) taken to complete the function.
    It will append the recorded time into `data/<encryption>_perf.txt`.
    """
    def wrapper(arg):
        init_time = time.time()
        result = func(arg)
        runtime = time.time() - init_time

        write_time_to_file(func.__name__, runtime)

        return result
    return wrapper


base_path = path.dirname(__file__)


def write_time_to_file(func_name, runtime):
    dest = path.abspath(path.join(base_path, "data", f"{func_name}_perf.txt"))

    with open(dest, "a") as f:
        f.write(runtime)
        f.write("\n")


if __name__ == "__main__":
    usernames_file = path.abspath(path.join(base_path, "data", "usernames.txt"))
    with open(usernames_file, "r") as f:
        usernames = f.readlines()
    print(len(usernames))
    passwords_file = path.abspath(path.join(base_path, "data", "passwords.txt"))
    with open(passwords_file, "r") as f:
        passwords = f.readlines()
    print(len(passwords))
