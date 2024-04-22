import matplotlib.pyplot as plt

from accuracy import dest_file

from encryptions.aes import aes_decrypt
from encryptions.des import des_decrypt
from encryptions.rsa import rsa_decrypt

if __name__ == "__main__":
    encrypt_functions = (aes_decrypt, des_decrypt, rsa_decrypt)
    func_names = [func.__name__[:3] for func in encrypt_functions]
    success_rates = []

    for func in encrypt_functions:
        with open(dest_file(func), "r") as f:
            lines = f.readlines()
            outcomes = [l for l in lines if l != "\n"]
        success = [o for o in outcomes if o == "Success\n"]
        success_rate = len(success) / len(lines) * 100
        success_rates.append(success_rate)
    
    plt.bar(func_names, success_rates)
    plt.xlabel("Encryption techniques")
    plt.ylabel("Success rate (%)")
    plt.show()
