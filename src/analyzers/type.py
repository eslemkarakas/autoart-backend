# -*- coding: utf-8 -*-
import polars as pl
from scipy.stats import kurtosis

LOW_CARDINALITY_THRESHOLD = 20.
HIGH_CARDINALITY_THRESHOLD = 80.

class TextInfoMethods:
    pass

class CategoricalInfoMethods:
    @staticmethod
    def evaluate_cardinality(feature_series:pl.Series, low_threshold:float = LOW_CARDINALITY_THRESHOLD, high_threshold:float = HIGH_CARDINALITY_THRESHOLD) -> dict:
        uniqueness_rate = feature_series.n_unique() / feature_series.shape[0] * 100

        if uniqueness_rate < low_cardinality:
            level = 'low'
        elif uniqueness_rate > high_cardinality:
            level = 'high'
        else:
            level = 'medium'

        return {'level':level, 'uniqueness_rate':uniqueness_rate}

class NumericalInfoMethods:
    @staticmethod
    def get_basic_stats(feature_series:pl.Series) -> dict:
        min_val = feature_series.min()
        max_val = feature_series.max()
        std_val = feature_series.std()
        mean_val = feature_series.mean()
        median_val = feature_series.median()

        return {'min':min_val, 'max':max_val, 'std':std_val, 'mean':mean_val, 'median':median_val}

    @staticmethod
    def get_entropy(feature_series:pl.Series) -> dict:
        s_val = feature_series.entropy(normalize=True)

        return {'value':s_val}

    @staticmethod
    def get_kurtosis(feature_series:pl.Series) -> dict:
        kurt_val = float(kurtosis(feature_series.to_numpy(), fisher=False)) # used pearson' definition

        if kurt_val > 3:
            kurt_interpret = 'leptokurtic'
        elif kurt_val < 3:
            kurt_interpret = 'mesokurtic'
        else:
            kurt_interpret = 'platykurtic'

        return {'value':kurt_val, 'interpretation':kurt_interpret} 

    @staticmethod
    def get_skewness(feature_series:pl.Series) -> dict:
        skew_val = feature_series.skew()

        if skew_val > 0:
            skew_interpret = 'right-skewed'
        elif skew_val < 0:
            skew_interpret = 'left-skewed'
        else:
            skew_interpret = 'normal-distribution'

        return {'value':skew_val, 'interpretation':skew_interpret}

class EdgeCaseInfoMethods:
    @staticmethod
    def is_empty(feature_series:pl.Series) -> bool:
        return feature_series.is_empty()

    @staticmethod
    def is_unique(feature_series:pl.Series, unique_count:int) -> bool:
        return unique_count == feature_series.shape[0]

    @staticmethod
    def is_constant(unique_count:int) -> bool:
        return unique_count == 1

    @staticmethod
    def is_binary(unique_count:int) -> bool:
        return unique_count == 2

class FeatureInfo:
    def __init__(self, df:pl.DataFrame):
        self.info = {}
        self.num_info = NumericalInfoMethods()
        self.cat_info = CategoricalInfoMethods()
        self.text_info = TextInfoMethods()
        self.edge_info = EdgeCaseInfoMethods()

    def _get_instructions(self):
        pass

    def analyze_series(self, fs:pl.Series) -> dict:
        return info

    def analyze_dataframe(self, df:pl.DataFrame) -> dict:
        return info
