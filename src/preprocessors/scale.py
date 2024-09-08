# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler, PowerTransformer

class Scaler(ABC):
    @abstractmethod
    def scale(self, data):
        pass

class MinMaxScalerMethod(Scaler):
    def __init__(self):
        self.data = None
        self.scaler = MinMaxScaler()
    
    def scale(self, data):
        self.data = self.scaler.fit_transform(data)
        return self.data
    
class StandardScalerMethod(Scaler):
    def __init__(self):
        self.data = None
        self.scaler = StandardScaler()
    
    def scale(self, data):
        self.data = self.scaler.fit_transform(data)
        return self.data

class RobustScalerMethod(Scaler):
    def __init__(self):
        self.data = None
        self.scaler = RobustScaler()
        
    def scale(self, data):
        self.data = self.scaler.fit_transform(data)
        return self.data
    
class MaxAbsScalerMethod(Scaler):
    def __init__(self):
        self.data = None
        self.scaler = MaxAbsScaler()
    
    def scale(self, data):
        self.data = self.scaler.fit_transform(data)
        return self.data

class ScalerFactory:
    @staticmethod
    def create_scaler(option):
        if option == 'min-max':
            return MinMaxScalerMethod()
        elif option == 'standard':
            return StandardScalerMethod()
        elif option == 'robust':
            return RobustScalerMethod()
        elif option == 'max-abs':
            return MaxAbsScalerMethod()
        else:
            raise
    
def call_scaler(option):
    scaler = None
    try:
        scaler = ScalerFactory.create_scaler(option)
    except Exception as e:
        print(f'{str(e)}')
    return scaler