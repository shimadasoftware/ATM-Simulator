#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transaction Class

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""     

class Transaction():
    """Transaction Class.
    """

#%%
    count = 0

    def __init__(self, transactionATM, transactionCard, transactionType, 
                transactionTime, transactionAmount, transactionStatus):
        """Transaction default constructor.

        Args:
            transactionATM (ATM, mandatory): Transaction ATM.
            transactionCard (Card, mandatory): Transaction Card.
            transactionType (str, mandatory): Transaction type (Balance, Withdraw, Deposit).
            transactionTime (datetime, optional): Transaction time.
            transactionAmount (int, mandatory): Transaction amount.
            transactionStatus (string, optional): Transaction status.
        """
        Transaction.count       += 1
        self._transactionID     = Transaction.count
        self._transactionATM    = transactionATM
        self._transactionCard   = transactionCard
        self._transactionType   = transactionType
        self._transactionTime   = transactionTime
        self._transactionAmount = transactionAmount
        self._transactionStatus = transactionStatus

#%%
    @property
    def transactionID(self):
        return self._transactionID
    
    @transactionID.setter
    def transactionID(self, transactionID):
        self._transactionID = transactionID

    @property
    def transactionATM(self):
        return self._transactionATM
    
    @transactionATM.setter
    def transactionATM(self, transactionATM):
        self._transactionATM = transactionATM

    @property
    def transactionCard(self):
        return self._transactionCard
    
    @transactionCard.setter
    def transactionCard(self, transactionCard):
        self._transactionCard = transactionCard
    
    @property
    def transactionType(self):
        return self._transactionType
    
    @transactionType.setter
    def transactionType(self, transactionType):
        self._transactionType = transactionType

    @property
    def transactionTime(self):
        return self._transactionTime
    
    @transactionTime.setter
    def transactionTime(self, transactionTime):
        self._transactionTime = transactionTime
    
    @property
    def transactionAmount(self):
        return self._transactionAmount
    
    @transactionAmount.setter
    def transactionAmount(self, transactionAmount):
        self._transactionAmount = transactionAmount

    @property
    def transactionStatus(self):
        return self._transactionStatus
    
    @transactionStatus.setter
    def transactionStatus(self, transactionStatus):
        self._transactionStatus = transactionStatus

#%%
    def __str__(self):
        return 'Transaction: [ID: {}, {}, {}, Type: {}, Time: {}, Amount: {}, Status: {}]'\
            .format(
                self._transactionID,
                self._transactionATM,
                self._transactionCard,
                self._transactionType,
                self._transactionTime,
                self._transactionAmount,
                self._transactionStatus
            )
