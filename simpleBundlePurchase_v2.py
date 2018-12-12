#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:47:40 2018

@author: ellenmacpherson
"""
from simpleBundlePurchase_v1 import checkPIN


def multipleOfFive(amount):
    return amount == int(amount / 5.0) * 5


def topUp(balance):
    maxTopUp = 150.00
    print ("Please enter the mobile number of the phone you wish to top up: ")
    mobileNumber1 = input()
    print ("Please reconfirm the number you wish to top up: ")
    mobileNumber2 = input()
    if mobileNumber1 == mobileNumber2:
        print ("Max top up amount is £150.")
        print("Top up amount should be a multiple of £5.")
        amount = float(input("Please enter your top up amount: "))

        if amount > maxTopUp:
            print ("Amount exceeds the maximum top up amount of £150.")
            print ("Request refused.")
            return "top-up-request:refused"

        elif amount > balance:
            print ("Amount exceeds available balance.")
            print ("Request refused.")
            return "top-up-request:refused"

        elif multipleOfFive(amount):
            print ("Transaction authorised.")
            print ("Your new account balance is ", balance - amount, 'GBP')
            return ("top-up-request", amount)

        else:
            print ("Top up amount is not a multiple of 5.")
            print ("Request refused.")
            return "top-up-request:refused"

    else:
        print ("Error: the two numbers you entered did not match.")
        print ("Transaction cancelled. Try again.")
        return "top-up-request:refused"

def MonthlyPlan(balance):

    print ("Please enter the mobile number of the phone you wish to top up: ")
    mobileNumber1 = input()
    if len(mobileNumber1) < 11:
        print ("Please enter a valid UK mobile number.")
    elif len(mobileNumber1) == 11:
        print ("Please reconfirm the number you wish to top up: ")
        mobileNumber2 = input()
        if mobileNumber1 == mobileNumber2:
            print ("To purchase our £15 monthly plan with 3000 texts, 300 minutes and 12GB data, enter 1.")
            print("To purchase our £20 monthly plan with 5000 texts, 500 minutes and 20GB data, enter 2.")
            print("To purchase our £30 monthly plan with unlimited texts, minutes and data, enter 3.")
            planNumber = int(input("Please enter your choice: "))

            if planNumber == 1:
                confirm = input("You're purchasing our £15 monthly plan. Enter yes to confirm: ").lower()
                if confirm == 'yes' and balance >= 15:
                    print ("Thank you. Your remaining balance is", (balance - 15), ".")
                    return balance - 15
                elif confirm == 'yes' and balance <= 15:
                    print ("Balance too low. Request refused.")
                    return "plan:refused"
                else:
                    print ("Request cancelled.")
                    return "plan:cancelled"


            elif planNumber == 2:
                confirm = input("You're purchasing our £20 monthly plan. Enter yes to confirm: ").lower()
                if confirm == 'yes' and balance >= 20:
                    print ("Thank you. Your remaining balance is", (balance - 20), ".")
                    return balance - 20
                elif confirm == 'yes' and balance <= 20:
                    print ("Balance too low. Request refused.")
                    return "plan:refused"
                else:
                    print ("Request cancelled.")
                    return "plan:cancelled"

            elif planNumber == 3:
                confirm = input("You're purchasing our £30 monthly plan. Enter yes to confirm: ").lower()
                if confirm == 'yes' and balance >= 30:
                    print ("Thank you. Your remaining balance is", (balance - 30), ".")
                    return balance - 30
                elif confirm == 'yes' and balance <= 30:
                    print ("Balance too low. Request refused.")
                    return "plan:refused"
                else:
                    print ("Request cancelled.")
                    return "plan:cancelled"
            else:
                print ("Plan code invalid. Please select option 1, 2, or 3.")
        else:
            print ("Error. Please ensure the numbers match.")
    else:
        print ("Error")

def DataBundlePurchase(truepin, balance):
    if checkPIN(truepin):
        print ("\nPlease choose your transaction type: ")
        print ("To request a balance, enter 1.")
        print ("to top up a data bundle, enter 2.")
        print ("To purchase a monthly plan, enter 3.")

        transactionChoice = int(input("Please select an option: "))

        if transactionChoice == 1:
            print ("Your balance is ", balance, " GBP")
            print ("Thanks for using our service!")
            return "balance-request"

        elif transactionChoice == 2:
            return topUp(balance)

        elif transactionChoice == 3:
            return MonthlyPlan(balance)

        else:
            print ("Error: transaction type not recognised.")
            return "transaction-error"

    else:
        print ("\nPIN authorisation failed - exiting.")
        return "PIN-error"
