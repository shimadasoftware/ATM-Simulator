#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Card Class

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""     

from datetime import date
from models.account import Account

class Card():
    """Card Class.
    """

#%%    
    def __init__(self, cardNumber = "", cardAccount = Account(),  
                cardPassword = 0, cardExpirationDate = date, cardPin = 0, cardType = 'Debit'):
        """
        Card default constructor.

        Args:
            cardNumber (int, optional): Card number. Defaults to 0.
            cardAccount (Card, mandatory): Card account. Defaults to Account().
            cardPassword (int, mandatory): Card password. Defaults to 0.
            cardExpirationDate (datetime, optional): Card expiration date. Defaults to datetime.
            cardPin (int, optional): Card pin. Defaults to 0.
            cardType (str, optional): Card type. Defaults to "Debit".
        """
        self._cardNumber         = cardNumber
        self._cardAccount        = cardAccount
        self._cardPassword       = cardPassword
        self._cardExpirationDate = cardExpirationDate
        self._cardPin            = cardPin
        self._cardType           = cardType

#%%
    @property
    def cardNumber(self):
        return self._cardNumber
    
    @cardNumber.setter
    def cardNumber(self, cardNumber):
        self._cardNumber = cardNumber
  
    @property
    def cardAccount(self):
        return self._cardAccount
    
    @cardAccount.setter
    def cardAccount(self, cardAccount):
        self._cardAccount = cardAccount

    @property
    def cardPassword(self):
        return self._cardPassword
    
    @cardPassword.setter
    def cardPassword(self, cardPassword):
        self._cardPassword = cardPassword

    @property
    def cardExpirationDate(self):
        return self._cardExpirationDate
    
    @cardExpirationDate.setter
    def cardExpirationDate(self, cardExpirationDate):
        self._cardExpirationDate = cardExpirationDate

    @property
    def cardPin(self):
        return self._cardPin
    
    @cardPin.setter
    def cardPin(self, cardPin):
        self._cardPin = cardPin

    @property
    def cardType(self):
        return self._cardType
    
    @cardType.setter
    def cardType(self, cardType):
        self._cardType = cardType

#%%
    def __str__(self):
        return 'Card: [Card Number: {}, {}, Card Password: {}, Card Expiration Date: {}, Card Pin: {}, Card type: {}]'\
            .format(
                self._cardNumber, 
                self._cardAccount.__str__(), 
                self._cardPassword, 
                self._cardExpirationDate, 
                self._cardPin,
                self._cardType
            )

