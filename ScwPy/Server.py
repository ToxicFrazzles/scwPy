from .PublicIP import PublicIPDescriptor


class Server:
    def __init__(self, manager, id):
        self.id = id
        self.manager = manager
        self.name = None
        self.organization = None
        self.allowed_actions = None
        self.tags = None
        self.commercial_type = None
        self.creation_date = None
        self.dynamic_ip_required = None
        self.enable_ipv6 = None
        self.hostname = None
        self.image = None
        self.protected = None
        self.private_ip = None
        self.public_ip = PublicIPDescriptor(self)
        self.modification_date = None
        self.state = None
        self.location = None
        self.ipv6 = None
        self.bootscript = None
        self.boot_type = None
        self.volumes = None
        self.security_group = None
        self.maintenances = None
        self.state_detail = None
        self.arch = None
        self.placement_group = None
        self.zone = None
        self.extra_networks = None
        self.private_nics = None
