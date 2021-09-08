#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transaction Controller

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""   
from datetime import datetime
from random import randint, randrange

from models.transaction import Transaction

class Transactions():
    """Transaction Collection.
    """

#%%
    def __init__(self, atms, cards, minWithdrawAccount,  maxWithdrawAccount, 
                minDepositAccount, maxDepositAccount, minBill, maxTransactions):
        """Transaction collection default constructor.

        Args:
            atms (ATMs): ATM's collection.
            cards (Cards): Cards collection.
            minWithdrawAccount (int): Minimum withdraw account.
            maxWithdrawAccount (int): Maximum withdraw account.
            minDepositAccount (int): Minimum deposit account.
            maxDepositAccount (int): Maximum deposit account.
            minBill (int): Minimum denomination of bills in the ATM.
            maxTransactions (int): Maximum number of transactions for random collection.
        """
        self._atms               = atms
        self._cards              = cards
        self._minWithdrawAccount = minWithdrawAccount
        self._maxWithdrawAccount = maxWithdrawAccount
        self._minDepositAccount  = minDepositAccount
        self._maxDepositAccount  = maxDepositAccount
        self._maxTransactions    = maxTransactions
        self._minBill            = minBill
        self._transactions       = []

#%%
    def createTransactions(self):
        """Create three transactions instances
        """
        self._transactions = [
            Transaction (
                self.atms[0],
                self.cards[0],
                1,                  # Balance
                datetime.now(),
                self.cards[0].account.accountBalance, 
                'Successful'
            ),
            Transaction (
                self.atms[0],
                self.cards[0],
                2,                  # Withdraw
                datetime.now(),
                50000,
                'Successful'
            ),
            Transaction (
                self.atms[0],
                self.cards[0],
                3,                  # Deposit
                datetime.now(),
                1500000,
                'Successful'
            ),
        ]

#%%
    def createRandomTransactions(self):
        """Create a random Transaction Collection.
        """
        self._transactions = []
        transactionNumber = randint(1, self._maxTransactions)

        for i in range(transactionNumber):
            atm  = self._atms[randrange(len(self._atms))]
            card = self._cards[randrange(len(self._cards))]
            transactionType = randint(1, 3)

            if transactionType == 1:            # Balance
                amount = card.cardAccount.accountBalance
                status = 'Successful'
            elif transactionType == 2:          # Withdraw
                if card.cardAccount.accountBalance < self._minWithdrawAccount:
                    status = 'Insufficient balance'
                    amount = 0
                else: 
                    if card.cardAccount.accountBalance < self._maxWithdrawAccount:
                        amount = randint(self._minWithdrawAccount, card.account.accountBalance)
                    else:
                        amount = randint(self._minWithdrawAccount, self._maxWithdrawAccount)
                    amount -= amount % self._minBill
                    status = 'Successful'
            else:                               # Deposit
                amount = randint(self._minDepositAccount, self._maxDepositAccount)
                amount -= amount % self._minBill
                status = 'Successful'

            transaction = Transaction(
                atm,
                card,
                transactionType,
                datetime.now(),
                amount,
                status
            )
            self._transactions.append(transaction)

#%%
    def randomSelectedTransaction(self):
        """Selecting a random transaction.

        Returns:
            transaction: The selected transaction
        """
        return self._transactions[randrange(len(self._transactions))]

#%%
    def add(self, transaction):
        """Append a transaction to the transaction collection.

        Args:
            transaction (Transaction): Transaction to append.
        """
        self._transactions.append(transaction)

#%%
    def __str__(self):
        """Transactions output.

        Returns:
            String: Output Transaction string.
        """
        output = '[Transactions: \n'
        for transaction in self._transactions:
            output += transaction.__str__() + '\n'
        return output + ']'
