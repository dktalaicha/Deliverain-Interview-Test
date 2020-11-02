#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:35:10 2020

@author: dinesh
"""

import pytest

import sys 
import os

#sys.path.append(os.path.abspath("/home/dinesh/Data-Science/06-Python/deliverain_python_test/tests"))
sys.path.append(os.path.abspath(''))

from variable_manipulation import (
    _find_all_variables,
    _find_categorical_variables,
    _find_numerical_variables,
)



def test_find_numerical_variables(traders_df):
    vars_num = ["price", "volume"]
    vars_mix = ["tradeDate", "traderId", "price"]
    vars_none = None

    assert _find_numerical_variables(traders_df, vars_num) == vars_num
    assert _find_numerical_variables(traders_df, vars_none) == vars_num

    with pytest.raises(TypeError):
        assert _find_numerical_variables(traders_df, vars_mix)

    with pytest.raises(ValueError):
        assert _find_numerical_variables(traders_df[["price", "volume"]], None)


def test_find_categorical_variables(traders_df):
    vars_cat = ["countryCode", "firstName","lastName"]
    vars_mix = ["tradeDate", "traderId", "price"]
    vars_none = None

    assert _find_categorical_variables(traders_df, vars_cat) == vars_cat
    assert _find_categorical_variables(traders_df, vars_none) == vars_cat

    with pytest.raises(TypeError):
        assert _find_categorical_variables(traders_df, vars_mix)

    with pytest.raises(ValueError):
        assert _find_categorical_variables(traders_df[["price", "volume"]], None)


def test_find_all_variables(traders_df):
    all_vars = ['countryCode', 'firstName', 'lastName', 'traderId', 'stockSymbol','stockName', 'tradeId', 'price', 'volume', 'tradeDate']
    user_vars = ["countryCode", "firstName","lastName"]
    

    assert _find_all_variables(traders_df) == all_vars
    assert _find_all_variables(traders_df, ["countryCode", "firstName","lastName"]) == user_vars

