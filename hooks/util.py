#!/usr/bin/env python3

import argparse
import logging.config

from pathlib import Path
from typing import Sequence


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(levelname)s] %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        # Reserved for future loggers
        # To override the logging level for a module hooks.foo:
        # "hooks.foo": {
        #     "level": "INFO",
        # },
    },
    "root": {
        "handlers": [
            "console",
        ],
        "level": "WARN",
    },
}

logging.config.dictConfig(LOGGING_CONFIG)


def get_input_files() -> Sequence[Path]:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path, nargs="+")
    args = parser.parse_args()
    return args.path