# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:54:55 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    Qxprice = df['Unit price']*df['Quantity']
    df.insert(7,'Qxprice',Qxprice)    

solve()

print(df.loc[0:2,'Unit price':'Total'])