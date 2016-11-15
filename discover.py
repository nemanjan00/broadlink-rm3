#!/usr/bin/python

import broadlink
import json

devices = broadlink.discover(timeout=5)

config = []

for device in devices:
    config.append({"ip": devices[0].host[0], "port": devices[0].host[1], "mac": str(devices[0].mac).encode('hex')})

config_file = open("config.json", "w")
config_file.write(json.dumps(config))
config_file.close()

