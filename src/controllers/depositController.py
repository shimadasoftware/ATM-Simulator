#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deposit Controller

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""   
from random import randint
import time
from datetime import datetime

from views.depositView import showDeposit, showPrepareCash, showInsertCash 
from views.depositView import showConfirmCash, showValidAmount, showInvalidAmount
from views.receiptView import showReceipt, showRemoveReceipt
from views.decision import showDecision
from views.pinView import showPin, showIncorrectPin

from models.transaction import Transaction

#%%
def depositSimulation(minDepositAccount, maxDepositAccount, minBill):
    """Generate a random amount of money according to the 
        minimum denomination cash, minimum deposit, 
        maximum deposit and transaction status.

    Args:
        minDepositAccount (int): Minimum amount of money allowed to deposit.
        maxDepositAccount (int): Maximum amount of money allowed to deposit.
        minBill (int): Minimum denomination of bills in the ATM.

    Returns:
        int: Random amount of cash,
        string: Status of the transaction.
    """
    amount = randint(minDepositAccount, maxDepositAccount)
    amount -= amount % minBill
    status = 'Successful'
    return amount, status

#%%
def amountValidation(amount, minDepositAccount, maxDepositAccount, minBill):
    """Validate the amount of money.

    Args:
        amount (int): Amount of money.
        minDepositAccount (int): Minimum amount of money allowed to deposit.
        maxDepositAccount (int): Maximum amount of money allowed to deposit.
        minBill (int): Minimum denomination of bills in the ATM.

    Returns:
        int: Amount of money,
        string: Status of the transaction,
        int: Option to continue (1) or finish (2).
    """
    option = 2
    amount -= amount % minBill
    if amount < minDepositAccount or amount > maxDepositAccount:
        amount = 0
        status = 'Deposit amount not allowed'
    else:
        status = 'Successful'
        option = 1
    
    if option == 1:
        showValidAmount()
    else:
        showInvalidAmount()
    time.sleep(3)

    showReceipt()
    optionR = 0
    while optionR not in [1, 2]: # Yes - No
        optionR = int(input('-> '))
    if optionR == 1:             # Yes
        showRemoveReceipt()
        time.sleep(3)

    return amount, status, option

#%%
def isCorrectPin(password):
    """Verify password.

    Args:
        password (int): Card password.

    Returns:
        boolean: Password status.
    """
    showPin()
    pin = int(input('-> '))
    if pin != password:
        showIncorrectPin()
        time.sleep(3)
        return False
    else:
        return True

#%%
def getAmount():
    """Get the amount by demo.
    """
    showDeposit()
    option = 0
    while option not in [1, 2]:
        option = int(input('-> '))
    
    showPrepareCash()
    time.sleep(3)

    showInsertCash()
    time.sleep(3)

    showConfirmCash()
    amount = int(input('-> '))
        
    return amount

#%%
def depositController(atm, card, simulation, minDepositAccount, maxDepositAccount, minBill):
    """Deposit Controller.

    Args:
        atm (ATM): Transaction ATM.
        card (Card): Client card. 
        simulation (boolean): Simulation.
        minDepositAccount (int): Minimum amount of money allowed to deposit.
        maxDepositAccount (int): Maximum amount of money allowed to deposit.
        minBill (int): Minimum denomination of bills in the ATM.

    Returns:
        int: Option to Continue (1) or finish (2),
        Transaction: Transaction object.
    """
    if datetime.now() > card.cardExpirationDate:
        amount = 0
        status = 'Card date expired'
    else:
        if not simulation:
            amount = getAmount()
            if isCorrectPin(card.cardPassword):
                amount, status, option = amountValidation(
                    amount, 
                    minDepositAccount, 
                    maxDepositAccount,
                    minBill
                )

                if option == 1:
                    showDecision()              # Continue (1) or finish (2)?
                    option = 0
                    while option not in [1, 2]:
                        option = int(input('-> '))
            else:
                amount = 0
                status = 'Invalid card password'
                option = 2
        else:
            amount, status = depositSimulation(minDepositAccount, maxDepositAccount, minBill)
            option = 1

    transaction = Transaction(
        atm, 
        card,
        3,                      # Deposit
        datetime.now(),
        amount,
        status
    )

    return option, transaction
