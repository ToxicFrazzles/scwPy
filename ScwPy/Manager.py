from .Common import *
from .Server import Server
import requests
import time
from typing import List


class Manager:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self._servers = None

    def api_request(self, url) -> requests.Response:
        headers = {
            'X-Auth-Token': self.auth_token,
            'Content-Type': 'application/json'
        }
        r = requests.get(url, headers=headers)
        print(url)
        print(r.text)
        return r

    def get_zone_servers(self, zone) -> List[Server]:
        request_url = f"{endpoint}/instance/v1/zones/{zone}/servers"
        page = 1
        servers = []
        while True:
            request = self.api_request(f"{request_url}?page={page}&per_page=100")
            if request.status_code != 200:
                break
            json = request.json()
            count = len(json['servers'])
            if count < 1:
                break
            for raw_server in json['servers']:
                print("Server:", raw_server['id'])
                server = Server(self, raw_server['id'])
                for key, value in raw_server.items():
                    if key == "id":
                        continue
                    print(f" {key}: {value}")
                    server.__setattr__(key, value)
                servers.append(server)
            if count < 100:
                break
            else:
                page += 1
            time.sleep(1)
        return servers

    def get_servers(self, zone=None) -> List[Server]:
        servers = []
        if zone is None:
            for zone in zones:
                servers += self.get_zone_servers(zone)
        else:
            servers = self.get_zone_servers(zone)
        self._servers = servers
        return servers
