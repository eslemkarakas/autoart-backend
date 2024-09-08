# -*- coding: utf-8 -*-
import polars as pl

class StoragePatternIdentifier:
    pass
        
class FeatureTypeIdentifier:
    @staticmethod
    def _is_binary(feature_series: pl.Series, unique_count:int) -> bool:
        return unique_count == 2

    @staticmethod
    def _is_primary_key(feature_series: pl.Series, unique_count:int) -> bool:
        return unique_count == feature_series.shape[0]
    
    @staticmethod
    def get_type(feature_series:pl.Series) -> dict:
        feature_info = {}
        feature_dtype = feature_series.dtype
        unique_count = feature_series.n_unique()

        feature_info['dtype'] = feature_series.dtype

        if isinstance(feature_dtype, (pl.Decimal, pl.Int8, pl.Int16, pl.Int32, pl.Int64, pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64, pl.Float32, pl.Float64)):
            feature_info['is_numeric'] = True

            #
        elif isinstance(feature_dtype, (pl.Utf8, pl.String, pl.Enum, pl.Categorical)):
            feature_info['is_string'] = True

            #
        elif isinstance(feature_dtype, (pl.Array, pl.List, pl.Struct)):
            feature_info['is_temporal'] = True

            #
        elif isinstance(feature_dtype, (pl.Date, pl.Datetime, pl.Duration, pl.Time)):
            feature_info['is_nested'] = True

            #
        else:
            raise

        return feature_info
