import numpy as np
from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.requests import Request

from json_utils import dump_numpy_to_json, dump_json_to_numpy


def main():
    client = HTTPClient('http://localhost:5000')
    response = client.send(Request('ping'))
    print('Response from server = {}'.format(response.data.result))

    # AM Modulation Test
    fs = 44100
    st = 1
    f_msg = 10
    f_car = 1000
    t = np.arange(0, st, 1 / fs)
    msg_signal = np.cos(2 * np.pi * f_msg * t)
    car_signal = np.sin(2 * np.pi * f_car * t)

    # Dump to JSON
    msg_signal = dump_numpy_to_json(msg_signal)
    car_signal = dump_numpy_to_json(car_signal)

    response = client.send(Request('am_mod', msg_signal=msg_signal, carrier_signal=car_signal))
    # Dump JSON response to Numpy array data
    resp_data = dump_json_to_numpy(response.data.result)
    print('Length of AM-modulated data = {}'.format(len(resp_data)))


if __name__ == '__main__':
    main()
