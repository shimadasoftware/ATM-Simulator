#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Statisticals Controller.

Created on Tue Aug 17 14:16:44 2021
Version: 1.0
Universidad Santo Tomás Tunja
Simulation
@author: Juana Valentina Mendoza Santamaría
@author: Alix Ivonne Chaparro Vasquez
presented to: Martha Susana Contreras Ortiz
"""

#%%
def stats(record):
    """[summary]

    Args:
        record ([type]): [description]
    """

    record.createDataFrames()

    print('\n' + '=' * 105)
    print('ATMs stats:')
    print(
        '{}\t{:^12}\t{:^12}\t{:^12}\t{}\t{}\t{}\t{}\t{}'.format(
            'ATM', 'Mean', 'Min', 'Max', 'Number', 'Balance', 'Withdra', 'Deposit', 'Success'
        )
    )
    for atm in sorted(record.atmDF.atm.unique(), key=int):
        print(
            '{:>2}\t${:>11,.0f}\t${:>11,.0f}\t${:>11,.0f}\t{:>6,}\t{:>6,}\t{:>6,}\t{:>6,}\t{:>6,}'.format(
                atm,
                record.atmDF[record.atmDF.atm == atm].cash.mean(),
                record.atmDF[record.atmDF.atm == atm].cash.min(),
                record.atmDF[record.atmDF.atm == atm].cash.max(),
                record.atmDF[record.atmDF.atm == atm].transaction.count(),
                record.atmDF[
                    (record.atmDF.atm == atm) & (record.atmDF.transaction == 1)
                ].transaction.count(),
                record.atmDF[
                    (record.atmDF.atm == atm) & (record.atmDF.transaction == 2)
                ].transaction.count(),
                record.atmDF[
                    (record.atmDF.atm == atm) & (record.atmDF.transaction == 3)
                ].transaction.count(),
                record.atmDF[
                    (record.atmDF.atm == atm) & (record.atmDF.status == 'Successful')
                ].transaction.count()
            )
        )
    print()

    print('\n' + '=' * 105)
    print('Clients stats:')
    print(
        '{}\t{}\t{:^12}\t{:^12}\t{:^12}\t{}\t{}\t{}\t{}\t{}'.format(
            'Client', 'Account', 'Mean', 'Min', 'Max', 'Number', 'Balance', 'Withdra', 'Deposit', 'Success'
        )
    )
    for longAccount in sorted(record.clientDF.longAccount.unique(), key=int):
        client  = int(longAccount.split('_')[0])
        account = int(longAccount.split('_')[1])
        print(
            '{:>2}\t{:>2}\t${:>11,.0f}\t${:>11,.0f}\t${:>11,.0f}\t{:>6,}\t{:>6,}\t{:>6,}\t{:>6,}\t{:>6,}'.format(
                client,
                account, 
                record.clientDF[
                    (record.clientDF.client == client) & (record.clientDF.account == account)
                ].balance.mean(),
                record.clientDF[
                    (record.clientDF.client == client) & (record.clientDF.account == account)
                ].balance.min(),
                record.clientDF[
                    (record.clientDF.client == client) & (record.clientDF.account == account)
                ].balance.max(),
                record.clientDF[
                    (record.clientDF.client == client) & (record.clientDF.account == account)
                ].transaction.count(),
                record.clientDF[
                    (record.clientDF.client == client) & 
                    (record.clientDF.account == account) & 
                    (record.clientDF.transaction == 1)
                ].transaction.count(),
                record.clientDF[
                    (record.clientDF.client == client) & 
                    (record.clientDF.account == account) & 
                    (record.clientDF.transaction == 2)
                ].transaction.count(),
                record.clientDF[
                    (record.clientDF.client == client) & 
                    (record.clientDF.account == account) & 
                    (record.clientDF.transaction == 3)
                ].transaction.count(),
                record.clientDF[
                    (record.clientDF.client == client) & 
                    (record.clientDF.account == account) & 
                    (record.clientDF.status == 'Successful')
                ].transaction.count()
            )
        )
    print()

    print('\n' + '=' * 105)
    print('Transactions stats:')
    print(
        '{:^38}\t{:^12}\t{:^12}\t{:^12}\t{}\t{}\t{}\t{}'.format(
            'Status', 'Mean', 'Min', 'Max', 'Number', 'Balance', 'Withdra', 'Deposit'
        )
    )
    for transaction in sorted(record.transactionDF.status.unique()):
        print(
            '{:<38}\t${:>11,.0f}\t${:>11,.0f}\t${:>11,.0f}\t{:>6,}\t{:>6,}\t{:>6,}\t{:>6,}'.format(
                transaction, 
                record.transactionDF[record.transactionDF.status == transaction].amount.mean(),
                record.transactionDF[record.transactionDF.status == transaction].amount.min(),
                record.transactionDF[record.transactionDF.status == transaction].amount.max(),
                record.transactionDF[record.transactionDF.status == transaction].transaction.count(),
                record.transactionDF[
                    (record.transactionDF.status == transaction) & 
                    (record.transactionDF.transaction == 1)
                ].transaction.count(),
                record.transactionDF[
                    (record.transactionDF.status == transaction) & 
                    (record.transactionDF.transaction == 2)
                ].transaction.count(),
                record.transactionDF[
                    (record.transactionDF.status == transaction) & 
                    (record.transactionDF.transaction == 3)
                ].transaction.count(),
            )
        )
    print()
