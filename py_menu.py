#!/usr/bin/python3

#################################################################
# NAME:             Marc Greyling
# STUDENT NUMBER:   881405156
# DATE:             2024-09-03
# PURPOSE:          Display menu to 
#                   1. register new user
#                   2. verify username/password credentials
#                   3. list user accounts
# VERSION:          0.1.3
#################################################################

import py_list
import py_login
import py_rego

#################################
# constants and global variables
#################################

isLoggedIn = False
needToLogin = 'You need to log in first'
alreadyLoggedIn = 'You are already logged in'
menuTxt = '''\
+++++++++++++++++++++++
+++    MAIN MENU    +++
+++++++++++++++++++++++
'''
menuItems = [
    'Register new user',
    'Log in',
    'List user accounts',
]

#################################
# functions
#################################

def showMenu():
    print(menuTxt)
    for i in range(len(menuItems)):
        item = '{:>3}'
        print(item.format(i + 1) + '.', menuItems[i])
    print(item.format('X') + '.', 'Exit')
    print()

def doLogin():
    global isLoggedIn
    if isLoggedIn:
        print(alreadyLoggedIn)
        return True
    success = py_login.login()
    if success:
        isLoggedIn = True
        return True
    return False

#################
# MAIN ROUTINE
#################

def main():
    shouldExit = False
    while not shouldExit:
        showMenu()
        choice = str(input('Choice: '))
        # only consider first char/number entered and make it uppercase
        choice = choice[0:1].upper()
        if choice == 'X':
            shouldExit = True
            print('Now exiting')
            break
        if int(choice) == 1:
            py_rego.register_user()
        if int(choice) == 2:
            doLogin()
        if int(choice) == 3:
            if isLoggedIn:
                py_list.show_accounts()
            else:
                print(needToLogin)
                doLogin()
        # if reached here, the input is not valid, loop will restart


# This will run if the file is run directly 
if __name__ == '__main__':  
    main()
