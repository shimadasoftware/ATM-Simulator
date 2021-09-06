#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATM Class.

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""     

from models.bank import Bank

class ATM():
    """
    ATM Class. 
 
    """

    def __init__(self, atmID = 0, atmBank = Bank(), atmAddress = "", 
                atmLanguage = ["Español", "English"], atmCash = 0):
        """
        Automatic Teller Machine - ATM default constructor.

        Args:
            atmID (int, mandatory): ATM identifier. Defaults to 0.
            atmBank (Bank, mandatory): ATM Bank. Defaults to NULL.
            atmAddress (str, optional): ATM address. Defaults to "".
            atmLanguage (str, optional): ATM language. Defaults to [""].
            atmCash (int, mandatory): ATM cash. Defaults to 0.
        """
        self._atmID          = atmID
        self._atmBank        = atmBank
        self._atmAddress     = atmAddress
        self._atmLanguage    = atmLanguage
        self._atmCash        = atmCash
    
    @property
    def atmID(self):
        return self._atmID
    
    @atmID.setter
    def atmID(self, atmID):
        self._atmID = atmID
    
    @property
    def atmBank(self):
        return self._atmBank
    
    @atmBank.setter
    def atmBank(self, atmBank):
        self._atmBank = atmBank

    @property
    def atmAddress(self):
        return self._atmAddress
    
    @atmAddress.setter
    def atmAddress(self, atmAddress):
        self._atmAddress = atmAddress
    
    @property
    def atmLanguage(self):
        return self._atmLanguage
    
    @atmLanguage.setter
    def atmLanguage(self, atmLanguage):
        self._atmLanguage = atmLanguage

    @property
    def atmCash(self):
        return self._atmCash
    
    @atmCash.setter
    def atmCash(self, atmCash):
        self._atmCash = atmCash
    
    def __str__(self):
        return 'ATM: [ID: {}, {}, atmAddress: {}, atmLanguage: {}, atmCash: {}]'\
            .format(
                self._atmID, 
                self._atmBank.__str__(), 
                self._atmAddress, 
                self._atmLanguage, 
                self._atmCash
            )
