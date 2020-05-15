import logging
import sys

#based on https://stackoverflow.com/questions/50714316/how-to-use-logging-getlogger-name-in-multiple-modules
def setup_general_logger(log_name):
    # create and configure main logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(f'exercises.log', 'a')

    # create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    screen_handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(screen_handler)

    return logger
