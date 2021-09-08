#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Report Controller.

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""

#%%
def showTransactionData(loop, transaction, bank, atms, accounts):
    """Show transaction data.

    Args:
        loop (int): Quantity of loops.
        transaction (Transaction): Transaction object.
        bank (Bank): Bank object.
        atms (ATMs): ATMs object.
        accounts (Accounts): Accounts object.
    """
    if transaction.transactionType == 1:
        transactionType = 'Balance'
    elif transaction.transactionType == 2:
        transactionType = 'Withdraw'
    else:
        transactionType = 'Deposit'

    print(
        '\n--> Loop {} ({}): Type {}, ATM {} ${:,}, Client {}, Account ${:,}, Amount ${:,}, Status {}'.format(
            loop,
            transaction.transactionTime,
            transactionType,
            transaction.transactionATM.atmID,
            transaction.transactionATM.atmCash,
            transaction.transactionCard.cardAccount.accountClient.clientID,
            transaction.transactionCard.cardAccount.accountBalance,
            transaction.transactionAmount,
            transaction.transactionStatus
        )
    )
    stage(bank, atms, accounts)
    #time.sleep(0.2)

#%%
def stage(bank, atms, accounts):
    """Display bank, atms, and accounts information.

    Args:
        bank (Bank): Bank object.
        atms (ATMs): ATMs object.
        cards (Cards): Cards object.
    """
    print("-" * 80)
    print("Bank: " + bank.bankName)
    print("-" * 80)

    print("ATMs:", end=' ')
    for atm in atms.atms:
        print("{}: ${:>10,}".format(atm.atmID, atm.atmCash), end=' | ')
    print("\n" + "-" * 80)

    print("Accounts:", end=' ')
    previousClient = 0
    for account in accounts.accounts:
        if account.accountClient.clientID != previousClient:
            print(
                "\nClient-{}:".format(account.accountClient.clientID), 
                end=' '
            )
            previousClient = account.accountClient.clientID
        print("${:>10,}".format(account.accountBalance), end=' | ')
    print("\n" + "-" * 80)
