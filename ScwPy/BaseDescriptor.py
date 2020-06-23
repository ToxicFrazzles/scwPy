class BaseDescriptor:
    def __init__(self, parent):
        self.value = None
        self.parent = parent

    def __getattr__(self, item):
        try:
            return self.value.__getattribute__(item)
        except AttributeError:
            raise AttributeError
