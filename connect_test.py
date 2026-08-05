from netmiko import ConnectHandler

device = {
    "device_type": "linux",
    "host": "192.168.122.10",
    "username": "root",
    "password": "frrlab123",
}


'''
connection = ConnectHandler( 
    device_type="linux",
    host="192.168.122.10",
    username= "root",
    password="frrlab123",
    )
'''

connection = ConnectHandler(**device)

output = connection.send_command('vtysh -c "show interface brief"')
print(output)

connection.disconnect()