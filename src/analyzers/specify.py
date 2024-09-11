# -*- coding: utf-8 -*-
import numpy as np
import polars as pl

LOW_CARDINALITY_THRESHOLD = 20.
HIGH_CARDINALITY_THRESHOLD = 80.

class CardinalityEvaluator:
    @staticmethod
    def evaluate_feature_cardinality(feature_series:pl.Series, unique_count:int, low_threshold:float = LOW_CARDINALITY_THRESHOLD, high_threshold:float = HIGH_CARDINALITY_THRESHOLD) -> dict:
        uniqueness_rate = unique_count / feature_series.shape[0] * 100

        if uniqueness_rate < low_cardinality:
            level = 'low'
        elif uniqueness_rate > high_cardinality:
            level = 'high'
        else:
            level = 'medium'

        return {'cardinality':{'level':level, 'uniqueness_rate':uniqueness_rate}}

class ScalingEvaluator:
    @staticmethod
    def specify_scaling_technique(algorithm_tags:list):
        if 'distance-based' in algorithm_tags:
            technique = 'normalization'
        elif 'gradient-based' in algorithm_tags:
            technique = 'standardization'
        else:
            pass

    @staticmethod
    def evaluate_feature_scaling(feature_series:pl.Series, explainability_level:str, algorithm_tags:list) -> dict:
        feature_series = feature_series.drop_nulls().drop_nans() # prepare series before calculations
        feature_series = feature_series.to_numpy()

        abs_mean = np.abs(np.mean(feature_series))
        std_dev = np.std(feature_series)

        if 'tree-based' in algorithm_tags:
            do = False
        if abs_mean > 0.5 or std_dev > 1.5:
            do = True
        elif explainability_level == 'high':
            do = True
        else:
            do = False

        return {'scaling':{'do':do}}

