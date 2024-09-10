# -*- coding: utf-8 -*-
from src.controllers.log import access_layer_logger, service_layer_logger, serve_layer_logger, monitor_layer_logger 

class AutoArtAPIError(Exception):
    def __init__(self, message:str):
        super(AutoArtServiceError, self).__init__(message)
        access_layer_logger.error(message)

class UnsupportedOptionError(AutoArtAPIError):
    def __init__(self, message:str):
        super(UnsupportedOptionError, self).__init__(message)
        access_layer_logger.error(message)

class InvalidConfigurationError(AutoArtAPIError):
    def __init__(self, message:str):
        super(InvalidConfigurationError, self).__init__(message)
        access_layer_logger.error(message)

class AuthenticationError(AutoArtAPIError):
    def __init__(self, message:str):
        super(AuthenticationError, self).__init__(message)
        access_layer_logger.error(message)

class AuthorizationError(AutoArtAPIError):
    def __init__(self, message:str):
        super(AuthorizationError, self).__init__(message)
        access_layer_logger.error(message)


class AutoArtServiceError(Exception):
    def __init__(self, message:str):
        super(AutoArtServiceError, self).__init__(message)
        service_layer_logger.error(message)

class RequestTimeoutError(AutoArtServiceError):
    def __init__(self, message:str):
        super(RequestTimeoutError, self).__init__(message)
        service_layer_logger.error(message)

class NotTrainedError(AutoArtServiceError):
    def __init__(self, message:str):
        super(NotTrainedError, self).__init__(message)
        service_layer_logger.error(message)

class DataManipulationError(AutoArtServiceError):
    def __init__(self, message:str):
        super(DataManipulationError, self).__init__(message)
        service_layer_logger.error(message)

class ParameterSpaceError(AutoArtServiceError):
    def __init__(self, message:str):
        super(ParameterSpaceError, self).__init__(message)
        service_layer_logger.error(message)
