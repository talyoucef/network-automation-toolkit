from netmiko import ConnectHandler
import difflib

device = {
    "device_type": "linux",
    "host": "192.168.122.10",
    "username": "root",
    "password": "frrlab123",
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