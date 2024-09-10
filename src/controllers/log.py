# -*- coding: utf-8 -*-
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
