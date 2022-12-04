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
                decrypted_list = [s.replace('"', "") for s in decrypted_list]
                check_1 = decrypted_list[0]
                decryption_1 = " ".join(decrypted_list)
                print(checker.check(check_1))
                if checker.check(check_1) == True or "\n" or '"' in check_1:
                    print(decryption_1, end="")
                elif checker.check(check_1) == False or "\n" not in check_1:
                    print("Most likely not a caesar cypher at work here")
                    quit()
