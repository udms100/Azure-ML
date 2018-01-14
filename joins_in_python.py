#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:39:18 2018

@author: xerxes
"""

## function to join automotive data 

def auto_join(autos, make):
    import pandas as pd
    on = ['autonum']
    return pd.merge(auto, makes on = on, how = 'left)
    

## perform the join in Azure machine learning 

def azureml_main(autos, makes):
    return auto_join(autos, makes)