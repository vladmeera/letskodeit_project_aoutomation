from logging import getLogger, DEBUG, FileHandler, Formatter, Logger
from inspect import stack

def custom_logger(log_level=DEBUG) -> Logger:
    """
    Creates a custom logger configured to log to a file named after the caller function.

    :param log_level: Logging level, default is DEBUG.
    :return: Configured logger instance.
    """

    # Gets the name of the class / method from where this method is called
    logger_name = stack()[1][3]

    logger = getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(DEBUG)

    file_handler = FileHandler("automation.log", mode='a')
    file_handler.setLevel(log_level)

    formatter = Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
