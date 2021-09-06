#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Balance Controller 

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""  
import time
from datetime import datetime

from views.balanceView import showBalance
from views.receiptView import showReceipt, showRemoveReceipt
from views.decision import showDecision
from views.pinView import showPin, showIncorrectPin

from models.transaction import Transaction

def balanceController(atm, card, simulation):
    """Balance Controller.

    Args:
        atm (ATM): Transaction ATM.
        card (Card): Client card. 
        simulation (boolean): Simulation.
    """
    if datetime.now() > card.cardExpirationDate:
        amount = 0
        status = 'Card date expired'
    else:
        if not simulation:
            showPin()
            pin = int(input('-> '))
            if pin != card.cardPassword:
                showIncorrectPin()
                time.sleep(3)
                amount = 0
                status = 'Invalid card password'
                option = 2
            else:
                showBalance(card.cardAccount.accountBalance)
                time.sleep(5)
                showReceipt()
            
                option = 0
                while option not in [1, 2]: # Yes - No
                    option = int(input('-> '))
                if option == 1:             # Yes
                    showRemoveReceipt()
                    time.sleep(3)

                showDecision()              # Continue (1) or finish (2)?
                option = 0
                while option not in [1, 2]:
                    option = int(input('-> '))
                
                amount = card.cardAccount.accountBalance
                status = 'Successful'
        else:
            option = 1 
            amount = card.cardAccount.accountBalance
            status = 'Successful'

    transaction = Transaction(
        atm, 
        card,
        1,                      # Balance
        datetime.now(),
        amount,
        status
    )

    return option, transaction
