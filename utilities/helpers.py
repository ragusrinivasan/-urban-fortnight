from time import sleep
import os


def clear(): return os.system('cls')

def back(): 
    message=''
    if input("\nEnter 1 to go back:") == "1" :
        message="Rerouting..."  
    else :
        message="Wrong input provided. Rerouting to home page"

    print(message)
    sleep(3)
    clear()
