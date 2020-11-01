#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:33:06 2020

@author: dinesh
"""

# Importing required libraries
import numpy as np
import pandas as pd

# For reading stock data from yahoo
import pandas_datareader.data as pdr

# For time stamps
from datetime import datetime


# Supressing the warning messages
import warnings
warnings.filterwarnings('ignore')


# Stock Dataset
# Import Stock Dataset
#Downloading Amazon stock data from Yahoo for the months of February and March 2020

def get_stock_data(filename='stock_data.csv',stock = "AMZN", start_date = '2020-02-01',end_date = '2020-03-31',
                   force_download=False):
    """
    Download and cache the stock data
    
    Parameters
    ----------
    filename : string (optional)
        location to save the data
    stock : string (optional)
        company name of which stock data want to download from yahoo api.
    start_date : string (optional)
        date from where stock data should download
    end_date : string (optional)
        date till where stock data should download
    force_download : bool (optional)
        if True, force re-download of data from Yahoo API else read from local
        
    Returns
    -------
    data : pandas.DataFrame
        The company Stock data
    """
    
    if force_download:
        # Grabing yahoo finance data and setting as a dataframe
        stock_data = pdr.DataReader(stock, 'yahoo', start_date, end_date)
        # Save the stock data in form of .csv to local 
        stock_data.to_csv(filename)
        
    # force_download is false, then read data from local
    stock_data = pd.read_csv(filename, index_col='Date')

    try:
        stock_data.index = pd.to_datetime(stock_data.index, format='%Y-%m-%d')
    except TypeError:
        stock_data.index = pd.to_datetime(stock_data.index)

    return stock_data

# Print docstrings of method 
print(get_stock_data.__doc__)


# collect data for Amazon from 2020-02-01 to 2020-03-31
stock_data = get_stock_data(filename='stock_data.csv',stock = "AMZN", 
                            start_date = '2020-02-01',end_date = '2020-03-31',force_download=True)

# Looking at sample rows in the data
stock_data.head()