# -*- coding: utf-8 -*-
import polars as pl

def is_empty(feature_series:pl.Series) -> bool:
    return feature_series.is_empty()

def is_unique(feature_series:pl.Series) -> bool:
    return feature_series.n_unique() == feature_series.shape[0]

def is_constant(feature_series:pl.Series) -> bool:
    return feature_series.n_unique() == 1
