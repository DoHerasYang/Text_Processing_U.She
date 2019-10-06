'''
Copyright@ Mark Hepple,Professor of University of Sheffield. All rights reserved.
Just for educational purpose and if you want use it into commercial purpose please contact the original writer.
'''

'''
Scenrio: 
        A bank user approaches the ATM and inserts their card.We imagine that the ATM then reads the card details and 
uses them to access key information from the bank’s central computer, namely: 
        (i) the card owner’s true PIN
        (ii) their current balance.

        The ATM then calls the code that you will write, which checks that the user knows the correct PIN, and if so, 
then provides ATM services to the user.

TODO:
        Download the code files SimpleCashpoint.py and test_cashpoint.py from the module home page, and open them in 
Spyder. The first file (SimpleCashpoint.py) contains a ‘dummy’ (i.e.empty) definition of the cashpoint function, which 
consists of a single print statement (which prints a message that the function has not yet been defined). It is your 
task to complete this function definition, so as to implement the system described by the flowchart.
        The second file (test_cashpoint.py) contains some test cases. If you run this file (by pressingF5), it first 
imports the cashpoint function from the first file, and then calls it with differentparameters, i.e. specifying different
PIN numbers and different current balances. The first call to the function in that file is given as:

Challenge: 
            1)Build the simple Graphic interface by PyQt5.
            2)Build more efficient system and user-interface

'''
import sys

try_times = 0
storage_balance = []


def cashpoint(truepin, balance):
    print("Welcome to Use the CashMachine on the Platform Python 3.7\n")
    func_handle = check_pin(truepin)
    while(not func_handle):  # If dot't receive the correct PIN we should re-input the correct pin 3 times
        print("We cannot find the correct PIN you input, please try again")
        if try_times == 3:
            print("Exceed the Maximum attempt times\n")
            exit(0)
        func_handle = check_pin(input())
        try_times = try_times + 1

    print("Now,Please Select the Transaction Service you want to accept\n")
    print("1.Get your Balance Information\n")
    print("2.Withdraw your amount and display the balance amount\n")
    print("3.Use the Phone Top-up Function\n")
    option_val = input("Please input the NUMBER of option:")
    if int(option_val) == 1:
        return balance
    elif int(option_val) == 2:
        return balance
    elif int(option_val) == 3:
        print("Service is not available\n")
    else:
        print("Error Input Service suspend\n")
        exit(0)

def check_pin(in_pin):
    file = open("./stoage.txt", 'r')
    if not file:
        print("cannot open the file,Please check the file location\n")
    pin = file.read().splitlines()
    for line in pin:
        if  str(in_pin) == line:        
            file.close()
            return True
    file.close()
    return False









