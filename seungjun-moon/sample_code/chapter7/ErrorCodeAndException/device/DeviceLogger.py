import logging

from sample_code.chapter7.ErrorCodeAndException import ErrorCodeAndException_PATH


class DeviceLogger:
    logger: logging.Logger = None

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        file_handler = logging.FileHandler(f'{ErrorCodeAndException_PATH}/device.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
