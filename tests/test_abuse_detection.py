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


"""Check that number of rows in traders dataset and final merged datasets are same.""" 
def test_check_rows_count(traders_df,market_data_label_df):
    dt.validate(traders_df.shape[0],market_data_label_df.shape[0])
    