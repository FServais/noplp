import logging

def get_logger(
        LOG_FORMAT     = '%(asctime)s [%(filename)18s:%(lineno)5s] %(levelname)5s %(message)s',
        LOG_NAME       = ''
):
    BASE_PATH = './'
    LOG_FILE_DEBUG = BASE_PATH + LOG_NAME + '.log'
    LOG_FILE_ERROR = BASE_PATH + LOG_NAME + '.err'

    log = logging.getLogger(LOG_NAME)

    if not log.handlers:
        log_formatter = logging.Formatter(LOG_FORMAT)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)
        stream_handler.setLevel(logging.INFO)
        log.addHandler(stream_handler)

        file_handler_debug = logging.FileHandler(LOG_FILE_DEBUG)
        file_handler_debug.setFormatter(log_formatter)
        file_handler_debug.setLevel(logging.DEBUG)
        log.addHandler(file_handler_debug)

        # file_handler_error = logging.FileHandler(LOG_FILE_ERROR)
        # file_handler_error.setFormatter(log_formatter)
        # file_handler_error.setLevel(logging.ERROR)
        # log.addHandler(file_handler_error)

        log.setLevel(logging.DEBUG)

    return log
