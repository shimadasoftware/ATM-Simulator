#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creation of the Bank

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""  

from models.bank import Bank
 
def createBank():
    """Create the bank

    Returns:
        Bank: The bank
    """
    return Bank(
        123456,
        'My Piggy Bank',
        'Tunja Downtown'
    )
