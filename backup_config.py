from netmiko import ConnectHandler
from datetime import datetime
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

# Remove noise lines that aren't part of the actual config
clean_lines = [line for line in raw_config.splitlines() if not line.startswith("%")]
config = "\n".join(clean_lines)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"backups/frr-config_{timestamp}.txt"

with open(filename, "w") as f:
    f.write(config)

print(f"Saved config to {filename}")

connection.disconnect()