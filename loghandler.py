import logging
import os
import sys

import colorlog


def loghandler():
    _logger = colorlog.getLogger(__name__)

    loglevel = os.getenv('LOG_LEVEL', "INFO")

    match loglevel.lower():
        case "debug":
            _logger.setLevel(logging.DEBUG)
        case "info":
            _logger.setLevel(logging.INFO)
        case "warn" | "warning":
            _logger.setLevel(logging.WARNING)
        case "error":
            _logger.setLevel(logging.ERROR)
        case "crit" | "critical":
            _logger.setLevel(logging.CRITICAL)
        case _:
            raise ValueError("Definied value of LOG_LEVEL is not known. Possible values are debug, info, warn, warning, error, crit and critical.")

    handler = colorlog.StreamHandler(sys.stdout)
    if loglevel:
        handler.setLevel(logging.DEBUG)
    else:
        handler.setLevel(logging.INFO)
    formatter = colorlog.ColoredFormatter(
        '[%(asctime)s] %(log_color)s%(levelname)s%(reset)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    handler.setFormatter(formatter)
    _logger.addHandler(handler)

    return _logger


logger = loghandler()
