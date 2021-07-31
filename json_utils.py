import json

import numpy as np


class NumpyEncoder(json.JSONEncoder):
    """
    Class used for Numpy -> JSON conversion
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def dump_numpy_to_json(data):
    """
    Dump Numpy data to JSON format

    :param data: Numpy data (e.g. array)
    :return: JSON data
    """
    return json.dumps(data, cls=NumpyEncoder)


def dump_json_to_numpy(data):
    """
    Dump JSON data to Numpy data

    :param data: JSON data
    :return: Numpy array
    """
    return np.asarray(json.loads(data))
