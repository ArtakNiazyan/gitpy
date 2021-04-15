import logging
import os


def configure_log_file(filename):
    logger = logging.getLogger(__name__)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    log_base_dir = "logs/"
    log_dir = os.path.join(ROOT_DIR, log_base_dir)
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    log_fn = os.path.join(log_dir, f"{filename}.log")
    handler = logging.FileHandler(log_fn)
    formatter = logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
