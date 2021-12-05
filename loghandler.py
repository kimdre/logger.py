import logging
import os
import sys

import colorlog


def loghandler():
    debug_mode = os.getenv('DEBUG_MODE', "False")
    if debug_mode.lower() == "false":
        debug_mode = False

    _logger = colorlog.getLogger(__name__)
    if debug_mode:
        _logger.setLevel(logging.DEBUG)
    else:
        _logger.setLevel(logging.INFO)

    handler = colorlog.StreamHandler(sys.stdout)
    if debug_mode:
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
