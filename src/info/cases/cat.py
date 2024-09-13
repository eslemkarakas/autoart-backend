# -*- coding: utf-8 -*-
import polars as pl

LOW_CARDINALITY_THRESHOLD = 20.
HIGH_CARDINALITY_THRESHOLD = 80.

def evaluate_cardinality(feature_series:pl.Series, low_threshold:float = LOW_CARDINALITY_THRESHOLD, high_threshold:float = HIGH_CARDINALITY_THRESHOLD) -> dict:
    uniqueness_rate = feature_series.n_unique() / feature_series.shape[0] * 100

    if uniqueness_rate < low_cardinality:
        level = 'low'
    elif uniqueness_rate > high_cardinality:
        level = 'high'
    else:
        level = 'medium'

    return {'level':level, 'uniqueness_rate':uniqueness_rate}
