#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""
Client Class Controller.

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""  

from random import randint, randrange
from models.client import Client 

class Clients():
    """Clients Collection.
    """

#%%
    def __init__(self, maxClients):
        """Clients Collection Default Constructor.

        Args:
            maxClients (int): Maximum number of clients
        """
        self._maxClients = maxClients
        self._clients    = []

#%%
    @property
    def clients(self):
        return self._clients
    
    @clients.setter
    def clients(self, clients):
        self._clients = clients

#%% 
    def createClients(self):
        """Create three clients.
        """
        self._clients = [
            Client(
                987,
                'Juana Mendoza',
                'juana.mendoza@usantoto.edu.co',
                7440404
            ),
            Client(
                654,
                'Alix Chaparro',
                'alix.chaparro@usantoto.edu.co',
                7440404
            ),
            Client(
                321,
                'Martha Contreras',
                'martha.contreras@usantoto.edu.co',
                7440404
            ),
        ]

#%%
    def createRandomClients(self):
        """Create a random Client Collection.
        """
        self._clients = []
        for id in range(randint(1, self._maxClients)):
            client = Client(
                (id + 1),
                "Client {}".format(id + 1),
                "client_{}@email.com".format(id + 1),
                randint(3100000000, 3209999999)
            )
            self._clients.append(client)

#%%
    def randomSelectedClient(self):
        """Selecting an Client.

        Returns:
            Client: The selected Client.
        """
        return self._clients[randrange(len(self._clients))]

#%%
    def __str__(self):
        """Clients output

        Returns:
            String: Output Client string
        """
        output = '[Clients: \n'
        for client in self._clients:
            output += client.__str__() + '\n'
        return output + ']'
