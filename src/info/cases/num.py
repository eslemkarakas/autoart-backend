# -*- coding: utf-8 -*-
import polars as pl
from scipy.stats import kurtosis

def get_basic_stats(feature_series:pl.Series) -> dict:
    min_val = feature_series.min()
    max_val = feature_series.max()
    std_val = feature_series.std()
    mean_val = feature_series.mean()
    median_val = feature_series.median()

    return {'min':min_val, 'max':max_val, 'std':std_val, 'mean':mean_val, 'median':median_val}

def get_entropy(feature_series:pl.Series) -> dict:
    s_val = feature_series.entropy(normalize=True)

    return {'value':s_val}

def get_kurtosis(feature_series:pl.Series) -> dict:
    kurt_val = float(kurtosis(feature_series.to_numpy(), fisher=False)) # used pearson' definition

    if kurt_val > 3:
        kurt_interpret = 'leptokurtic'
    elif kurt_val < 3:
        kurt_interpret = 'mesokurtic'
    else:
        kurt_interpret = 'platykurtic'

    return {'value':kurt_val, 'interpretation':kurt_interpret} 

def get_skewness(feature_series:pl.Series) -> dict:
    skew_val = feature_series.skew()

    if skew_val > 0:
        skew_interpret = 'right-skewed'
    elif skew_val < 0:
        skew_interpret = 'left-skewed'
    else:
        skew_interpret = 'normal-distribution'

    return {'value':skew_val, 'interpretation':skew_interpret}
