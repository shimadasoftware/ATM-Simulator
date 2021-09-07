#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main Controller 

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

from controllers.settings import config

from models.atms import ATMs
from models.clients import Clients
from models.accounts import Accounts
from models.cards import Cards
from models.transactions import Transactions
from models.record import Record

from views.mainView import mainView, insertCardView, insertCardDeepelyView, insertCardCompletelyView
from views.mainView import mainMenuView

from controllers.bankController import createBank
from controllers.balanceController import balanceController
from controllers.withdrawController import withdrawController
from controllers.depositController import depositController
from controllers.statsController import stats
from controllers.reportController import stage, showTransactionData
from controllers.plotController import resultPlots

__author__    = ["Juana Valentina Mendoza Santamaría", "Alix Ivonne Chaparro Vasquez"]
__copyright__ = "Copyright 2021, Universidad Santo Tomás Tunja"
__credits__   = ["Martha Susana Contreras Ortiz"]
__license__   = "GPL"
__version__   = "1.0.1"
__maintainer__= ["Juana Valentina Mendoza Santamaría", "Alix Ivonne Chaparro Vasquez"]
__email__     = ["juana.mendoza@usantoto.edu.co", "alix.ivonne@usantoto.edu.co"]
__status__    = "Develpment"


#%%
def previousScreens():
    """
    Project the screens
    """
    mainView()
    time.sleep(2)

    insertCardView()
    time.sleep(2)

    insertCardDeepelyView()
    time.sleep(2)

    insertCardCompletelyView()
    time.sleep(2)

#%% 
def initialize(simulation):
    """Initializing variables

    Args:
        simulation (boolean): True (simulation) - False (Demo)
    """

    global maxSimulationTime
    global minWithdrawAccount, maxWithdrawAccount
    global minDepositAccount, maxDepositAccount
    global minBill
    global record

    maxATMs            = config.PARAMETERS['maxATMs']
    minATMCash         = config.PARAMETERS['minATMCash']
    maxATMCash         = config.PARAMETERS['maxATMCash']
    minBill            = config.PARAMETERS['minBill']
    maxClients         = config.PARAMETERS['maxClients']
    maxAccounts        = config.PARAMETERS['maxAccounts']
    maxAccountBalance  = config.PARAMETERS['maxAccountBalance']
    maxCards           = config.PARAMETERS['maxCards']
    minWithdrawAccount = config.PARAMETERS['minWithdrawAccount']
    maxWithdrawAccount = config.PARAMETERS['maxWithdrawAccount']
    minDepositAccount  = config.PARAMETERS['minDepositAccount']
    maxDepositAccount  = config.PARAMETERS['maxDepositAccount']
    maxTransactions    = config.PARAMETERS['maxTransactions']
    maxSimulationTime  = config.PARAMETERS['maxSimulationTime']

    global bank, atms
    global clients, accounts, cards
    global transactions

    bank    = createBank()
    atms    = ATMs(
        bank, maxATMs, minATMCash, maxATMCash, minBill
    )
    if simulation:                      # Simulation
        atms.createRandomATMs()
    else:                               # Controlled demo
        atms.createATMs()

    clients = Clients(maxClients)
    if simulation:
        clients.createRandomClients()
    else:
        clients.createClients()

    accounts = Accounts(
        clients.clients[0], 
        maxAccounts, 
        maxAccountBalance,
        minBill
    )
    if simulation:
        for client in clients.clients:
            oldList = accounts.accounts
            accounts.client = client
            accounts.createRandomAccounts()
            newList = accounts.accounts
            accounts.accounts = oldList + newList
    else:
        accounts.createAccounts()

    cards = Cards(accounts.accounts[0], maxCards)
    if simulation:
        for account in accounts.accounts:
            oldList = cards.cards
            cards.account = account
            cards.createRandomCards()
            newList = cards.cards
            cards.cards = oldList + newList
    else:
        cards.createCards()

    transactions = Transactions(
        atms, 
        cards, 
        minWithdrawAccount, 
        maxWithdrawAccount, 
        minDepositAccount, 
        maxDepositAccount, 
        minBill, 
        maxTransactions
    )

    record = Record()
 
#%%
def getOption(simulation):
    """Select the type of transaction to be made.

    Args:
        simulation (boolean): demo or simulation.
    """
    global record

    loop = 0
    option = 0
    while option != -1:     # Finish
        atm     = atms.randomSelectedATM()
        client  = clients.randomSelectedClient()
        account = accounts.randomSelectedAccount(client)
        card    = cards.randomSelectedCard(account)

        if not simulation:
            mainMenuView()  # Balance, Withdraw, Deposit, Consult Trasactions
            while option not in [-1, 1, 2, 3, 99]:
                option = int(input('-> '))
        else:
            loop += 1
            if loop >= maxSimulationTime:
                option = -1 # End of simulation
            else: 
                option = randint(1, 3)

        if option == 1:     # Balance
            option, transaction = balanceController(atm, card, simulation)
            transactions.add(transaction)

        elif option == 2:   # Withdraw
            option, transaction = withdrawController(
                atm, 
                card, 
                simulation, 
                minWithdrawAccount, 
                maxWithdrawAccount, 
                minBill
            )
            transactions.add(transaction)

            if transaction.transactionStatus == 'Successful':
                atm.atmCash -= transaction.transactionAmount
                card.cardAccount.accountBalance -= transaction.transactionAmount
        
        elif option == 3:   # Deposit
            option, transaction = depositController(
                atm, 
                card, 
                simulation,
                minDepositAccount,
                maxDepositAccount,
                minBill
            )
            transactions.add(transaction)

            if transaction.transactionStatus == 'Successful':
                atm.atmCash += transaction.transactionAmount
                card.cardAccount.accountBalance += transaction.transactionAmount
            
        elif option == 99:
            print(transactions)
            option = input("Press Enter to continue...")
        
        if option != -1:
            option = -1 if option == 2 else 0   # option = 2 (finish)
        
        if simulation:
            showTransactionData(loop, transaction, bank, atms, accounts)

        record.recordTransaction(loop, transaction)


#%%
def mainController(simulation):
    """Start of application

    Args:
        simulation (boolean): demo or simulation.
    """
    global bank, atms, accounts
    global record

    initialize(simulation)

    if not simulation:
        previousScreens()

    stage(bank, atms, accounts)
    getOption(simulation)

    stats(record)
    resultPlots(record)
