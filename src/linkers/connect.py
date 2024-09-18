# -*- coding: utf-8 -*-
from src.platforms.aws.storage.s3 import S3
from src.platforms.aws.database.redshift import Redshift

from src.controllers.exceptions import UnsupportedOptionError

class Connectors:
    """
    The 'Connectors' class is a connector factory that contains the connectors of popular databases and storage services 
    on cloud providers. It ensures connections to these services are established using the singleton pattern, which guarantees 
    that only one instance of each connector is created during the application's lifecycle.

    Parameters
    ----------
    where:str
        Specify the target service or database for the connection (e.g., 'aws-s3', 'aws-redshift').

    configs:dict
        Contain the necessary configuration details in a dictionary for establishing the connection to a specific service.

    Raises
    ------
    UnsupportedOptionError
        When the given `where` is not supported.

    Examples
    --------
    >>> conn_obj = Connectors(where='aws-redshift', configs=redshift_configs)
    >>> redshift_conn = conn_obj.get_connector
    >>> redshift_conn.read()
    shape: (2, 1)
    ┌─────┐
    │ foo │
    │ --- │
    │ i64 │
    ╞═════╡
    │ 123 │
    │ 456 │
    └─────┘

    This connector can have read, write, delete or update methods and operation result is depending on the underlying connector and configuration.
    """
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
                                    'aws-s3':None,
                                    'aws-rds':None,
                                    'aws-aurora':None,
                                    'aws-dynamodb':None,
                                    'aws-redshift':Redshift(configs=self.configs),
                                    'aws-timestream':None,
                                }

        connector_loader = connector_service_map.get(self.where)

        if connector_loader:
            connector = connector_loader(self.configs)
        else:
            raise UnsupportedOptionError(f'{self.where} is not supported by AutoArt.')

        return connector
    
    def _reset_connector(self, where:str) -> None:
        if where in self._instances:
            del self._instances[where]

    @property
    def get_connector(self):
        return self.connector
