# source: http://docs.python-guide.org/en/latest/writing/logging/
import logging
from logging.config import dictConfig


def setup_logger(level=logging.NOTSET, name=''):
    logging_config = dict(
        version=1,
        formatters={
            'f': {'format':
                      '%(asctime)-28s %(levelname)-10s %(module)-24s %(lineno)-6s %(funcName)-28s %(message)-8s'}
        },
        handlers={
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': level}
        },
        loggers={
            name: {'handlers': ['h'],
                    'level': level}
            }
    )
    dictConfig(logging_config)
    return logging.getLogger(name)


