import logging.config


def configure_logging(level):
    logger_config = {
        'level': level,
        'handlers': ['console', 'file']
    }

    log_names = [
        'aiohttp.access',
        'aiohttp.client',
        'aiohttp.internal',
        'aiohttp.server',
        'aiohttp.web',
        'aiohttp.websocket',
    ]

    loggers = {name: logger_config for name in log_names}

    config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': level,
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': 'server.log',
                'maxBytes': 2048,
                'backupCount': 3
            }
        },
        'loggers': loggers,
        'root': logger_config,
    }

    logging.config.dictConfig(config)
