# coding=utf-8
import numpy as np


def all_numpy(obj):
    # Ensure everything is in numpy or int or float (no torch tensor)

    if isinstance(obj, dict):
        for key in obj.keys():
            all_numpy(obj[key])
    elif isinstance(obj, list):
        for i in range(len(obj)):
            all_numpy(obj[i])
    else:
        if not isinstance(obj, (np.ndarray, int, float)):
            return False

    return True