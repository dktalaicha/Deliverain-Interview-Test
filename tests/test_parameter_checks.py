#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:14:22 2020

@author: dinesh
"""

import pytest

import sys 
import os

sys.path.append(os.path.abspath(''))

from parameter_checks import _define_numerical_dict


def test_not_numerical_dict():
    input_dict = {"a": 1, "b": "c"}

    with pytest.raises(ValueError):
        assert _define_numerical_dict(input_dict)


def test_input_type():
    input_dict = [1, 2, 3]

    with pytest.raises(TypeError):
        assert _define_numerical_dict(input_dict)