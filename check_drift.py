from netmiko import ConnectHandler
import difflib
import os
from dotenv import load_dotenv

load_dotenv()

device = {
    "device_type": "linux",
    "host": os.getenv("FRR_HOST"),
    "username": os.getenv("FRR_USER"),
    "password": os.getenv("FRR_PASSWORD"),
}

connection = ConnectHandler(**device)

raw_config = connection.send_command('vtysh -c "show running-config"')
clean_lines = [line for line in raw_config.splitlines() if not line.startswith("%")]
current_config = clean_lines

connection.disconnect()

with open("baseline_config.txt") as f:
    baseline_config = f.read().splitlines()

diff = list(difflib.unified_diff(
    baseline_config,
    current_config,
    fromfile="baseline",
    tofile="current",
    lineterm=""
))

if diff:
    print("DRIFT DETECTED:")
    for line in diff:
        print(line)
else:
    print("No drift detected. Configuration matches baseline.")