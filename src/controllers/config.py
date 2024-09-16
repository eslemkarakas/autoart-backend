# -*- coding: utf-8 -*-
import os
from typing import List, Union, Literal

from src.controllers.exceptions import UnsupportedOptionError

class LocalConfig:
    def __init__(self, filename:str):
        self.configs = {}
        self.full_path = os.path.join(os.getcwd(), filename)
        self.extension = filename.split('.')[-1]

    def _from_ini(self) -> None:
        import configparser

        config_obj = configparser.ConfigParser()
        config_obj.read(self.full_path)
        configs = {}
        for section in config_obj.sections():
            configs[section] = {}
            for key, value in config_obj.items(section):
                configs[section][key] = value

        self.configs = configs

    def _from_env(self) -> None:
        from dotenv import dotenv_values

        env_vars = dotenv_values(self.full_path) # return OrderedDict
        configs = dict(env_vars)

        self.configs = configs

    def _from_yaml(self) -> None:
        import yaml

        with open(self.full_path, 'r') as yaml_file:
            configs = yaml.safe_load(yaml_file)

        self.configs = configs

    def _from_json(self) -> None:
        import json

        with open(self.full_path, 'r') as json_file:
            configs = json.load(json_file)

        self.configs = configs

    def load_configs(self) -> None:
        config_source_map = {
                                'ini':self._from_ini,
                                'env':self._from_env,
                                'yaml':self._from_yaml,
                                'json':self._from_json,
                            }

        config_loader = config_source_map.get(self.extension)

        if config_loader:
            config_loader()
        else:
            raise UnsupportedOptionError(f'{self.extension} is not supported by AutoArt.')

class CloudConfig:
    def __init__(self, secret_pairs:dict):
        self.configs = {}
        self.secret_pairs = secret_pairs

    def _from_secrets_manager(self) -> None:
        pass

    def _from_ssm_parameter_store(self) -> None:
        pass

    def load_configs(self) -> None:
        service_source_map = {
                                'aws-secrets-manager':self._from_secrets_manager,
                                'aws-ssm-parameter-store':self._from_ssm_parameter_store,
                            }

        config_loader = service_source_map.get(self.secret_pairs[0])

        if config_loader:
            config_loader()
        else:
            raise UnsupportedOptionError(f'{self.secret_pairs[0]} is not supported by AutoArt.')

class Configs:
    def __init__(self, where:Literal['local', 'cloud'], which:Union[str, dict]):
        self.where = where
        self.which = which
        self.service = self._get_config_service()

    def _get_config_service(self) -> Union[LocalConfig, CloudConfig]:
        config_service_map = {
                                'local':LocalConfig,
                                'cloud':CloudConfig,
                            }

        config_service = config_service_map.get(self.where)

        if config_service:
            service = config_service(self.which)
            service.load_configs()
        else:
            raise UnsupportedOptionError(f'{self.where} is not supported by AutoArt.')

        return service

    @property
    def configs(self):
        return self.service.configs
