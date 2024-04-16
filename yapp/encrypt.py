# This file initialize required keys for AES, DES and RSA. It should only be run once.

import click
import os

from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

from yapp.encryptions.aes import *
from yapp.encryptions.des import *
from yapp.encryptions.rsa import *

@click.command("init-keys")
def init_keys_command():
    try:
        os.makedirs("./yapp/.keys")
    except OSError:
        pass
    
    with open("./yapp/.keys/aes-key", "wb") as f:
        f.write(get_random_bytes(16))
        click.echo("Generated AES key.")
    with open("./yapp/.keys/des-key", "wb") as f:
        f.write(get_random_bytes(8))
        click.echo("Generated DES key.")
    private_key = RSA.generate(2048)
    with open("./yapp/.keys/private-rsa-key.pem", "wb") as f:
        f.write(private_key.exportKey())
        click.echo("Generated private RSA key.")
    with open("./yapp/.keys/public-rsa-key.pem", "wb") as f:
        f.write(private_key.publickey().exportKey())
        click.echo("Generated public RSA key.")


def init_app(app):
    app.cli.add_command(init_keys_command)


def encrypt_with_option(plaintext, option):
    match option:
        case "aes":
            return aes_encrypt(plaintext)
        case "des":
            return des_encrypt(plaintext)
        case "rsa":
            return rsa_encrypt(plaintext)
        case _:
            raise ValueError(f"unknown option: {option}")


def decrypt_with_option(ciphertext, option):
    match option:
        case "aes":
            return aes_decrypt(ciphertext)
        case "des":
            return des_decrypt(ciphertext)
        case "rsa":
            return rsa_decrypt(ciphertext)
        case _:
            raise ValueError(f"unknown option: {option}")

