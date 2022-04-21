import sys
from data_config import test_data
from data_config import dictionary_keys


class BMSDataReceiver:
    def __init__(self):
        self.bms_data = []
        self.max_reading = {}
        self.min_reading = {}

    def stub_fetch_data_from_sender(self):
        data = test_data
        return data

    def fetch_data_from_sender(self):
        data = []
        for _ in range(50):
            data.append(sys.stdin.readline().strip())
        return data

    def convert_to_list_of_dictionery(self, data):
        for i in data:
            data_instance = {}
            d1 = i.split('\t')
            for index in range(len(d1)):
                data_instance[dictionary_keys[index]] = d1[index]
            self.bms_data.append(data_instance)
        return self.bms_data

    def get_maximum_of_parameters(self):
        for key in self.bms_data[0].keys():
            self.max_reading[key] = max(d[key] for d in self.bms_data)
        return self.max_reading

    def get_minimum_of_parameters(self):
        for key in self.bms_data[0].keys():
            self.min_reading[key] = min(d[key] for d in self.bms_data)
        return self.min_reading


receiver = BMSDataReceiver()
data_from_sender = receiver.fetch_data_from_sender()
receiver.convert_to_list_of_dictionery(data_from_sender)
print(receiver.get_maximum_of_parameters())
print(receiver.get_minimum_of_parameters())
