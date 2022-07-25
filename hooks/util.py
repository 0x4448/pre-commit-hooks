#!/usr/bin/env python3

import logging
import logging.config


LOG_CONFIG = {
    "version": 1,
    "formatters": {"default": {"format": "[%(levelname)s] %(message)s"}},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "WARNING",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "": {
            "handlers": [
                "console",
            ]
        }
    },
}

logging.config.dictConfig(LOG_CONFIG)
log = logging.getLogger(__name__)
