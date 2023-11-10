#!/bin/python3

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

KEY_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
MESSAGE_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def chiffrement_xor_bytes(plaintext, key):
    sortie = []
    for i in range(len(plaintext)):
        sortie.append(plaintext[i] ^ key[i % len(key)])
    return bytes(sortie)


def DecodeAES_ECB(tabMessage, tabKey):
    """ Dechiffrement AES ECB de tabMessage. La clef tabKey est un tableau de 16 éléments.
        Retourne un tableau d'octets. Les caractères espace en fin de
        tableau sont supprimés."""
    cipher = Cipher(algorithms.AES(bytearray(tabKey)), modes.ECB())
    decryptor = cipher.decryptor()
    return decryptor.update(tabMessage).strip()


def contains4digits(plaintext):
    for i in range(0, len(plaintext)-4):
        if plaintext[i:i+4].isdigit():
            return True
    return False



def attackXOR(cipherText, dict_file):
    file = open(dict_file, "r", encoding="ISO-8859-1")
    for line in file:
        if line != "\n":
            try:
                decoded = chiffrement_xor_bytes(cipherText, bytes(line.strip(), 'UTF-8'))
                if all (chr(decoded[i]) in MESSAGE_ALPHABET for i in range(len(decoded))) and ("ON" in decoded.decode() or "OFF" in decoded.decode()):
                    print(line.strip())
                    print(decoded.decode('UTF-8'))
            except:
                pass



def attackAES(cipherText, dict_file, nb_tours):
    file = open(dict_file, "r", encoding="ISO-8859-1")
    for line in file:
        try:
            if line != "\n":
                decoded = cipherText
                for j in range(nb_tours):
                    decoded = DecodeAES_ECB(decoded, bytes(line.strip(), 'UTF-8'))
                    if ("ON" in decoded.decode() or "OFF" in decoded.decode()):
                        print(line.strip())
                        print(decoded.decode('UTF-8'))
        except:
            pass

if __name__ == "__main__":
    message = "LC1SUVBXAhkGERcaFgo="
    message = base64.b64decode(message)

    #attackAES(message, "rockyou.txt", 4)
    #attackXOR(message, "test.txt")