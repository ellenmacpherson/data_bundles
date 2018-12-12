#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:38:12 2018

@author: ellenmacpherson
"""

def checkPIN_once(truepin):
    attempt = input('Please enter your PIN: ')
    if attempt == str(truepin):
        return True
    else:
        print ("PIN incorrect.")
        return False
    
def checkPIN(truepin):
    if checkPIN_once(truepin):
        return True
    else:
        print ("\nPlease try again (2nd attempt. You have one attempt remaining.)")
    if checkPIN_once(truepin):
        return True
    else:
        print ("Please try again (3rd and final attempt).")
    if checkPIN_once(truepin):
        return True
    else:
        print ("You have used all your attempts. For security reasons, your account has been locked. Contact customer services for help.")
    return False

def DataBundlePurchase(truepin, balance):
    if checkPIN(truepin):
        print ("\nPlease choose your transaction type: ")
        print ("To request a balance, enter 1.")
        print ("To top up a Pay As You Go data bundle, enter 2.")
        print ("To purchase a monthly plan, enter 3.")
        
        transactionChoice = int(input("Please select an option: "))
        
        if transactionChoice == 1:
            print ("Your balance is ", balance, " GBP")
            print ("Thanks for using our service today")
            return "balance-request"
        
        elif transactionChoice == 2:
            print ("Service unavailable")
            
        elif transactionChoice == 3: 
            print ("Service unavailable")
        
        else: 
            print ("Error: transaction type not recognised.")
            return "transaction-error"
    
    else:
        print ("\nPIN authorisation failed - exiting.")
        return "PIN-error"
        
    
    
