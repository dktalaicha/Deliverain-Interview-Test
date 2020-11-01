#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:33:30 2020

@author: dinesh
"""

# Importing required libraries
import numpy as np
import pandas as pd
import pytest

import sys
from pathlib import Path

"""
Add the parent directory of package to sys.path before attempting to import anything 
from package using absolute imports.
"""
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

from market_abuse_detection import get_stock_data


#from pathlib import Path
#print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())


def test_get_stock_data():
    data = get_stock_data()
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.date)) == 60
    
    
if __name__ == '__main__':
    test_get_stock_data()

    
    
