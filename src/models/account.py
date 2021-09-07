#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Account Class

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""     

from models.client import Client

class Account():
    """Account Class.
    """

    def __init__(self, accountNumber = 0, accountClient = Client(),
                accountType = "Savings", accountBalance = 0):
        """
        Account default constructor.

        Args:
            accountNumber (int, mandatory): Account accountNumber. Defaults to 0.
            accountClient ([Client, mandatory): [description]. Defaults to Client().
            accountType (str, mandatory): Account type. Defaults to "".
            accountBalance (int, mandatory): Account accountBalance. Defaults to 0.
        """
        self._accountNumber  = accountNumber
        self._accountClient  = accountClient
        self._accountType    = accountType
        self._accountBalance = accountBalance

    @property
    def accountNumber(self):
        return self._accountNumber
    
    @accountNumber.setter
    def accountNumber(self, accountNumber):
        self._accountNumber = accountNumber
  
    @property
    def accountClient(self):
        return self._accountClient
    
    @accountClient.setter
    def accountClient(self, accountClient):
        self._accountClient = accountClient

    @property
    def accountType(self):
        return self._accountType
    
    @accountType.setter
    def accountType(self, accountType):
        self._accountType = accountType
    
    @property
    def accountBalance(self):
        return self._accountBalance
    
    @accountBalance.setter
    def accountBalance(self, accountBalance):
        self._accountBalance = accountBalance

    def __str__(self):
        return 'Account: [accountNumber: {}, {}, Account Type: {}, accountBalance: {}]'\
            .format(
                self._accountNumber, 
                self._accountClient.__str__(),
                self._accountType, 
                self._accountBalance
            )
        
