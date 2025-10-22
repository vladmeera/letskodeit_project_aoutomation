import os
from inspect import stack
from logging import DEBUG, FileHandler, Formatter, getLogger


def count_lines():
    current_dir_path = os.path.dirname(__file__)
    project_path = os.path.join(current_dir_path, "..")
    log_file = os.path.join(project_path, "automation.log")
    try:
        with open(log_file, "r") as file:
            line_count = sum(1 for line in file)
        return line_count
    except Exception as e:
        print(f"An error occurred - {e}")
        return None


def custom_logger(log_level=DEBUG, log_filename="automation.log", mode="a"):
    """
    Creates a custom logger configured to log to a file named after the caller function.

    :return: Configured logger instance.
    """

    current_dir_path = os.path.dirname(__file__)
    project_path = os.path.join(current_dir_path, "..")
    log_file = os.path.join(project_path, "automation.log")

    # Gets the name of the class / method from where this method is called
    logger_name = stack()[1][3]

    logger = getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(DEBUG)
    if mode == "a":
        file_handler = FileHandler(log_filename, mode=mode)
        file_handler.setLevel(log_level)

        formatter = Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    elif mode == "w":
        file_handler = FileHandler(log_filename, mode=mode)
        file_handler.setLevel(log_level)

        formatter = Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        print("Invalid mode for file handler")

    num_lines = count_lines()
    if num_lines > 4000:
        print(
            f"\n--> Log file '{log_file}' has more than 4000 lines - !!! DELETE ALL LOGS AFTER 5000 !!! - | lines > 4000 | <--\n"
        )

    if num_lines > 5000:
        with open(log_file, "w") as file:
            file.truncate(0)
            print(
                f"\n--> Log file '{log_file}' cleared successfully - !!! REASON !!! - | lines > 5000 | <--\n"
            )

    return logger
