import random
import string
limit_long = 30
all_chars = string.ascii_letters + string.digits + string.punctuation
all_chars_sp = all_chars + " "
print("Infos: This programme designed for generate a strong password, save passwords, remove passwords and view saved passwords")
print("More info: You can back from any service via enter 'back'")
print("           You can't name a passaword private word like 'back'")
print("1/ Generite password")
print("2/ Save password")
print("3/ Remove password")
print("4/ View saved password")
print("5/ Exit")
while True:
    opr = input("Who is service you want (select the service via his number): ")
    if opr == "1":
        while True:
            pass_long = input("Enter the long of the password: ").lower()
            if pass_long == "back":
                break
            else:
                try:
                    pass_long = int(pass_long)
                except ValueError:
                    print("Invalid input: Use integer numbers only in this operation")
                    continue
                if pass_long > 0 and pass_long <= limit_long:
                    while True:
                        space = input("Do you want the spaces in your password (Some apps, webs, ... don't support spaces in your password) (Yes/No): ").lower()
                        password = ""
                        if space == "back":
                                break
                        else:
                            if space == "yes":
                                use_chars = all_chars_sp
                            elif space == "no":
                                use_chars = all_chars
                            else:
                                print("Invalid input: Enter 'yes' or 'no' only")
                                continue
                            for i in range(pass_long):
                                password += random.choice(use_chars)
                            print("Congratulation, the password is generated")
                            print(f"the password is: {password}")
                            break
                elif pass_long > limit_long:
                    print(f"Invalid input: My limite is generete a password have a {limit_long} character in maximum")
                    continue
                else:
                    print("Invalid input: This long is not available")
                    continue
                break
    elif opr == "2":
        while True:
            name_pass_a = input("Enter a name of the password: ")
            if name_pass_a.lower() == "back":
                break
            else:
                with open("passwords.txt", "r") as f:
                    exist = False
                    lines = f.readlines()
                    for line in lines:
                        name_pass = line.split(":")[0].strip()
                        if name_pass == name_pass_a:
                            exist = True
                            break
                        else:
                            continue
                if exist == False:
                    while True:
                        back = False
                        password = input("Enter the password: ")
                        if password.lower() == "back":
                            back = True
                            break
                        else:
                            with open("passwords.txt", "r") as f:
                                file = f.read()
                            with open("passwords.txt", "w") as f:
                                if file == "":
                                    f.write(f"{name_pass_a}: {password}")
                                else:
                                    f.write(f"{name_pass_a}: {password}\n" + file)
                            print("Congratulation, the password is saved")
                            break
                else:
                    print("This name is already used, chose another one")
                    continue
            if back == False:
                break
            else:
                continue
    elif opr == "3":
        print("1/ Remove one password")
        print("2/ Remove all passwords")
        while True:
            opr = input("What you want (via numbers): ").lower()
            if opr == "1":
                while True:
                    name_pass_r = input("Enter the name of password: ")
                    if name_pass_r.lower() == "back":
                        break
                    else:
                        with open("passwords.txt", "r") as f:
                            lines = f.readlines()
                            new_lines = ""
                            for line in lines:
                                name_pass = line.split(":")[0].strip()
                                if name_pass == name_pass_r:
                                    continue
                                else:
                                    new_lines += line
                            if new_lines == lines:
                                print("This password is not found")
                                print("Check the name of password")
                                continue
                            else:
                                with open("passwords.txt", "w") as f:
                                    f.write(new_lines)
                                print("Congratulation, the password is removed")
                                break
            elif opr == "2":
                with open("passwords.txt", "w") as f:
                    f.write("")
                print("Congratulation, all passwords are removed")
            elif opr == "back":
                break
            else:
                print("Invalid input: This service is not available")
                continue
            break
    elif opr == "4":
        print("1/ View a saved password")
        print("2/ View all saved passwords")
        while True:
            opr = input("What you want (via numbers): ").lower()
            if opr == "1":
                while True:
                    name_pass_v = input("Enter the name of the password: ")
                    if name_pass_v.lower() == "back":
                        break
                    else:
                        with open("passwords.txt", "r") as f:
                            lines = f.readlines()
                            for line in lines:
                                name_pass = line.split(":")[0].strip()
                                if name_pass == name_pass_v:
                                    print(line.split("\n")[0])
                                    print("Congratulation, the password is desiplayed")
                                    break
                                else:
                                    continue
                            if name_pass != name_pass_v:
                                print("This password is not found")
                                print("Check the name of password")
                                continue
                            else:
                                break
            elif opr == "2":
                with open("passwords.txt", "r") as f:
                    print(f.read())
                print("Congratulation, the passwords is desiplayed")
                break
            elif opr == "back":
                break
            else:
                print("Invalid input: This service is not available")
                continue
            break
    elif opr == "5":
        print("The programme is closed")
        break
    else:
        print("Invalid input: This service is not available")
        continue