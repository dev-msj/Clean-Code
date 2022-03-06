import logging

from sample_code.chapter7.ErrorCodeAndException.device.DeviceHandle import DeviceHandle
from sample_code.chapter7.ErrorCodeAndException.device.DeviceLogger import DeviceLogger
from sample_code.chapter7.ErrorCodeAndException.device.DeviceRecord import DeviceRecord
from sample_code.chapter7.ErrorCodeAndException.exception.DeviceShutDownError import DeviceShutDownError


class DeviceController:
    DEV1: int = 339088
    DEVICE_SUSPENDED: str = "SUSPENDED"
    logger: logging.Logger

    def __init__(self):
        self.logger = DeviceLogger(self.__class__.__name__).logger

    def send_shut_down(self):
        try:
            self.__try_to_shut_down()
        except DeviceShutDownError as e:
            self.logger.error(e)

    def __try_to_shut_down(self):
        handle: DeviceHandle = self.__get_handle(self.DEV1)
        record = self.__retrieve_device_record(handle)

        self.__pause_device(handle)
        self.__clear_device_work_queue(handle)
        self.__close_device(handle)

    @classmethod
    def __get_handle(cls, device_id: int) -> DeviceHandle:
        handle = DeviceHandle(device_id)

        if handle.INVALID:
            raise DeviceShutDownError("Device suspended. Unable to shut down")

        return DeviceHandle(device_id)

    def __retrieve_device_record(self, handle: DeviceHandle) -> DeviceRecord:
        device_info = {
            339088: {
                "status": "RUNNING"
            },
            339089: {
                "status": "SUSPENDED"
            }
        }

        status = device_info.get(handle.get_device_id()).get("status")

        if status == self.DEVICE_SUSPENDED:
            raise DeviceShutDownError(f"Invalid handle for: {self.DEV1.__str__()}")

        return DeviceRecord(handle.get_device_id(), status)

    @classmethod
    def __pause_device(cls, handle: DeviceHandle):
        handle.pause()

    @classmethod
    def __clear_device_work_queue(cls, handle: DeviceHandle):
        handle.clear_queue()

    @classmethod
    def __close_device(cls, handle: DeviceHandle):
        handle.close()