# -*- coding: utf-8 -*-
import polars as pl
from typing import Tuple

LOW_CARDINALITY_THRESHOLD = 20.
HIGH_CARDINALITY_THRESHOLD = 80.

class CardinalityLevelSpecifier:
    @staticmethod
    def _specify_cardinality_level(feature_series:pl.Series, unique_count:int, low_threshold:float = LOW_CARDINALITY_THRESHOLD, high_threshold:float = HIGH_CARDINALITY_THRESHOLD) -> Tuple['str', 'float']:
        uniqueness_rate = unique_count / feature_series.shape[0] * 100

        if uniqueness_rate < low_cardinality:
            return 'Low Cardinality', uniqueness_rate
        elif uniqueness_rate > high_cardinality:
            return 'High Cardinality', uniqueness_rate
        else:
            return 'Medium Cardinality', uniqueness_rate
