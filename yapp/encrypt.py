# This file initialize required keys for AES, DES and RSA. It should only be run once.

import click
import os

from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

@click.command("init-keys")
def init_keys_command():
    try:
        os.makedirs(".keys")
    except OSError:
        pass
    
    with open(".keys/aes-key", "wb") as f:
        f.write(get_random_bytes(16))
        click.echo("Generated AES key.")
    with open(".keys/des-key", "wb") as f:
        f.write(get_random_bytes(8))
        click.echo("Generated DES key.")
    with open(".keys/rsa-key", "wb") as f:
        f.write(RSA.generate(2048).publickey().exportKey(format="DER"))
        click.echo("Generated RSA key")


def init_app(app):
    app.cli.add_command(init_keys_command)

