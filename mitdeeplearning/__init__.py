import importlib

import mitdeeplearning.util

import mitdeeplearning.lab1
import mitdeeplearning.lab2
import mitdeeplearning.lab3


def __getattr__(name):
    if name == "lab3_old":
        module = importlib.import_module(".lab3_old", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
