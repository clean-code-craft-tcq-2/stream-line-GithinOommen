from BMSDataReceiver import BMSDataReceiver
from data_config import test_data
from data_config import dictionary_keys

import unittest


class BMSDataReceiverTest(unittest.TestCase):
    def test_stub_fetch_data_from_sender(self):
        receiver = BMSDataReceiver()
        data = receiver.stub_fetch_data_from_sender()
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
        self.assertEqual(receiver.get_maximum_of_parameters(), {'Temperature': '9.000000', 'SoC': '96.000000', 'Charge': '0.190000'})

    def test_get_minimum_of_parameters(self):
        receiver = BMSDataReceiver()
        receiver.convert_to_list_of_dictionery(test_data)
        self.assertEqual(receiver.get_minimum_of_parameters(), {'Temperature': '10.000000', 'SoC': '2.000000', 'Charge': '0.010000'})


unittest.main()