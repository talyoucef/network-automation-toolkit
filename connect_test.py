from netmiko import ConnectHandler
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

output = connection.send_command('vtysh -c "show interface brief"')
print(output)

connection.disconnect()