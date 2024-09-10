# -*- coding: utf-8 -*-
"""
The file 'log.py' configures logging layers according to instructions specified in the 'log.ini' file. AutoArt utilizes four distinct logging layers, each with 
its own custom configuration, to handle different aspects of logging within the service. Each layer directs its output to the service terminal.

Notes
-----
Logs can be tracked in CloudTrail Event Logs for auditing and monitoring purposes.

Layers
------
auto-art.access_layer
    Responsible for logging events related to API access, including authentication and authorization issues.

auto-art.service_layer
    Responsible for core service operations, including machine learning service and data manipulation issues.

auto-art.serve_layer
    Responsible for serving system outputs into the downstream services, including sending predictions, CRUD operations on trained models.

auto-art.monitor_layer
    Responsible for monitoring the system health and model success, including performance metrics, and operational health checks.
"""
import os
import sys
import logging
import logging.config

LOG_PATH = os.path.join(os.getcwd(), "configs/log.ini")
logging.config.fileConfig(LOG_PATH)

access_layer_logger = logging.getLogger('auto-art.access_layer')
service_layer_logger = logging.getLogger('auto-art.service_layer')
serve_layer_logger = logging.getLogger('auto-art.serve_layer')
monitor_layer_logger = logging.getLogger('auto-art.monitor_layer')
