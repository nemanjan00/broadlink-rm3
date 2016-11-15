#!/usr/bin/python

import broadlink
import json

import time

import sys

device_id = int(sys.argv[len(sys.argv)-1])
command_name = sys.argv[len(sys.argv)-2]

config_file = open("config.json", "r")
config = config_file.read()
config_file.close()

config = json.loads(config)
device = config[device_id]

device = broadlink.device((device["ip"], device["port"]), mac=device["mac"].decode('hex'))

device.auth()

device.enter_learning()

while True:
    time.sleep(1)
    ir_packet = device.check_data()
    
    if (str(ir_packet).encode("hex") != "4e6f6e65"):
        break

commands_file = open("commands.json", "r")
commands = commands_file.read()
commands_file.close()

commands = json.loads(commands)

commands[command_name] = str(ir_packet).encode("hex")

commands_file = open("commands.json", "w")
commands = commands_file.write(json.dumps(commands))
commands_file.close()


