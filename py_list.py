#!/usr/bin/python3

#################################################################
# NAME:             Marc Greyling
# STUDENT NUMBER:   881405156
# DATE:             2024-09-03
# PURPOSE:          List all users accounts stored in accounts 
#                   file 
# VERSION:          0.1.13
#################################################################

#################################
# constants and global variables
#################################

accounts_filepath = 'accounts.txt'
welcomeText = '''
*******************************
***  LIST OF USER ACCOUNTS  ***
*******************************
'''
endText = '''
*******************************
'''

#################################
# functions
#################################

def loopOverAccounts():
    collect = []
    with open(accounts_filepath) as f:
        for line in f:
            if not line:
                continue
            arr = line.strip().split(',')
            if arr[0]:
                collect.append(arr[0])
    return collect

#################
# MAIN ROUTINE
#################

def show_accounts():
    print(welcomeText)
    count = 0
    accounts = loopOverAccounts()
    for account in accounts:
        count += 1
        item = '{:>3}'
        print(item.format(count) + '.', account)
    print(endText)
    print()

# This will run if the file is run directly 
if __name__ == '__main__':  
    print('This routine should not be run directly')

