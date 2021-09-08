#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Record class.

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""

import pandas as pd

class Record():
    """Record class.
    """

#%%
    def __init__(self):
        """Record Default Constructor.

        Args:
            atmDict (dict): ATM dictionary.
            clientDict (dict): Client dictionary.
            transactionDict (dict): Transaction dictionary.
        """
        self._atmDict         = {}
        self._clientDict      = {}
        self._transactionDict = {}
        self._atmDF           = pd.DataFrame()
        self._clientDF        = pd.DataFrame()
        self._transactionDF   = pd.DataFrame()

#%%
    @property
    def atmDict(self):
        return self._atmDict
    
    @atmDict.setter
    def atmDict(self, atmDict):
        self._atmDict = atmDict

    @property
    def clientDict(self):
        return self._clientDict
    
    @clientDict.setter
    def clientDict(self, clientDict):
        self._clientDict = clientDict

    @property
    def transactionDict(self):
        return self._transactionDict
    
    @transactionDict.setter
    def transactionDict(self, transactionDict):
        self._transactionDict = transactionDict

    @property
    def atmDF(self):
        return self._atmDF
    
    @atmDF.setter
    def atmDF(self, atmDF):
        self._atmDF = atmDF

    @property
    def clientDF(self):
        return self._clientDF
    
    @clientDF.setter
    def clientDF(self, clientDF):
        self._clientDF = clientDF

    @property
    def transactionDF(self):
        return self._transactionDF
    
    @transactionDF.setter
    def transactionDF(self, transactionDF):
        self._transactionDF = transactionDF

#%%
    def recordTransaction(self, loop, transaction):
        """Record a transaction into the dictionaries.

        Args:
            loop (int): Quantity of loops.
            transaction (Transaction): Transaction object.
        """

        a = {}
        a['time']           = transaction.transactionTime
        a['atm']            = transaction.transactionATM.atmID
        a['transaction']    = transaction.transactionType
        a['cash']           = transaction.transactionATM.atmCash
        a['status']         = transaction.transactionStatus
        self._atmDict[loop] = a

        c = {}
        c['time']              = transaction.transactionTime
        c['client']            = transaction.transactionCard.cardAccount.accountClient.clientID
        c['account']           = transaction.transactionCard.cardAccount.accountNumber
        c['transaction']       = transaction.transactionType
        c['balance']           = transaction.transactionCard.cardAccount.accountBalance
        c['status']            = transaction.transactionStatus
        self._clientDict[loop] = c

        t = {}
        t['time']                   = transaction.transactionTime
        t['transaction']            = transaction.transactionType
        t['amount']                 = transaction.transactionAmount
        t['status']                 = transaction.transactionStatus
        self._transactionDict[loop] = t

#%%
    def createDataFrames(self):
        """Convert dictionaries to dataframes.
        """
        self._atmDF = pd.DataFrame.from_dict(self._atmDict, orient='index')
        
        self._clientDF = pd.DataFrame.from_dict(self._clientDict, orient='index')
        self._clientDF['longAccount'] = self._clientDF.client.map(str) +\
            '_' + self._clientDF.account.map(str)
        
        self._transactionDF = pd.DataFrame.from_dict(self._transactionDict, orient='index')
