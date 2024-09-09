#!/usr/bin/python3

#################################################################
# NAME:             Marc Greyling
# STUDENT NUMBER:   881405156
# DATE:             2024-09-03
# PURPOSE:          Prompt for username and password. Verify
#                   against credentials stored in accounts file 
# VERSION:          0.1.19
#################################################################

from getpass import getpass

#################################
# constants and global variables
#################################

welcomeText = '''
*******************
* * *  LOGIN  * * *
*******************
'''
failText = 'Your attempt to log in has failed.'
numberOfAttemptsText = 'Number of login attempts'
accounts_filepath = './accounts.txt'
max_attempts = 5

#################################
# functions
#################################

# loops over lines in accounts file 
# if no args, return False
# if 2 args, name and password are supplied, 
#   and if a match is found
#   returns true else return false
def verifyUserPw(*args):
    if not len(args) or len(args) < 2:
        return False
    with open(accounts_filepath) as f:
        for line in f:
            arr = line.strip().split(',')
            # if name and pw match and return true
            if len(arr) > 1 and arr[0] == args[0] and arr[1] == args[1]:
                return True
    # default
    return False

# prompts for input of password
# NOTE: `getpass` prevents password being echoed to console
def promptForPassword():
    pw = getpass('Input password: ')
    return pw

#################
# MAIN ROUTINE
#################

def login():
    print(welcomeText)
    finished = False # on successful login, set to True
    name = ''
    # count the number of login attempts
    count = 0
    while not finished:

        # break loop if login attempts reach maximum permitted
        if count and count >= max_attempts:
            break
        
        # prompt for name and trim any leading/trailing space
        name = input('Name: ')
        name = name.strip()

        # restart while loop if zero length input
        if not name:
            count += 1 # increment attempts counter
            continue

        # prompt for password; restart loop if zero length input
        pw = promptForPassword()
        if not pw:
            count += 1 # increment attempts counter
            continue

        resultCredentialsCheck = verifyUserPw(name, pw)
        
        if not resultCredentialsCheck:
            count += 1 # increment attempts counter
            print('\nIncorrect password or unknown username. Please try again.\n')
        else:
            print('\nPassword accepted.', 'Logged in as', name, '\n')
            finished = True
    
    # if reached here and not finished, display failure message
    if not finished:
        print(numberOfAttemptsText + ':', count)
        print(failText, '\n')
    else: # login was successful
        return True

# This will run if the file is run directly 
if __name__ == '__main__':  
    login()

