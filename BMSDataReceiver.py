import sys
from data_config import test_data
from data_config import dictionary_keys
from data_config import min_max_print_format
from data_config import moving_average_format
from data_config import test_data_null


class BMSDataReceiver:
    def __init__(self):
        self.bms_data = []
        self.max_reading = {}
        self.min_reading = {}
        self.moving_average = {}

    def stub_fetch_data_from_sender(self, data):
        return data

    def fetch_data_from_sender(self):
        data = []
        if sys.stdin:
            for _ in range(50):
                data.append(sys.stdin.readline().strip())
            return data
        else:
            return 'No Data Found'

    def convert_to_list_of_dictionary(self, data):
        if data:
            for i in data:
                data_instance = {}
                d1 = i.split('\t')
                for index in range(len(d1)):
                    data_instance[dictionary_keys[index]] = d1[index]
                self.bms_data.append(data_instance)
            return self.bms_data
        else:
            return 'No Data Found'

    def calculate_maximum_of_parameters(self):
        for key in self.bms_data[0].keys():
            self.max_reading[key] = max(d[key] for d in self.bms_data)
        return self.max_reading

    def calculate_minimum_of_parameters(self):
        for key in self.bms_data[0].keys():
            self.min_reading[key] = min(d[key] for d in self.bms_data)
        return self.min_reading

    def print_min_and_max_values_to_console(self):
        for key in self.min_reading.keys():
            self.print_to_console(min_max_print_format.format(key, self.min_reading[key], self.max_reading[key]))

    def print_moving_average(self):
        for key in self.moving_average.keys():
            self.print_to_console(moving_average_format.format(key, self.moving_average[key]))

    def calculate_moving_average(self):

        if len(self.bms_data) > 5:
            for key in self.bms_data[0].keys():
                moving_average = sum(float(d[key]) for d in self.bms_data[-5:]) / 5
                self.moving_average[key] = moving_average
            return self.moving_average

    def print_to_console(self, message):
        print(message)

    def fetch_and_display_stats_sender_data(self):
        print(self.fetch_data_from_sender())
        self.convert_to_list_of_dictionary(self.fetch_data_from_sender())
        if self.bms_data:
            print(self.bms_data)
            self.calculate_maximum_of_parameters()
            self.calculate_minimum_of_parameters()
            self.print_min_and_max_values_to_console()
            self.calculate_moving_average()
            self.print_moving_average()
        else:
            return 'No Data Found'


receiver = BMSDataReceiver()
receiver.fetch_and_display_stats_sender_data()
