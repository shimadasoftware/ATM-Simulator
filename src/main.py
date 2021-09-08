#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main 

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
""" 
from controllers.settings import config
from controllers.mainController import mainController

if __name__ == "__main__":
    simulator = config.PARAMETERS['simulator']
    mainController(simulator)   # True (simulation) - False (Demo)