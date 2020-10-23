import random
import sqlite3

Balance = 0
logged_in = False
logged_in_account = []
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS card (
        id INTEGER,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
        )""")
conn.commit()

def create_card_number():
    iin = '400000' # 6 charactors
    bankIN = '' # 9 charactors
    for x in range(9): # count to 9
        bankIN += str(random.randint(0,9))
        iinbin = iin + bankIN
    return  iinbin# creates 15 digit card number

def checksum(iinbin):
    index = []
    for digit in iinbin: #create list of digits
        index.append(int(digit))
    for x in range(15): # index numbers that are odd are *2
        if ((x+1) % 2) != 0: # odd number
            index[x] = index[x]*2
    for y in range(15):
        if index[y] > 9:
            index[y] = index[y] - 9
    if sum(index) % 10 > 0:
            checksum = 10 - (sum(index) % 10)
    else:
        checksum = 0
    return checksum

def create_pin():
    pin = ''
    for x in range(4): # count to 9
        pin += str(random.randint(0,9))
    return pin

def login(entered_ccn, entered_pin):
    global logged_in
    global logged_in_account
    cur.execute("SELECT * FROM card")
    accounts = cur.fetchall()
    for account in accounts:
        #print(account)
        if account[1] == entered_ccn and account[2] == entered_pin:
            logged_in = True
            logged_in_account = [account[1], account[2], account[3]] # put SQL data into p2
            print('You have successfully logged in!')

def checkAccount(entered_ccn):
    cur.execute("SELECT * FROM card")
    accounts = cur.fetchall()
    for account in accounts:
        if account[1] == entered_ccn:
            return True

def transfer(amount):
    if amount > p2.bal:
        print('Not enough money!')
    else:
        p2.bal -= amount
        #update sql
        sql_balance = f'UPDATE card SET balance = {p2.bal} WHERE number = {p2.ccn};'
        cur.execute(sql_balance)
        sql_balance = f'UPDATE card SET balance = balance + {amount} WHERE number = {entered_ccn};'
        cur.execute(sql_balance)
        conn.commit()
        print('Success!')

class Account:
  def __init__(self, ccn, pin, bal=0):
    self.ccn = ccn
    self.pin = pin
    self.bal = bal

while True:
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    selection = input()
    if selection == '1':
        p1 = Account(create_card_number(), create_pin())
        print('\nYour card has been created')
        print('Your card number:')
        print(p1.ccn + str(checksum(p1.ccn)))
        print('Your card PIN:')
        print(p1.pin)
        forSQL = [0, p1.ccn + str(checksum(p1.ccn)), p1.pin, p1.bal]
        cur.execute("INSERT INTO card VALUES (?,?,?,?)", forSQL)
        conn.commit()

    elif selection == '2':
        print('\nEnter your card number:')
        entered_ccn = input()
        print('Enter your PIN:')
        entered_pin = input()
        print()
        login(entered_ccn, entered_pin)
        if logged_in == True:
            p2 = Account(logged_in_account[0], logged_in_account[1], logged_in_account[2])
        while logged_in == True:
            #print(p2.ccn)
            print()
            print('1. Balance')
            print('2. Add income')
            print('3. Do transfer')
            print('4. Close account')
            print('5. Log out')
            print('0. Exit')
            loggedin_selection = input()
            if loggedin_selection == '1':
                print('\nBalance: ' + str(p2.bal))
            elif loggedin_selection == '2':
                print ('\nEnter income:')
                p2.bal = p2.bal + int(input())
                #update sql
                sql_balance = f'UPDATE card SET balance = {p2.bal} WHERE number = {p2.ccn};'
                cur.execute(sql_balance)
                conn.commit()
                print('Income was added!')
                #print(p2.bal)
            elif loggedin_selection == '3':
                print ('\nTransfer')
                print('Enter card number:')
                entered_ccn = input()
                # Check number is real i.e. check checksum
                if entered_ccn != (entered_ccn[:-1] + str(checksum(entered_ccn[:-1]))):
                    print('Probably you made a mistake in the card number. Please try again!')
                # Check account exists in DB
                elif checkAccount((entered_ccn)) != True:
                    print('Such a card does not exist.')
                else: #account exists
                    print('Enter how much money you want to transfer:')
                    amount = int(input())
                    transfer(amount)
            elif loggedin_selection == '4':
                #update sql
                sql_balance = f'DELETE from card WHERE number = {p2.ccn};'
                cur.execute(sql_balance)
                conn.commit()
                print ('\nThe account has been closed!')
            elif loggedin_selection == '5':
                print ('You have successfully logged out!')
                conn.commit()
                conn.close()
            elif loggedin_selection == '0':
                print('Bye!')
                conn.commit()
                conn.close()
                exit()
        else:
            print('Wrong card number or PIN!')
            print()

    elif selection == '0':
        conn.commit()
        conn.close()
        exit()
conn.commit()
conn.close()
