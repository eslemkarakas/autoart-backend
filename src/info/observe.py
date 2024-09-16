# -*- coding: utf-8 -*-
import polars as pl

import src.info.cases.num as num
import src.info.cases.cat as cat
import src.info.cases.edge as edge
import src.info.cases.text as text

class Observer:
    def __init__(self):
        self.info = {}
        self.f_info = {}

    def _get_instructions(self):
        pass

    def _check_edge_cases(self, feature_series:pl.Series) -> bool:
        checks = {
                'empty':edge.is_empty,
                'unique':edge.is_unique,
                'constant':edge.is_constant,
                }

        for key, func in checks.items():
            if func(feature_series):
                self.f_info['scope'] = 'out'
                self.f_info['due'] = key
                return True

        return False

    def analyze_series(self, feature_series:pl.Series) -> dict:
        if self._check_edge_cases(feature_series):
            return self.f_info

        return self.f_info

    def analyze_dataframe(self, dataframe:pl.DataFrame) -> dict:
        print(dataframe)
        for col in dataframe.columns:
            self.info[col] = self.analyze_series(feature_series=dataframe[col])
            self.f_info = {} # reinitialize feature info

        return self.info
