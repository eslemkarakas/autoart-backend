# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

from src.controllers.errors import UnsupportedOptionError

class Encoder(ABC):
    @abstractmethod
    def encode(self, data):
        pass

    @abstractmethod
    def decode(self, data):
        pass

class LabelEncoderMethod(Encoder):
    def __init__(self):
        self.data = None
        self.encoder = LabelEncoder()
    
    def encode(self, data):
        self.data = self.encoder.fit_transform(data)
        return self.data

    def decode(self, data):
        self.data = self.encoder.inverse_transform(data)
        return self.data

class EncoderFactory:
    @staticmethod
    def create_encoder(option):
        if option == 'label':
            return LabelEncoderMethod()
        elif option == 'one-hot':
            return None
        elif option == 'target':
            return None
        else:
            raise UnsupportedOptionError(f'{option} is not supported by AutoArt.')

# define a wrapper function for handling exceptions
def call_encoder(option):
    encoder = None
    try:
        encoder = EncoderFactory.create_encoder(option)
    except Exception as e:
        print(f'{str(e)}')
    return encoder