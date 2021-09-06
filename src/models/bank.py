#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 14:16:44 2021
 
Version: 1.0

Universidad Santo Tomás Tunja

Simulation

@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez

presented to: Martha Susana Contreras Ortiz
"""     

class Bank():
    """
    Bank class.
    
    """ 

    def __init__(self, bankID = 0, bankName = "", bankAddress = ""):
        """
        Bank default constructor.

        Args:
            bankID (int, mandatory): Bank identifier. Defaults to 0.
            bankName (str, optional): Bank commercial brand. Defaults to "".
            bankAddress (str, optional): Bank address. Defaults to "".
        """
        self._bankID      = bankID
        self._bankName    = bankName
        self._bankAddress = bankAddress
    
    @property
    def bankID(self):
        return self._bankID
    
    @bankID.setter
    def bankID(self, bankID):
        self._bankID = bankID
    
    @property
    def bankName(self):
        return self._bankName
    
    @bankName.setter
    def bankName(self, bankName):
        self._bankName = bankName
    
    @property
    def bankAddress(self):
        return self._bankAddress
    
    @bankAddress.setter
    def bankAddress(self, bankAddress):
        self._bankAddress = bankAddress
    
    def __str__(self):
        return 'Bank: [ID: {}, Name: {}, Address: {}]'\
            .format(
                self._bankID, 
                self._bankName, 
                self._bankAddress
            )
        
