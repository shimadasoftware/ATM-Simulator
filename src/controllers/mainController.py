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

from controllers.bankController import createBank
from controllers.atmController import ATMs
from controllers.clientController import Clients
from controllers.accountController import Accounts
from controllers.cardController import Cards
from controllers.transactionController import Transactions

from views.mainView import mainView, insertCardView, insertCardDeepelyView, insertCardCompletelyView
from views.mainView import mainMenuView

from controllers.balanceController import balanceController
from controllers.withdrawController import withdrawController
from controllers.depositController import depositController

# import controllers.exitController

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
        simulation ([type]): [description]
    """

    global maxSimulationTime

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

    global bank, atms, atm
    global clients, client, accounts, account, cards, card
    global transactions

    bank    = createBank()
    atms    = ATMs(
        bank, maxATMs, minATMCash, maxATMCash, minBill
    )
    atms.createATMs()
    atm     = atms.randomSelectedATM()

    clients = Clients(maxClients)
    if simulation:
        clients.createRandomClients()
    else:
        clients.createClients()

    accounts = []
    for client in clients:
        accList = Accounts(client, maxAccounts, maxAccountBalance)
        if simulation:
            accList.createRandomAccounts()
        else:
            accList.createAccounts()
        accounts = accounts + accList

    cards = []
    for account in accounts:
        carList = Cards(account, maxCards)
        if simulation:
            carList.createCards()
        else:
            carList.createRandomCards()
        cards = cards + carList

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
 
#%%
def getOption(simulation):
    """Select the type of transaction to be made.

    Args:
        simulation (boolean): graphical or simulation.
    """
    option = 0
    loops = 0
    while option != -1:     # Finish
        client  = clients.randomSelectedClient()
        account = accounts.randomSelectedAccount(client)
        card    = cards.randomSelectedCard(account)

        if not simulation:
            mainMenuView()  # Balance, Withdraw, Deposit, Consult Trasactions
            while option not in [-1, 1, 2, 3, 99]:
                option = int(input('-> '))
        else:
            loops += 1
            if loops > maxSimulationTime:
                option = -1 # End of simulation
            else: 
                option = randint(1, 3)

        if option == 1:     # Balance
            option, transaction = balanceController(atm, card, simulation)
            transactions.add(transaction)
            option = -1 if option == 2 else 0   # option = 2 (finish)
        elif option == 2:   # Withdraw
            option, transaction = withdrawController(atm, card, simulation)
            transactions.add(transaction)

            if transaction.transactionStatus == 'Successful':
                atm.atmCash -= transaction.transactionAmount
                card.cardAccount.accountBalance -= transaction.transactionAmount
        elif option == 3:
            depositController()
    # elif option == -1:
    #     controllers.exitController()
        elif option == 99:
            print(transactions)
            option = input("Press Enter to continue...")
            option = 0
    print(transactions)

#%%
def mainController(simulation):
    """Start of application

    Args:
        simulation (boolean): graphical or simulation.
    """
    initialize(simulation)
    #if not simulation:
        #previousScreens()
    getOption(simulation)

    # stats()
    # visualization()
