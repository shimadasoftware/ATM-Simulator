#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Account Class Controller

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""  

from random import randint, randrange
from models.account import Account

class Accounts():
    """Accounts Collection
    """
#%%
    def __init__(self, client, maxAccounts, maxAccountBalance, minBill):
        """Accounts Collection Default Constructor 

        Args:
            client (Client): Account client (owner)
            maxAccounts (int): Maximum accounts per client
            maxAccountBalance (int): Max account balance
            minBill (int): Minimum denomination bills.
        """
        self._client            = client
        self._maxAccounts       = maxAccounts
        self._maxAccountBalance = maxAccountBalance
        self._minBill           = minBill
        self._accounts          = []

#%%
    @property
    def client(self):
        return self._client
    
    @client.setter
    def client(self, client):
        self._client = client

#%%
    @property
    def accounts(self):
        return self._accounts
    
    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

#%%        
    def createAccounts(self):
        """Create three accounts of the client
        """
        self._accounts = [
            Account(
                123456789,
                self._client,
                "Savings",
                10000000,
            ),
            Account(
                223456789,
                self._client,
                "Checking",
                5000000,
            ),
            Account(
                423456789,
                self._client,
                "Savings",
                1500000,
            ),
        ]

#%%
    def createRandomAccounts(self):
        """Create a random account collection.
        """
        self._accounts = []
        accountType = 'Savings' if randint(0, 1) == 0 else 'Checking'
        for id in range(randint(1, self._maxAccounts)):
            balance = randint(0, self._maxAccountBalance)
            balance -= balance % self._minBill
            account = Account(
                (id + 1),
                self._client,
                accountType,
                balance
            )
            self._accounts.append(account)

#%%
    def randomSelectedAccount(self, client):
        """Selecting an Account

        Args:
            client ([type]): [description]

        Returns:
            Account: The selected Account
        """
        tmpList = []
        for account in self._accounts:
            if account.accountClient == client:
                tmpList.append(account)
        
        if len(tmpList) > 0:
            return tmpList[randrange(len(tmpList))]
        else:
            return self._accounts[randrange(len(self._accounts))]

#%%
    def __str__(self):
        """Accounts output

        Returns:
            String: Output Account string
        """
        output = '[Accounts: \n'
        for account in self._accounts:
            output += account.__str__() + '\n'
        return output + ']'
