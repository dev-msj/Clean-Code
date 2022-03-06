import queue


class DeviceHandle:
    INVALID = False
    __device_id: int = 0
    __work_queue: queue.Queue

    def __init__(self, device_id: int):
        self.__device_id = device_id
        self.__work_queue = queue.Queue()

    def get_device_id(self) -> int:
        return self.__device_id

    def pause(self):
        print(f"{self.__device_id} pause!!!")

    def clear_queue(self):
        self.__work_queue.queue.clear()
        print(f"{self.__device_id} work queue clear!!!")

    def close(self):
        print(f"{self.__device_id} close!!!")
