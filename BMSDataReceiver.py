import sys
from data_config import test_data
from data_config import dictionary_keys
from data_config import min_max_print_format
from data_config import moving_average_format
from data_config import test_data_null
from data_config import moving_average_window


def fetch_data_from_sender():
    data = []  # pragma: no cover
    if sys.stdin:  # pragma: no cover
        for _ in range(50):  # pragma: no cover
            data.append(sys.stdin.readline().strip())  # pragma: no cover
        return data  # pragma: no cover
    else:  # pragma: no cover
        return 'No Data Found'  # pragma: no cover


def stub_fetch_data_from_sender(data):
    return data


def print_to_console(message):
    print(message)  # pragma: no cover


class BMSDataReceiver:
    def __init__(self):
        self.bms_data = []
        self.max_reading = {}
        self.min_reading = {}
        self.moving_average = {}

    def convert_to_list_of_dictionary(self, data):
        if data:
            for reading_instance in data:
                data_instance = {}
                parameters = reading_instance.split('\t')
                for index in range(len(parameters)):
                    data_instance[dictionary_keys[index]] = parameters[index]
                self.bms_data.append(data_instance)
            return self.bms_data
        else:
            return 'No Data Found'

    def calculate_maximum_of_parameters(self):
        for key in self.bms_data[0].keys():
            self.max_reading[key] = max(reading[key] for reading in self.bms_data)
        return self.max_reading

    def calculate_minimum_of_parameters(self):
        for key in self.bms_data[0].keys():
            self.min_reading[key] = min(reading[key] for reading in self.bms_data)
        return self.min_reading

    def print_min_and_max_values_to_console(self):
        for key in self.min_reading.keys():  # pragma: no cover
            print_to_console(
                min_max_print_format.format(key, self.min_reading[key], self.max_reading[key]))  # pragma: no cover

    def print_moving_average(self):
        for key in self.moving_average.keys():  # pragma: no cover
            print_to_console(moving_average_format.format(key, self.moving_average[key]))  # pragma: no cover

    def calculate_moving_average(self):

        if len(self.bms_data) > moving_average_window:
            for key in self.bms_data[0].keys():
                moving_average = sum(
                    float(d[key]) for d in self.bms_data[-moving_average_window:]) / moving_average_window
                self.moving_average[key] = moving_average
            return self.moving_average


if __name__ == '__main__':
    receiver = BMSDataReceiver()  # pragma: no cover
    unparsed_data = fetch_data_from_sender()  # pragma: no cover
    data_list_of_dictionary = receiver.convert_to_list_of_dictionary(unparsed_data)  # pragma: no cover
    receiver.calculate_maximum_of_parameters()  # pragma: no cover
    receiver.calculate_minimum_of_parameters()  # pragma: no cover
    receiver.print_min_and_max_values_to_console()  # pragma: no cover
    receiver.calculate_moving_average()  # pragma: no cover
    receiver.print_moving_average()  # pragma: no cover
