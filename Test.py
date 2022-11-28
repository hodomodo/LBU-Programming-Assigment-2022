
password = input("Please enter a new password: ")
if len(password) > 0:
    def password_checker(password_1):
        from string import ascii_letters as letters, digits, punctuation

        has_letter = has_digit = has_punc = False

        for character in password:
            if character in letters:
                has_letter = True
            elif character in digits:
                has_digit = True
            elif character in punctuation:
                has_punc = True
                return has_letter and has_digit and has_punc

        if has_letter is True and has_digit is True and has_punc is True:
            print("This password is acceptable")
        else:
            print("This password is unacceptable")


password_checker(password)

