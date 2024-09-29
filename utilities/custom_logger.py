from logging import getLogger, DEBUG, FileHandler, Formatter
from inspect import stack

def custom_logger(log_level):
    # Gets the name of the class / method from where this method is called
    logger_name = stack()[1][3]

    logger = getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(DEBUG)

    file_handler = FileHandler("{0}.log".format(logger_name), mode='w')
    file_handler.setLevel(log_level)

    formatter = Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
