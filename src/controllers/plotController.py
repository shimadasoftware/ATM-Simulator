#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main Controller 

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""

from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import warnings


#%%
def transactionPlot(record):
    """[summary]

    Args:
        record ([type]): [description]
    """
    warnings.filterwarnings('ignore')

    ax = record.transactionDF.status.value_counts().plot(
        kind='bar', title='Transaction status', figsize=(14,8)
    )
    ax.set_xlabel("Status", fontsize=12)
    plt.xticks(rotation=15)
    ax.set_ylabel("Frequency", fontsize=12)
    plt.savefig('figs/tra_freq.png')    
    #plt.show()
    plt.close()
    
    df = record.transactionDF.pivot_table(index='status', columns='transaction', values='amount', aggfunc=['count'])
    df.columns.set_levels(['balance', 'withdraw', 'deposit'], level=1, inplace=True)
    df = df.fillna(0)
    ax = df.plot(
        title='Transaction types and status', figsize=(14,8)
    )
    ax.set_xlabel("Status", fontsize=12)
    plt.xticks(rotation=15)
    ax.set_ylabel("Transaction type", fontsize=12)
    plt.savefig('figs/tran_status_type.png')   
    #plt.show()
    plt.close()

    df = record.transactionDF.pivot_table(index='status', values='amount', aggfunc=['mean'])
    ax = df.plot(
        kind='bar', title='Transaction amount', figsize=(14,8), legend=False
    )
    ax.set_xlabel("Status", fontsize=12)
    plt.xticks(rotation=15)
    ax.set_ylabel("Amount", fontsize=12)
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.savefig('figs/trans_amount.png')
    #plt.show()
    plt.close()

#%%
def clientPlot(record):
    """[summary]

    Args:
        record ([type]): [description]
    """
    warnings.filterwarnings('ignore')

    ax = record.clientDF.client.value_counts().plot(
       kind='bar', title='Client vs Transaction', figsize=(14,8) 
    )
    ax.set_xlabel("Client", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    plt.savefig('figs/client_freq.png')    
    #plt.show()
    plt.close()
    
    df = record.clientDF.pivot_table(index='client', columns='transaction', values='balance', aggfunc=['count'])
    df.columns.set_levels(['balance', 'withdraw', 'deposit'], level=1, inplace=True)
    ax = df.plot(
        title='Client vs Transaction types', figsize=(14,8)
    )
    ax.set_xlabel("Client", fontsize=12)
    ax.xaxis.set_major_locator(mtick.MaxNLocator(integer=True))
    ax.set_ylabel("Transaction type", fontsize=12)
    plt.savefig('figs/client_transaction_type.png')   
    #plt.show()
    plt.close()

    df = record.clientDF.pivot_table(index='client', values='balance', aggfunc=['mean'])
    ax = df.plot(
        kind='bar', title='Client balance', figsize=(14,8), legend=False
    )
    ax.set_xlabel("Client", fontsize=12)
    ax.set_ylabel("Balance", fontsize=12)
    ax.xaxis.set_major_locator(mtick.MaxNLocator(integer=True))
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.savefig('figs/client_balance.png')   
    #plt.show()
    plt.close()

#%%
def atmPlot(record):
    """[summary]

    Args:
        record ([type]): [description]
    """
    warnings.filterwarnings('ignore')

    ax = record.atmDF.atm.value_counts().plot(
        kind='bar', title='ATM vs Transaction', figsize=(14,8)
    )
    ax.set_xlabel("ATM", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    plt.savefig('figs/atm_freq.png')    
    #plt.show()
    plt.close()
    
    df = record.atmDF.pivot_table(index='atm', columns='transaction', values='cash', aggfunc=['count'])
    df.columns.set_levels(['balance', 'withdraw', 'deposit'], level=1, inplace=True)
    ax = df.plot(
        title='ATM vs Transaction types', figsize=(14,8)
    )
    ax.set_xlabel("ATM", fontsize=12)
    ax.set_ylabel("Transaction type", fontsize=12)
    plt.savefig('figs/atm_transaction_type.png')   
    #plt.show()
    plt.close()

    df = record.atmDF.pivot_table(index='atm', values='cash', aggfunc=['mean'])
    ax = df.plot(
        kind='bar', title='ATM cash', figsize=(14,8), legend=False
    )
    ax.set_xlabel("ATM", fontsize=12)
    ax.set_ylabel("Cash", fontsize=12)
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.savefig('figs/atm_cash.png')
    #plt.show()
    plt.close()

#%%
def resultPlots(record):
    """[summary]

    Args:
        record ([type]): [description]
    """
    record.createDataFrames()
    
    atmPlot(record)
    clientPlot(record)
    transactionPlot(record)

