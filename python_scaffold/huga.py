class Huga(object):
    def __init__(self, name: str):
        self._name: str = name

    def echo(self):
        return "Hello, {}.".format(self._name)
