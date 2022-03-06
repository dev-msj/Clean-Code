import logging

from sample_code.chapter7.ErrorCodeAndException.device.DeviceHandle import DeviceHandle
from sample_code.chapter7.ErrorCodeAndException.device.DeviceLogger import DeviceLogger
from sample_code.chapter7.ErrorCodeAndException.device.DeviceRecord import DeviceRecord


class DeviceController:
    DEV1: int = 339088
    DEVICE_SUSPENDED: str = "SUSPENDED"
    logger: logging.Logger

    def __init__(self):
        self.logger = DeviceLogger(self.__class__.__name__).logger

    def send_shut_down(self):
        handle: DeviceHandle = self.__get_handle(self.DEV1)

        if handle != DeviceHandle.INVALID:
            record = self.__retrieve_device_record(handle)

            if record.get_status() != self.DEVICE_SUSPENDED:
                self.__pause_device(handle)
                self.__clear_device_work_queue(handle)
                self.__close_device(handle)
            else:
                self.logger.error("Device suspended. Unable to shut down")
        else:
            self.logger.error(f"Invalid handle for: {self.DEV1.__str__()}")

    @classmethod
    def __get_handle(cls, device: int) -> DeviceHandle:
        return DeviceHandle(device)

    @classmethod
    def __retrieve_device_record(cls, handle: DeviceHandle) -> DeviceRecord:
        device = handle.get_device_id()
        status = "RUNNING"

        return DeviceRecord(device, status)

    @classmethod
    def __pause_device(cls, handle: DeviceHandle):
        handle.pause()

    @classmethod
    def __clear_device_work_queue(cls, handle: DeviceHandle):
        handle.clear_queue()

    @classmethod
    def __close_device(cls, handle: DeviceHandle):
        handle.close()
