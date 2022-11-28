import enchant
import sys
import os.path


checker = enchant.Dict("en_UK")

alphabet = "nopqrstuvwxyzabcdefghijklm"

decrypted_list = []


def decrypt(text):
    text = text.lower()

    result = ''

    for char in text:
        if char.isalpha():
            result += alphabet[(alphabet.index(char) - 14) % 26]

        else:
            result += char

    return result


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as f:
            for line in f:
                decryption = decrypt(line)
                decrypted_list = ",".join(decrypt(line)).replace(",", "").split(" ")
                check_1 = decrypted_list[0]
                if checker.check(check_1) == False:
                    print("Most likely not a caesar cypher at work here")
                    quit()
                elif checker.check(check_1) == True:
                    print(decryption, end="")