from random import randint, shuffle
import os
import sys
import glob

original_alphabet = "abcdefghijklmnopqrstuvwxyz"

if not os.path.exists("keys"):
    os.mkdir("keys")

key_type = input(
    "would you like to use (1) a random key or (2) the reversed key? ")


def swap(original_key, modified_key):
    choice = input("would you like to (e) encode or (d) decode a string? ")
    new_string = ""
    string = ""
    if choice in ("d", "decode"):
        string = input("what string do you want to decode? ").lower()
        for char in string:
            try:
                new_string += original_key[modified_key.index(char)]
            except ValueError:
                new_string += char
    elif choice in ("e", "encode"):
        string = input("what string do you want to encode? ").lower()
        for char in string:
            try:
                new_string += modified_key[original_key.index(char)]
            except ValueError:
                new_string += char
    return string, new_string


if key_type == "1":
    choice = input(
        "would you like to (l) load an existing random key, or (c) create a new one? ").lower()
    if choice == "c":
        original_alphabet_list = [char for char in original_alphabet]
        shuffle(original_alphabet_list)
        new_alphabet = "".join(original_alphabet_list)
        string = input("what would you like to encode? ").lower()
        encoded_string = ""
        for char in string:
            try:
                encoded_string += new_alphabet[original_alphabet.index(
                    char)]
            except ValueError:
                encoded_string += char
        print("successfully encoded '{}' to '{}'".format(string, encoded_string))
        choice = input("(y/n) would you like to save this key? ").lower()
        if choice in ("yes", "y"):
            next_num = len(glob.glob("keys/random*.key")) + 1
            with open("keys/random%i.key" % next_num, "w") as f:
                f.write(new_alphabet)
                print("saved to 'keys/random%i.key" % next_num)
    elif choice in ("l", "load"):
        total_rnd_keys = len(glob.glob("keys/random*.key"))
        if total_rnd_keys == 0:
            print("no random keys have been created!")
            sys.exit()
        elif total_rnd_keys == 1:
            choice = input("(y/n) use the one existing key? ").lower()
            if choice in ("y", "yes"):
                with open("keys/random1.key") as f:
                    key = f.read().replace("\n", "")
                    swap(original_alphabet, key)
        else:
            key_num = input("type a number from 1 to %i: " % total_rnd_keys)
            if os.path.exists("keys/random%s.key" % key_num):
                with open("keys/random%s.key" % key_num) as f:
                    modified_key = f.read().removesuffix("\n")
                    old_string, new_string = swap(
                        original_alphabet, modified_key)
                    print("\nold:", old_string)
                    print("new:", new_string)
elif key_type == "2":
    reversed_alphabet = "".join(reversed(original_alphabet))
    old_string, new_string = swap(original_alphabet, reversed_alphabet)
    print("\nold:", old_string)
    print("new:", new_string)

print("\nexiting!")
