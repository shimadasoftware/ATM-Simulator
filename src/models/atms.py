#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ATM Class Controller

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""  

from random import randint, randrange
from models.atm import ATM

class ATMs():
    """ATM Collection.
    """

#%%
    def __init__(self, bank, maxATMs, minCash, maxCash, minBill):
        """ATM Collection Default Constructor.

        Args:
            bank (Bank): ATM's Bank.
            maxATMs (int): Number of ATMs to generate.
            minCash (int): Cash minimum of ATM.
            maxCash (int): Cash maximum of ATM.
            minBill (int): Minimum denomination of bills in the ATM.
        """
        self._bank    = bank
        self._maxATMs = maxATMs
        self._minCash = minCash
        self._maxCash = maxCash
        self._minBill = minBill
        self._atms    = []

#%%
    @property
    def atms(self):
        return self._atms
    
    @atms.setter
    def atms(self, atms):
        self._atms = atms

#%%       
    def createATMs(self):
        """Create three ATM instances
        """
        self._atms = [
            ATM (
                1,
                self._bank,
                'Tunja Downtown',
                ['Español', 'English'],
                20000000
            ),
            ATM (
                2,
                self._bank,
                'North Tunja',
                ['Español', 'English'],
                25000000
            ),
            ATM (
                3,
                self._bank,
                'Santoto University',
                ['Español', 'English'],
                10000000
            ),
        ]

#%%
    def createRandomATMs(self):
        """Create a random ATM Collection.
        """
        self._atms = []
        for id in range(randint(1, self._maxATMs)):
            cash = randint(self._minCash, self._maxCash)
            cash -= cash % self._minBill  # Divisible per minBill
            atm = ATM(
                (id + 1),
                self._bank,
                "ATM Address {}".format(id + 1),
                ['Español', 'English'],
                cash
            )
            self._atms.append(atm)

#%%
    def randomSelectedATM(self):
        """Selecting an ATM

        Returns:
            ATM: The selected ATM
        """
        return self._atms[randrange(len(self._atms))]

#%%
    def __str__(self):
        """ATMs output

        Returns:
            String: Output ATM string
        """
        output = '[ATMs: \n'
        for atm in self._atms:
            output += atm.__str__() + '\n'
        return output + ']'
