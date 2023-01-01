from modules.home import *
from utilities.validations import selectField
from utilities.helpers import clear
import maskpass
from data.users import users
from constants.constants import *

def register():
    print("Register Form\n")

    username = selectField('username', input(username_prompt))
    password = selectField('password', input(register_password_prompt))
    phoneno = selectField('phoneno', input(phoneno_prompt))

    if not any(dict['username'] == username and dict['phoneno'] == phoneno for dict in users) :
        print(user_exists) 
    else : 
        users.append(
        {'username': username, 'password': password, 'phoneno': phoneno})
        print(register_success)
        
    sleep(3)
    clear()
    main()


def login():
    print("Login Form\n")

    username = input(username_prompt)
    password = maskpass.advpass(prompt=login_password_prompt)

    cond =False

    for index,dict in enumerate(users):
        if dict['username'] == username and dict['password'] == password :
            cond=True
            users[index]['login'] = True
            print(login_success)

    if not cond :
       print(login_err)

    sleep(3)
    clear()
    home() if cond else main()


def main():

    print(users,title)

    option = input(option_prompt)

    if option == "1":
        clear()
        register()

    elif option == "2":
        clear()
        login()

    elif option == "3":
        print(exit_message)
        exit()
    
    else:
        print(input_err)
        clear()
    
    main()


main()


