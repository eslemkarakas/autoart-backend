# -*- coding: utf-8 -*-
from src.platforms.aws.storage.s3 import S3
from src.platforms.aws.database.redshift import Redshift

class Connectors:
    _instances = {}

    def __new__(cls, where:str, *args, **kwargs):
        if where not in cls._instances:
            cls._instances[where] = super(Connectors, cls).__new__(cls)
        
        return cls._instances[where]

    def __init__(self, where:str, configs:dict):
        if not hasattr(self, 'is_initialized'):
            self.where = where
            self.configs = configs
            self.connector = self._create_connector()
            self.is_initialized = True # prevent reinitialization

    def _create_connector(self):
        connector_service_map = {
                                    's3':None,
                                    'rds':None,
                                    'aurora':None,
                                    'dynamodb':None,
                                    'redshift':None,
                                    'timestream':None,
                                }
        
        connector_loader = connector_service_map.get(self.where)
        
        if connector_loader:
            connector = connector_loader(self.configs)
        else:
            raise ValueError(f'[ERROR] Given service is unsupported: {self.where}')

        return connector
    
    def _reset_connector(self, where:str) -> None:
        if where in self._instances:
            del self._instances[where]

    @property
    def get_connector(self):
        return self.connector
