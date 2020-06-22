import ScwPy


if __name__ == "__main__":
    with open("real.key", "r") as key_file:
        key = key_file.read().strip()

    api = ScwPy.Manager(auth_token=key)
    servers = api.get_servers()
    for server in servers:
        print(f"{server.name}: {server.private_ip}")
