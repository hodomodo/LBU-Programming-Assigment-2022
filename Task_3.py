import fileinput
import random
import sys
import os.path

n = open("Student_Emails.txt", "w")

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as f:
            for line in f:
                rand_num = random.randint(1000, 9999)
                file = line
                id = file[0:8]
                names_start = file[9:99]
                names = names_start.split(", ")
                length = len(names)
                first_name = names[0]
                last_name = names[-1]
                last_name = str(last_name)
                initials = [char for char in first_name if char.isupper()]
                caps = sum(1 for c in initials if c.isupper())
                if caps > 1:
                    initials.insert(1, ".")
                    initials.insert(3, ".")
                    initials = str(initials)
                else:
                    initials.insert(1, ".")
                    initials = str(initials)
                initials = initials.replace("-", "")
                initials = initials.replace("'", "")
                initials = initials.replace("[", "")
                initials = initials.replace("]", "")
                initials = initials.lower()
                last_name = last_name.replace(" ", "")
                last_name = last_name.replace("-", "")
                last_name = last_name.replace("'", "")
                last_name = last_name.replace("[", "")
                last_name = last_name.replace("]", "")
                last_name = last_name.lower()
                id = str(id)
                emails = initials, last_name, rand_num, "@poppleton.ac.uk"
                emails = str(emails)
                emails = emails.replace(" ", "")
                emails = emails.replace(" ", "")
                emails = emails.replace("-", "")
                emails = emails.replace("'", "")
                emails = emails.replace(")", "")
                emails = emails.replace("(", "")
                emails = emails.replace(",", "")
                final = id, emails
                final = str(final)
                final = final.replace("'", "")
                final = final.replace(")", "")
                final = final.replace("(", "")
                final = final.replace(",", "")
                final = final.replace(r"\\n", "")
                n.write(final)
                n.write("\n")
            n.close
    else:
        print("Error:", sys.argv[1], "does not exist")
else:
    print("Error: Missing command-line  argument.")

