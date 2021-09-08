#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Withdraw Controller 

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

from views.withdrawView import showWithdrawal, showOtherAmount, showValidAmount, showInvalidAmount
from views.receiptView import showReceipt, showRemoveReceipt
from views.decision import showDecision
from views.pinView import showPin, showIncorrectPin

from models.transaction import Transaction

#%%
def withdrawSimulation(atm, card, minWithdrawAccount, maxWithdrawAccount, minBill):
    """Generate a random amount of money according to the 
        minimum denomination cash, minimum withdraw, 
        maximum withdraw, atm and card.

    Args:
        atm (ATM): ATM object.
        card (Card): Client card.
        minWithdrawAccount (int): Minimum amount of money allowed to withdraw.
        maxWithdrawAccount (int): Maximum amount of money allowed to withdraw.
        minBill (int): Minimum denomination of bills in the ATM.

    Returns:
        int: Random amount of cash,
        string: Status of the transaction.
    """
    if card.cardAccount.accountBalance < minWithdrawAccount:
        amount = 0
        status = 'Insufficient balance'
    else:
        if card.cardAccount.accountBalance < maxWithdrawAccount:
            amount = randint(minWithdrawAccount, card.cardAccount.accountBalance)
        else:
            amount = randint(minWithdrawAccount, maxWithdrawAccount)
        amount -= amount % minBill

        if amount <= atm.atmCash:
            status = 'Successful'
        else:
            status = 'There is not enough money in the ATM' 
            amount = 0
    
    return amount, status

#%%
def amountValidation(amount, minWithdrawAccount, maxWithdrawAccount,
                    atmCash, accountBalance, minBill):
    """Validate the amount of money.

    Args:
        amount (int): Amount of money.
        minWithdrawAccount (int): Minimum amount of money allowed to withdraw.
        maxWithdrawAccount (int): Maximum amount of money allowed to withdraw.
        atmCash (int): Amount of money in the ATM.
        accountBalance (int): Amount of money in the client's account.
        minBill (int): Minimum denomination of bills in the ATM.

    Returns:
        int: Amount of money,
        string: Status of the transaction,
        int: Option to continue (1) or finish (2).
    """
    option = 2
    if amount < minWithdrawAccount or amount > maxWithdrawAccount:
        amount = 0
        status = 'Withdrawal amount not allowed'
    elif amount > atmCash:
        amount = 0
        status = 'There is not enough money in the ATM'
    elif amount > accountBalance:
        amount = 0
        status = 'Insufficient account balance'
    elif amount % minBill != 0:
        amount = 0
        status = 'There are no bills of this denomination for this withdrawal'
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
    """Get withdraw amount.
    """
    showWithdrawal()
    option = 0
    while option not in [-1, 1, 2, 3, 4, 5, 6]:
        option = int(input('-> '))
    
    if option == 1:
        amount = 100000
    elif option == 2:
        amount = 200000
    elif option == 3:
        amount = 500000
    elif option == 4:
        amount = 700000
    elif option == 5:
        amount = 1000000
    elif option == 6:
        showOtherAmount()
        amount = int(input('-> '))
    return amount

#%%
def withdrawController(atm, card, simulation, minWithdrawAccount, maxWithdrawAccount, minBill):
    """Withdraw Controller.

    Args:
        atm (ATM): Transaction ATM.
        card (Card): Client card. 
        simulation (boolean): Simulation.
        minWithdrawAccount (int): Minimum amount of money allowed to withdraw.
        maxWithdrawAccount (int): Maximum amount of money allowed to withdraw.
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
                    minWithdrawAccount, 
                    maxWithdrawAccount,
                    atm.atmCash,
                    card.cardAccount.accountBalance,
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
            amount, status = withdrawSimulation(
                atm, 
                card, 
                minWithdrawAccount, 
                maxWithdrawAccount, 
                minBill
            )
            option = 1

    transaction = Transaction(
        atm, 
        card,
        2,                      # Withdraw
        datetime.now(),
        amount,
        status
    )

    return option, transaction
