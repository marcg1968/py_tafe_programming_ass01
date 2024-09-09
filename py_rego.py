#!/usr/bin/python3

#################################################################
# NAME:             Marc Greyling
# STUDENT NUMBER:   881405156
# DATE:             2024-09-03
# PURPOSE:          Add new user account (username and pasword) 
#                   to accounts file
# VERSION:          0.1.20
#################################################################

#################################
# constants and global variables
#################################

welcomeTextHdr = '''
****************************
*** Account registration ***
****************************\
'''
welcomeTextMain = 'Use this program to add a new user account by supplying a unique username and a password.'
welcomeTextPwMinLen = 'The mininum length for the password is'
promptName = 'Enter a unique username'
promptPw = 'Enter a password'
accounts_filepath = './accounts.txt'
password_min_length = 10

##############
# functions
##############

# takes single argument username loops over lines in accounts file 
# if username is found, returns true, else returns false
def chkUserInAccounts(*args):
    if len(args) < 1:
        return False
    with open(accounts_filepath) as f:
        for line in f:
            arr = line.split(',')
            if arr[0] == args[0]:
                return True
    return False

def addUserCredentialsToFile(name, pw):
    success = False
    try:
        f = open(accounts_filepath, 'a')
        f.write('\n' + name + ',' + pw)
        f.close()
        print('New user ' + name + ' added.')
    except Exception as e:
        print('Error writing file')
    finally:
        success = True
    return success

# prompts for input of new password
# NOTE: password is shown in plaintext as typed by the user
def promptAndCheckPassword():
    pw = ''
    pwCheck = False
    while pwCheck is False:
        pw = input(promptPw + ': ')
        pwCheck = True if len(pw) >= password_min_length else False
        if pwCheck is True:
            break
        print('Password needs to be of length ' + str(password_min_length) + ' or greater')
        print('Try again, please ... ')
    return pw

# prompts for username and checks if username already defined
# if so, returns empty string, else returns new username
def promptUserName():
    name = input(promptName + ': ')

    # check if account exists
    accountAlreadyExists = chkUserInAccounts(name)
    if accountAlreadyExists is True:
        print('Account for username ', name, ' already exists.', sep='"')
        return ''
    return name


def showWelcome():
    print(welcomeTextHdr, '\n')
    print(welcomeTextMain, '\n')
    print(welcomeTextPwMinLen, password_min_length, '\n')

#################
# MAIN ROUTINE
#################

def register_user():

    showWelcome()

    finished = False
    while not finished:

        name = promptUserName()
        if not name:
            continue

        # if reached here, account doesn't yet exist

        # check password min length requirements
        pw = promptAndCheckPassword()

        # if reached here, password input meets requirements
        print('Password accepted')

        # append account credentials to file
        finished = addUserCredentialsToFile(name, pw)

# This will run if the file is run directly 
if __name__ == '__main__':  
    register_user()
