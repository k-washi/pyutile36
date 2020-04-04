import os
import logging


class Configure(object):
    log_level = os.environ.get('PYTHON_LOG_LEVEL')
    if not log_level:
        log_level = logging.DEBUG
