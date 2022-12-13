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
                decryption.replace("\n", "")
                decryption.replace(".", "")
                decrypted_list = ",".join(decryption).replace(",", "").split(" ")
                decrypted_list = [s.replace('"', "") for s in decrypted_list]
                check_1 = decrypted_list[0]
                decryption_1 = " ".join(decrypted_list)
                if checker.check(check_1) == True:
                    print(decryption_1, end="")
                    for line in f:
                        decryption = decrypt(line)
                        decryption.replace("\n", "")
                        decryption.replace(".", "")
                        decrypted_list = ",".join(decryption).replace(",", "").split(" ")
                        decrypted_list = [s.replace('"', "") for s in decrypted_list]
                        check_1 = decrypted_list[0]
                        decryption_1 = " ".join(decrypted_list)
                        print(decryption_1, end="")
                else:
                    print("Most likely not a caesar cypher at work here")
                    quit()
    else:
        print("File could not be found")
        quit()
else:
    print("Please provide a text file to be decrypted")
    quit()