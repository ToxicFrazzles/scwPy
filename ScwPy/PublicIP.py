from .BaseDescriptor import BaseDescriptor


class PublicIP:
    def __init__(self, manager, id):
        self.id = id
        self.manager = manager
        self.address = None
        self.dynamic = None


class PublicIPDescriptor(BaseDescriptor):
    def __init__(self, parent):
        super().__init__(parent)

    def __get__(self, obj, owner=None) -> PublicIP:
        try:
            return self.value
        except AttributeError:
            print("There's an attribute error there")
            raise AttributeError

    def __set__(self, obj, value):
        print("Set is called")
        if isinstance(value, PublicIP):
            ip = value
        else:
            ip = PublicIP(obj.manager, value['id'])
            for key, val in value.items():
                if key == "id": continue
                ip.__setattr__(key, val)
        self.value = ip
