#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:49:54 2020

@author: dinesh
"""

from pandas.testing import assert_frame_equal
import pytest

import sys 
import os

#sys.path.append(os.path.abspath("/home/dinesh/Data-Science/06-Python/deliverain_python_test/tests"))
sys.path.append(os.path.abspath(''))


from dataframe_checks import (
    _check_contains_na,
    _check_input_matches_training_df,
    _is_dataframe,
)


def test_stock_df_is_dataframe(stock_df):
    assert_frame_equal(_is_dataframe(stock_df), stock_df)
    with pytest.raises(TypeError):
        assert _is_dataframe([1, 2, 4])


def test_check_input_matches_training_df(stock_df):
    with pytest.raises(ValueError):
        assert _check_input_matches_training_df(stock_df, 4)

"""
def test_contains_na(stock_df):
    with pytest.raises(ValueError):
        assert _check_contains_na(stock_df, ["Date","High"])
"""