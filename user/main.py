#! usr/bin/python3
from user import User
from bank import Bank, Wallet
import random
import string
from getpass import getpass
import os
import hashlib
from datetime import datetime
import json
import pickle

user_cmd = None
user_var = []


make_sure_user_set_password = 0
make_sure_user_craete_ac = 0
make_sure_user_set_username = 0

 
try:
    with open('jsonfiles/username.json', 'r') as u:
        User.user_names = json.load(u)
except:
    pass
try:
    with open('jsonfiles/userdata.json', 'r') as u:
        Bank.userdata = json.load(u) 
except:
    pass
try:
    with open('jsonfiles/user_var.json', 'rb') as uv:
        user_var = pickle.load(uv)
except:
    pass
def random_variable(length: int = 2) -> str:
    """returning random variable"""
    st = string.ascii_letters
    return "".join(random.choice(st) for i in range(length))

def generate_salt() -> str:
    """Function to generate random salt"""
    return os.urandom(16).hex()

def hash_password(password: str, salt: str) -> str:
    """Function to hash the password with salt""" 
    salted_password = password + salt 
    hash_object = hashlib.sha256(salted_password.encode())
    return hash_object.hexdigest()

def check_password(stored_password: str, salt: str, provided_password: str) -> bool:
    """Function to check the password"""
    hashed_provided_password = hash_password(provided_password, salt)
    return stored_password == hashed_provided_password


while True:
    user_cmd = int(input("Please Enter your command: \n" + \
                         "0. exit the program \n1. Create Account \n2. Log in\n=> "))
    if user_cmd == 0:
        os.system("clear")
        break

    elif user_cmd == 1:
        os.system("clear")
        user_na = input("Enter your username:\n=>")             
        if user_na in User.user_names:
            print("Warning: username already exist...")
            break
        user_var.append(user_na) 
        user_var[(len(user_var) - 1)] = Wallet()
        user_var[(len(user_var) - 1)].username1 = user_na 
        make_sure_user_craete_ac += 1
        os.system("clear")
        while True:
            pa_wo = getpass("Enter password: ") 
            if len(pa_wo) >= 4:
                user_var[(len(user_var) - 1)].password1 = pa_wo
                break 
            else:
                print("password must have more than 4 charactar....")
        os.system("clear")
        birth = input("Please Enter your birth date -> [Y/M/D]:")
        user_var[(len(user_var) - 1)].birthday1 = birth
        os.system("clear") 
        phnum = input("Enter your phone number\n=>")
        os.system("clear")
        user_var[(len(user_var) - 1)].phone_number1 = phnum
        print("Your account has been successfully created! ):")
        user_var[(len(user_var) - 1)].time = datetime.now()
        user_var[(len(user_var) - 1)].to_dict()
        user_var[(len(user_var) - 1)].save_data() 
        with open('jsonfiles/userdata.json', 'w') as u:
            json.dump(Bank.user_data, u)
        

    elif user_cmd == 2:
        os.system("clear") 
        end_user = input("Enter your username:\n=>")
        os.system("clear")
        end_pass = getpass("Enter your password:\n=>")
        os.system("clear")   
        try:   
            index = User.user_names.index(end_user)
        except:
            pass
        
        if end_user ==  user_var[index].username1  and end_pass == user_var[index].password1:   
            salt = generate_salt()
            hashed_password = hash_password(user_var[index].password1, salt)
            is_correct = check_password(hashed_password, salt, user_var[index].password1)
            os.system("clear") 
            while True:
                cmd = int(input("Please Enter your command:\n1.Display your information\n" + \
                                "2.Edit your information\n3.Change password\n4.Bank operation \n5.Log out \n=> "))
                if cmd == 1:
                    os.system("clear")
                    print(user_var[index].__str__())
                    c1 = input("Enter '0' to pass....")
                    if c1=="0":
                        os.system("clear")    
                        pass

                elif cmd == 2:
                    os.system("clear") 
                    c = int(input("Which on do you want to change? \n1.Username\n2.Phone number\n3.Birthday\n=>"))
                    if c == 1:
                        os.system("clear")
                        new_username = input("Enter New username:")
                        user_var[index].username1 = new_username
                    elif c == 2:
                        os.system("clear")
                        new_phonenumber = input("Enter New phone_number:")
                        user_var[index].phone_number1 = new_phonenumber
                    elif c == 3:
                        os.system("clear")
                        new_birthday = input("Enter New birthday:")
                        user_var[index].birthday1 = new_birthday
                    else:
                        os.system("clear")
                        print("Warning: invalid command...")
                    os.system("clear")
                elif cmd == 3:
                    os.system("clear") 
                    last_password = getpass("Enter you password:")
                    if last_password == user_var[index].password1:
                        os.system("clear")  
                        c2 = input("Which one do you want to change:\n1.Password\n2.Card password\n:")
                        if c2 == "1":
                            os.system("clear")
                            new_password = getpass("Enter New password:")
                            confirm_pass = getpass("Confirm New password:")                        
                            if new_password == confirm_pass:
                                user_var[index].password1 = new_password
                                os.system("clear")
                            else:
                                os.system("clear")
                                print("Warning: the password is not confirm\n Try again....")
                                break
                        elif c2 == "2":
                            os.system("clear")
                            card_new_pass = getpass("Enter you new card password:")
                            confirm_card = getpass("Confirm new card password:")
                            if card_new_pass == confirm_card:
                                user_var[index].card_pass1 = card_new_pass
                            else:
                                print("something went Wrong....")
                        os.system("clear")
                    else:
                        os.system("clear")
                        print("Warning: Wrong password...\n Try again:") 
                    salt = generate_salt()
                    hashed_password = hash_password(user_var[index].password1, salt)
                    is_correct = check_password(hashed_password, salt, user_var[index].password1)

                elif cmd == 4:   
                    c3 = None
                    os.system("clear")
                    passw1 = int(getpass("Enter your card password:\n=>"))
                    os.system("clear")
                    input_cvv2 = int(input("Enter your Cvv2:"))
                    while c3 != 0 and passw1 == user_var[index].card_pass1 and input_cvv2 == user_var[index].cvv2:
                        os.system("clear") 
                        c3 = input("Choose the operation:\n0.back\n1.Show inventory\n2.Deposit\n3.Recharge the wallet\n4.Money transfer\n5.cash withdrawl\n6.purchases subscription\n=>")
                        if c3 == "0":
                            os.system("clear")
                            break
                        elif c3 =="1":
                            os.system("clear")
                            print(user_var[index].__str1__())
                            c1 = input("Enter '0' to pass....")
                            if c1=="0":
                                os.system("clear")    
                                pass
                        elif c3 == "2":
                            os.system("clear")
                            money = int(input("How much money do you want to deposit?\n=>"))
                            user_var[index].add(money)

                        
                        elif c3 == "3":
                            os.system("clear")
                            money = int(input("How much money do you want to charge?\n=>"))
                            user_var[index].sub(money)
                            user_var[index].add_w(money)

                        elif c3 == "4":
                            os.system("clear")
                            money = int(input("How much money do you want to transfer?\n=>"))
                            acc = input("Whose account do you want to deposit?\n=>")
                            user_var[index].transfer(acc, money)

                        elif c3 == "5":
                            os.system("clear")
                            money = int(input("How much money do you want to withdraw?\n=>"))
                            user_var[index].sub(money)

                        elif c3 == "6":
                            os.system("clear")
                            cm = int(input("Which one do you want to buy...\n0.back\n1.Bronze --> 10000\n[It is a basic and simple default service  and does not have special privileges.]\n2.Silver --> 20000\n[This service returns 20% of the amount of each transaction to the wallet for up to three future purchases.]\n3.Gold --> 30000\n[This service rewards 50 percent of the amount plus a free energy drink for the next month.]\n=>"))
                        while True:    
                            if cm == 0:
                                break
                            
                            elif cm == 1:
                                if user_var[index].wallet_balance1 >= 10000:  
                                    user_var[index].wallet_balance1 -= 10000
                                    user_var[index].subscription = 1
                                    break 
                                else:
                                    print("Insufficient inventory")
                            elif cm == 2:
                                if user_var[index].wallet_balance1 >= 20000: 
                                    user_var[index].wallet_balance1 -= 20000
                                    user_var[index].subscription = 2
                                    break  
                                else:
                                    print("Insufficient inventory")
                            elif cm == 3:
                               if user_var[index].wallet_balance1 >= 30000:     
                                    user_var[index].wallet_balance1 -= 30000
                                    user_var[index].subscription = 3
                                    break  
                               else:
                                    print("Insufficient inventory")
                            else:
                                print("invalid command...")
                        else:
                            os.system("clear")
                            print('invalid command!...')
                    if passw1 != user_var[index].card_pass1:
                        os.system("clear")
                        print("Wrong password...!") 
                    correctness = passw1 != user_var[index].card_pass1 
                    if input_cvv2 != user_var[index].cvv2:    
                        if not correctness: 
                            os.system("clear")
                        print("Wrong cvv2...!")
                elif cmd == 5:
                    os.system("clear") 
                    print("Log out...")
                    break

                else:
                    os.system("clear") 
                    print("Warning: invalid command...")
                    break 


        elif user_cmd == 2 and make_sure_user_craete_ac == 0:
            print("Warning: first with '1' command Create account and try again ...")
            os.system("clear")
            break
        elif user_cmd == 1 and make_sure_user_craete_ac == 1:
            print("Warning: You have created account...")
            os.system("clear")
            break
        elif end_user !=  user_var[index].username1:
            print("username not found ...")
        elif end_pass != user_var[index].password1:
            print("Wrong password...")
        else:
            os.system("clear")
            print("Warning: invalid command...") 
            break
        


with open('jsonfiles/username.json', 'w') as un:
    json.dump(User.user_names, un)

with open('jsonfiles/user_var.json', 'wb') as uv:
    pickle.dump(user_var, uv)
