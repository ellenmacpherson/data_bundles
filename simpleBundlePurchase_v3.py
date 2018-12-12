#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:29:30 2018

@author: ellenmacpherson
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:47:40 2018

@author: ellenmacpherson
"""
from simpleBundlePurchase_v1 import checkPIN
from simpleBundlePurchase_v2 import topUp, MonthlyPlan

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