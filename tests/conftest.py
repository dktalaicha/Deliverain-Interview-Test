#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:48:26 2020

@author: dinesh
"""

import pytest

@pytest.fixture
def supply_stock_details():
	# The Amazon stock we'll use for the analysis
    stock = "AMZN"

    # Set up Start and End dates for data grab
    start_date = '2020-02-01'
    end_date = '2020-03-31'
    
    return [stock,start_date,end_date]
