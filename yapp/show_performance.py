import matplotlib.pyplot as plt

from performance import dest_file

from encryptions.aes import aes_encrypt
from encryptions.des import des_encrypt
from encryptions.rsa import rsa_encrypt

if __name__ == "__main__":
    encrypt_functions = (aes_encrypt, des_encrypt, rsa_encrypt)
    func_names = [func.__name__[:3] for func in encrypt_functions]
    averages = []

    for func in encrypt_functions:
        with open(dest_file(func), "r") as f:
            runtimes = [float(l) for l in f.readlines() if l != "\n"]
        avg = sum(runtimes) / len(runtimes)
        averages.append(avg)
    
    plt.bar(func_names, averages)
    plt.xlabel("Encryption techniques")
    plt.ylabel("Average runtime")
    plt.show()
