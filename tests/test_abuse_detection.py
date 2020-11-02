#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:33:30 2020

@author: dinesh
"""

# Importing required libraries
import numpy as np
import pandas as pd
import datatest as dt
from datetime import datetime
import pytest

@pytest.mark.mandatory
def test_stock_columns(stock_df):
    dt.validate(
        stock_df.columns,
        {'Date','High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'},
    )

    
def test_stock_data_types(stock_df):
    dt.validate(stock_df['Date'], datetime)
    dt.validate(stock_df['High'], float)
    dt.validate(stock_df['Low'], float)
    dt.validate(stock_df['Open'], float)
    dt.validate(stock_df['Close'], float)
    dt.validate(stock_df['Volume'], int)
    dt.validate(stock_df['Adj Close'], float)
    

def test_stock_unique_data(stock_df):
    assert len(np.unique(stock_df['Date'])) == 42


@pytest.mark.mandatory
def test_traders_columns(traders_df):
    dt.validate(
        traders_df.columns,
        {'countryCode', 'firstName', 'lastName', 'traderId', 'stockSymbol',
       'stockName', 'tradeId', 'price', 'volume', 'tradeDate'},
    )

"""Check that values are of the given type. """ 
def test_traders_data_types(traders_df):
    #dt.validate(traders_df['countryCode'], str())
    dt.validate(traders_df['firstName'], str)
    dt.validate(traders_df['lastName'], str)
    dt.validate(traders_df['traderId'], str)
    dt.validate(traders_df['stockSymbol'], str)
    dt.validate(traders_df['stockName'], str)
    dt.validate(traders_df['tradeId'], str)
    dt.validate(traders_df['price'], float)
    dt.validate(traders_df['volume'], float)
    dt.validate(traders_df['tradeDate'], datetime)
 
def test_unique_tradeId(traders_df):
    dt.validate.unique(traders_df['tradeId'])


"""
def test_get_stock_data(stock_data):
    assert isinstance(stock_data.index, pd.DatetimeIndex)
    assert all(stock_data.columns == ['Date','High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'])
    assert isinstance(stock_data.index, pd.DatetimeIndex)
    assert len(np.unique(stock_data.index.date)) == 42
    
  

def test_stock_data_duplicate():
    assert stock_data[stock_data.duplicated() == True]
    
def test_something_works(stock_data): # snapshot is a pytest fixture from snapshottest
    stock_data.assert_match(data_frame.to_csv(index=False), 'some_module_level_unique_name_for_the_snapshot')
    


if __name__ == '__main__':
    test_get_stock_data()

"""
    
