#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:15:09 2020

@author: dinesh
"""

# Importing required libraries
import pandas as pd
import pytest

import sys
from pathlib import Path

# Add the parent directory of package to sys.path before attempting to import anything from package using absolute imports.
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[0]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass


@pytest.fixture(scope='module')
def stock_df():
    return pd.read_pickle('../StockDataClean.pkl')

@pytest.fixture(scope='module')
def traders_df():
    return pd.read_pickle('../TradersDataClean.pkl')