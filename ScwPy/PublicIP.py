from .BaseDescriptor import BaseDescriptor


class PublicIP:
    def __init__(self, manager, id):
        self.id = id
        self.manager = manager
        self.owner = None
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
            # TODO: Add some logic for reassigning an IP address via the API
            ip = value
        else:
            matches = [i for i, x in enumerate(self.parent.manager._public_ips) if x.id == value['id']]
            if len(matches) > 0:
                ip = self.parent.manager._public_ips[matches[0]]
            else:
                ip = PublicIP(obj.manager, value['id'])
            ip.owner = obj
            for key, val in value.items():
                if key == "id": continue
                ip.__setattr__(key, val)
        self.value = ip
