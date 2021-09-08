#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cards Class Controller 

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
from models.card import Card

class Cards():
    """Cards Collection.
    """

#%%
    def __init__(self, account, maxCards):
        """Cards Collection Default Constuctor.

        Args:
            account (Account): Card account.
            maxCards (int): Maximum number of cards.
        """
        self._account  = account
        self._maxCards = maxCards
        self._cards    = []

#%%
    @property
    def account(self):
        return self._account
    
    @account.setter
    def account(self, account):
        self._account = account

#%%
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = cards

#%%
    def createCards(self):
        """Create two cards.
        """
        self._cards = [
            Card (
                123456789,
                self._account,
                1234,
                datetime(2030, 1, 1),
                1234,
                'Credit'
            ),
            Card (
                132456789,
                self._account,
                1234,
                datetime(2028, 1, 1),
                1234,
                'Debit'
            )
        ]

#%%
    def createRandomCards(self):
        """Create a random cards collection.
        """
        self._cards = []
        cardType = 'Credit' if randint(0, 1) == 0 else 'Debit'
        year = datetime.today().year + randint(1, 10)
        for id in range(self._maxCards):
            card = Card(
                (id + 1),
                self._account,
                randint(1000, 9999),
                datetime(year, 1, 1),
                randint(1000, 9999),
                cardType
            )
            self._cards.append(card)

#%%
    def randomSelectedCard(self, account):
        """Selecting a Card.

        Args:
            account (Account): Client account.

        Returns:
            Card: The selected Card.
        """
        tmpList = []
        for card in self._cards:
            if card.cardAccount == account:
                tmpList.append(card)
        
        if len(tmpList) > 0:
            return tmpList[randrange(len(tmpList))]
        else:
            return self._cards[randrange(len(self._cards))]

#%%
    def __str__(self):
        """Cards output.

        Returns:
            String: Output Card string.
        """
        output = '[Cards: \n'
        for card in self._cards:
            output += card.__str__() + '\n'
        return output + ']'
