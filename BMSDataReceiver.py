import sys


class BMSDataReceiver:
    def __init__(self):
        self.bms_data = []

    def read_data_from_sender(self):

        for line in sys.stdin:
            if len(line) != 1:
                bms_param = {}
                print(line.replace('\n', ''))
                input_data = line.split('\t')
                bms_param['Temperature'] = input_data[0]
                bms_param['SoC'] = input_data[1]
                bms_param['Current'] = input_data[2]
                self.bms_data.append(bms_param)


receiver = BMSDataReceiver()
receiver.read_data_from_sender()
