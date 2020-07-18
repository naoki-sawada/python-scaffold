__version__ = "0.1.0"

from .huga import Huga


def run():
    h: Huga = Huga("world")
    print(h.echo())
