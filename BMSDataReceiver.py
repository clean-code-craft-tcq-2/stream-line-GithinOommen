import sys


class BMSDataReceiver:
    def __init__(self):
        self.bms_data = []

    def read_data_from_sender(self):
        data = []
        for _ in range(50):
            data.append(sys.stdin.readline().strip())
        print(data)


receiver = BMSDataReceiver()
receiver.read_data_from_sender()
