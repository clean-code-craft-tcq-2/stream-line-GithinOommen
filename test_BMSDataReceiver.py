from BMSDataReceiver import BMSDataReceiver
from data_config import test_data
from data_config import dictionary_keys
from data_config import min_max_print_format
from data_config import moving_average_format
from data_config import test_data_null
import unittest


class BMSDataReceiverTest(unittest.TestCase):
    def test_stub_fetch_data_from_sender(self):
        receiver = BMSDataReceiver()
        data = receiver.stub_fetch_data_from_sender(test_data)
        self.assertTrue(len(data) > 0)
        self.assertEqual(data, test_data)

    def test_dictionary_keys(self):
        self.assertEqual(dictionary_keys, ['Temperature', 'SoC', 'Charge'])

    def test_convert_to_list_of_dictionery(self):
        receiver = BMSDataReceiver()
        self.assertEqual(receiver.convert_to_list_of_dictionery(test_data),
                         [{'Temperature': '10.000000', 'SoC': '65.000000', 'Charge': '0.010000'},
                          {'Temperature': '4.000000', 'SoC': '46.000000', 'Charge': '0.030000'},
                          {'Temperature': '21.000000', 'SoC': '32.000000', 'Charge': '0.050000'},
                          {'Temperature': '48.000000', 'SoC': '30.000000', 'Charge': '0.070000'},
                          {'Temperature': '31.000000', 'SoC': '47.000000', 'Charge': '0.090000'},
                          {'Temperature': '48.000000', 'SoC': '96.000000', 'Charge': '0.110000'},
                          {'Temperature': '9.000000', 'SoC': '89.000000', 'Charge': '0.130000'},
                          {'Temperature': '37.000000', 'SoC': '58.000000', 'Charge': '0.150000'},
                          {'Temperature': '3.000000', 'SoC': '2.000000', 'Charge': '0.170000'},
                          {'Temperature': '31.000000', 'SoC': '93.000000', 'Charge': '0.190000'}]
                         )

    def test_get_maximum_of_parameters(self):
        receiver = BMSDataReceiver()
        receiver.convert_to_list_of_dictionery(test_data)
        self.assertEqual(receiver.calculate_maximum_of_parameters(),
                         {'Temperature': '9.000000', 'SoC': '96.000000', 'Charge': '0.190000'})

    def test_get_minimum_of_parameters(self):
        receiver = BMSDataReceiver()
        receiver.convert_to_list_of_dictionery(test_data)
        self.assertEqual(receiver.calculate_minimum_of_parameters(),
                         {'Temperature': '10.000000', 'SoC': '2.000000', 'Charge': '0.010000'})

    def test_print_min_and_max_values_to_console(self):
        receiver = BMSDataReceiver()
        receiver.convert_to_list_of_dictionery(test_data)
        min_reading = receiver.calculate_minimum_of_parameters()
        max_reading = receiver.calculate_maximum_of_parameters()
        self.assertEqual(
            min_max_print_format.format('Temperature', min_reading['Temperature'], max_reading['Temperature']),
            'Minimum and Maximum Temperature are 10.000000 , 9.000000')

    def test_calculate_moving_average_and_format(self):
        receiver = BMSDataReceiver()
        receiver.convert_to_list_of_dictionery(test_data)
        moving_average = receiver.calculate_moving_average()
        self.assertEqual(moving_average, {'Temperature': 25.6, 'SoC': 67.6, 'Charge': 0.15})
        self.assertEqual(moving_average_format.format('Temperature', moving_average['Temperature']),
                         'The moving average of Temperature is 25.6')

    def test_for_null_data(self):
        receiver = BMSDataReceiver()
        receiver.convert_to_list_of_dictionery(test_data_null)
        self.assertEqual(receiver.fetch_and_display_stats_sender_data(), 'No Data Found')


unittest.main()
