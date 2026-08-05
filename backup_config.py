from netmiko import ConnectHandler
from datetime import datetime

device = {
    "device_type": "linux",
    "host": "192.168.122.10",
    "username": "root",
    "password": "frrlab123",
}

connection = ConnectHandler(**device)

raw_config = connection.send_command('vtysh -c "show running-config"')

# Remove noise lines that aren't part of the actual config
clean_lines = [line for line in raw_config.splitlines() if not line.startswith("%")]
config = "\n".join(clean_lines)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"backups/frr-config_{timestamp}.txt"

with open(filename, "w") as f:
    f.write(config)

print(f"Saved config to {filename}")

connection.disconnect()