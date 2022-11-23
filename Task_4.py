import fileinput
import enchant

e = enchant.Dict("en_UK")

alphabet = "nopqrstuvwxyzabcdefghijklm"

for f in fileinput.input():
    def decrypt(text):
        text = text.lower()

        result = ''

        for char in text:
            if char.isalpha():
                result += alphabet[(alphabet.index(char) - 14) % 26]

            else:
                result += char

        return result

decryption_check = e.check(f)
print(f)
print(decryption_check)

if decryption_check is True:
    print(decrypt(f))
elif decryption_check is False:
    print("Cannot decrypt. Most likely not a Caesar Cypher at work here")

