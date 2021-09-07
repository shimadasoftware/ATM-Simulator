#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Client Class.

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""     

class Client():
    """Client class.
    """

    def __init__(self, clientID = 0, clientName = "", clientEmail = "", clientPhone = 0):
        """
        Client default constructor.

        Args:
            clientID (int, mandatory): Client identifier. Defaults to 0.
            clientName (str, mandatory): Client name. Defaults to "".
            clientEmail (str, optional): Client email. Defaults to "".
            clientPhone (int, optional): Client phone. Defaults to 0.
        """
        self._clientID    = clientID
        self._clientName  = clientName
        self._clientEmail = clientEmail
        self._clientPhone = clientPhone
    
    @property
    def clientID(self):
        return self._clientID
    
    @clientID.setter
    def clientID(self, clientID):
        self._clientID = clientID
    
    @property
    def clientName(self):
        return self._clientName
    
    @clientName.setter
    def clientName(self, clientName):
        self._clientName = clientName
    
    @property
    def clientEmail(self):
        return self._clientEmail
    
    @clientEmail.setter
    def clientEmail(self, clientEmail):
        self._clientEmail = clientEmail

    @property
    def clientPhone(self):
        return self._clientPhone
    
    @clientPhone.setter
    def clientPhone(self, clientPhone):
        self._clientPhone = clientPhone

    def __str__(self):
        return 'Client: [ID: {}, Name: {}, Email: {}, Phone: {}]'\
            .format(
                self._clientID, 
                self._clientName, 
                self._clientEmail, 
                self._clientPhone
            )
