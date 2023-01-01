import re
from utilities.helpers import *
from constants.constants import *
from time import sleep


def validateUsername(username):
    pattern = r'\b[A-Za-z0-9._]+\b'
    if re.match(pattern, username):
        return True
    else:
        return False


def validatePassword(password):
    l, u, p, d = 0, 0, 0, 0
    if (len(password) >= 8):
        for i in password:
   
            if (i.islower()):
                l += 1
 
            if (i.isupper()):
                u += 1

            if (i.isdigit()):
                d += 1

            if (i == '@' or i == '$' or i == '_'):
                p += 1
    if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l+p+u+d == len(password)):
        return True
    else:
        return False


def validatePhoneno(phoneno):
    pattern = r'^[6-9]\d{9}$'
    if re.match(pattern, phoneno):
        return True
    else:
        return False

def validateGender(gender):

    if gender.upper() in ["M","F"] :
        return True
    else:
        return False

def validateType(type):

    if type.lower() in ["wl","wg"] :
        return True
    else:
        return False

def validateNumber(number):

    if number.isnumeric() :
        return True
    else:
        return False

def validateBmi(bmi):

    if bmi.isfloat():
        return True
    else:
        return False


dispatch = {
        'username': {
            'err': username_err,
            'fn': validateUsername
        },
        'password': {
            'err': password_err,
            'fn': validatePassword
        },
        'phoneno': {
            'err': phoneno_err,
            'fn': validatePhoneno
            },
        'gender':{
            'err': gender_err,
            'fn': validateGender
        },
         'type':{
            'err': type_err,
            'fn': validateType
        },
        "number":{
            'err':number_err,
            'fn':validateNumber
        },
        "bmi":{
            'err':bmi_err,
            'fn':validateBmi
        }
    }

def selectField(command, value):

    while not (dispatch[command]['fn'](value)):
        print(dispatch[command]['err'])
        print(validation_title)
        option = input(option_prompt)
        if option == "1":
            value = input(f'Enter {command}:')
        elif option == "2":
            print(input_err)
            sleep(3)
            clear()
            exit()


    return value



