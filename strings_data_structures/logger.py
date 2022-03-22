import logging

def logging_init(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

    info_handler = logging.FileHandler('info.log')
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    error_handler = logging.FileHandler('error.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(stream_handler)
    return logger