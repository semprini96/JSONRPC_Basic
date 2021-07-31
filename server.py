import signal
import sys

from jsonrpcserver import method, serve

from json_utils import dump_json_to_numpy, dump_numpy_to_json


def signal_handler(sig, frame):
    """
    Handle SIGINT signal (e.g. Ctrl-C)
    """
    print('SIGINT received, stopping...')
    sys.exit(0)


@method
def ping():
    """
    Very simple ping function

    :return: 'Pong' static string
    """
    return 'Pong'


@method
def am_mod(msg_signal, carrier_signal):
    """
    Calculate AM modulation of given message signal and given carrier signal

    :param msg_signal: Message signal
    :param carrier_signal: Carrier signal
    :return: AM-modulated signal
    """
    mod_signal = dump_json_to_numpy(carrier_signal) * (1 + dump_json_to_numpy(msg_signal))
    return dump_numpy_to_json(mod_signal)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    print('Server process started, listening on port 5000')
    serve()
