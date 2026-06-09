#Password Strength Checker

import re  #search a special charachter

#pass strength check conditions:

def check_password_strength(password):
    if len(password) < 8: #'length of password'
        return "Weak: password must at least 8 chars"
      
    if not any(char.isdigit() for char in password):
        return "Weak: password mudt contain a digit"
    
    if not any(char.isupper() for char in password):
        return "Weak: password mudt contain an upper char"
    
    if not any(char.islower() for char in password):
        return "Weak: password mudt contain a lower char"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: password must contain a special character"
    
    return "Strong: Your Password is secured!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter Your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank you for using this tool")
            break
        result = check_password_strength(password)

        print(result)


if __name__ == "__main__":
    password_checker()


    



    
    
