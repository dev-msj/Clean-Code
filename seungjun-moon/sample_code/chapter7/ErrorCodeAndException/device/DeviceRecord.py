class DeviceRecord:
    __device_id: int
    __status: str

    def __init__(self, device_id: int, status: str):
        self.__device_id = device_id
        self.__status = status

    def get_status(self) -> str:
        return self.__status
