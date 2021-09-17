from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64decode,b64encode

import argparse

parser = argparse.ArgumentParser(description='rsa encryption/decryption')
parser.add_argument("-P", "--privkey", help="Priv Key file path", required=False, default="")
parser.add_argument("-p", "--pubkey", help="Pub Key file path", required=False, default="")
parser.add_argument("--text", help="Text to encrypt or decrypt", default="hello world")
parser.add_argument("-e", "--encrypt", help="Whether to encrypt or not", nargs='?', const="public", choices=["", "public", "private"], default="")
parser.add_argument("-d", "--decrypt", help="Whether to decrypt or not", nargs='?', const="private", choices=["", "public", "private"], default="")
parser.add_argument("--debug", help="Debug flag", action="store_true", default=False)

args = parser.parse_args()

if not args.encrypt and not args.decrypt:
    parser.error("requires either --encrypt or --decrypt")

if args.privkey:
    privkey = open(args.privkey, "r").read()
if args.pubkey:
    pubkey = open(args.pubkey, "r").read()

if args.debug:
    print("privatekey", privkey, "\n", "publickey", pubkey)
    print("privatekey", privkey, "\n", "publickey", pubkey)

enc = dec = None
if args.encrypt == "public":
    enc = Cipher_PKCS1_v1_5.new(RSA.importKey(pubkey))
if args.encrypt == "private":
    enc = Cipher_PKCS1_v1_5.new(RSA.importKey(privkey))

if args.decrypt == "public":
    dec = Cipher_PKCS1_v1_5.new(RSA.importKey(pubkey))
if args.decrypt == "private":
    dec = Cipher_PKCS1_v1_5.new(RSA.importKey(privkey))

encrypted = ""
if args.encrypt:
    encrypted = b64encode(enc.encrypt(args.text.encode()))
    print(encrypted.decode())

if args.decrypt and not args.encrypt:
    uncrypted = dec.decrypt(b64decode(args.text), None).decode()
    print(uncrypted)

if args.decrypt and args.encrypt:
    uncrypted = dec.decrypt(b64decode(encrypted), None).decode()
    print(uncrypted)

