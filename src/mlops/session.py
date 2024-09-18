# -*- coding: utf-8 -*-
import os 
import threading
import mlflow

from src.controllers.exceptions import UnsupportedOptionError

class MLFlowSession:
    _session = None
    _lock = threading.Lock()

    def __new__(cls, stage:str, product:str = None):
        if cls._session is None:
            with cls._lock:
                cls._session = super(MLFlowSession, cls).__new__(cls)
                cls._session._initialize_session(stage=stage, product=product)

        return cls._session

    def _initialize_session(self, stage:str, product:str = None):
        if stage == 'dev':
            mlflow.set_tracking_uri('file:///' + os.path.abspath('mlruns'))
        elif stage == 'prod':
            if product == None:
                product = input('Enter product name: ')

            mlflow.set_tracking_uri(product)
        else:
            raise UnsupportedOptionError(rf"{stage} is not supported by AutoArt. Choose 'dev' or 'prod' as the stage.")

    def get_info_about_active_session(self):
        print(mlflow.get_tracking_uri())

    @classmethod
    def reset_session(cls):
        with cls._lock:
            if cls._session is not None:
                cls._session = None

    @classmethod
    def switch_session(cls, stage:str, product:str = None):
        cls.reset_session()

        return cls(stage, product)
