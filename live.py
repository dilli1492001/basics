import string
password = input("enter your password : ")
def valid_password(password):
    is_uppercase = False
    is_lowercase = False
    is_number = False
    is_special = False
    for character in password:
        if character.isupper():
            is_uppercase = True
        elif character.islower():
            is_lowercase = True
        elif character.isdigit():
            is_number = True
        elif character in string.punctuation():
            is_special = True
    return is_special and is_uppercase and is_lowercase and is_number
result = valid_password(password)
if result:
    print("strong password!")
else:
    print("weak password!")
        
