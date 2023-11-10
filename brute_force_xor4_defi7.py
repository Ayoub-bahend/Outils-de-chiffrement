# !/bin/python3

import random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

KEY_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
MESSAGE_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "


def chiffrement_xor(plaintext, key):
    sortie = []
    for i in range(len(plaintext)):
        sortie.append(chr(ord(plaintext[i]) ^ ord(key[i % len(key)])))
    return ''.join(sortie)


def chiffrement_xor_bytes(plaintext, key):
    sortie = []
    for i in range(len(plaintext)):
        sortie.append(plaintext[i] ^ key[i % len(key)])
    return bytes(sortie)


def salt(plaintext, compteur, salt):
    return str(compteur) + plaintext + salt


def reduceAlphabet(cipherText, lettre):
    reducedAlphabet = []
    print(chiffrement_xor(cipherText[i], lettre))
    if all(chiffrement_xor(cipherText[i], lettre) in KEY_ALPHABET for i in range(len(cipherText))):
        reducedAlphabet.append(lettre)

    return reducedAlphabet


def contains4digits(plaintext):
    for i in range(0, len(plaintext) - 4):
        if plaintext[i:i + 4].isdigit():
            return True
    return False


def bruteForce(cipherText):
    keyRange = [*range(65, 91)]  # A-Z
    keyRange += [*range(97, 123)]  # a-z
    keyRange += [*range(48, 50)]  # 0-9
    for xor_key1 in keyRange:  # (32, 127) for the printable ASCII characters, (65, 90) for the uppercase letters
        for xor_key2 in keyRange:
            for xor_key3 in keyRange:
                for xor_key4 in keyRange:
                    key = bytes([xor_key1, xor_key2, xor_key3, xor_key4])  # 4 bytes key
                    # print(key)
                    decoded = chiffrement_xor_bytes(cipherText, key)  # decode the cipher text using the current key
                    # if all bytes are printable and the payload is in the decoded text
                    # if all bytes decoded are in ALPHABET + "1234567890"
                    if ("ON" in decoded.decode() or "OFF" in decoded.decode()) and all(
                            chr(decoded[i]) in MESSAGE_ALPHABET for i in range(len(decoded))):
                        print("Found possible key: " + key.decode() + " => " + decoded.decode())
                        return


if __name__ == "__main__":

    for i in range(1):
        ciphertext = "NDdIT0RCX1g4JSo3NDcrNz43UTNGPys3"
        ciphertext = base64.b64decode(ciphertext)
        bruteForce(ciphertext)





    