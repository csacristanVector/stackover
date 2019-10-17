import logging


def setup_logger(level, name):
    log = logging.Logger(name)
    log.setLevel(level)

    # consoleHandler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '[%(asctime)s]-[%(name)s]-[%(pathname)s:%(lineno)d]-[%(levelname)s] - %(message)s'
    )
    ch.setFormatter(formatter)

    log.addHandler(ch)

    log.info('Log System initialized')

    return log
