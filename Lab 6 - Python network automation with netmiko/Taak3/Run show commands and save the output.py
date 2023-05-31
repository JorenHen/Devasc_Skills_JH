from netmiko import ConnectHandler
import threading
devices = [
{
    'device_type': 'cisco_xe',
    'ip': '192.168.253.128',
    'username': 'admin',
    'password': 'Admin!.',
}

]
def run_show_command(device, command):
connection = ConnectHandler(**device)
output = connection.send_command(command)
filename = f"{device['ip']}_output.txt"
with open(filename, 'w') as f:
    f.write(output)
print(f"Output from {device['ip']} saved to {filename}")
connection.disconnect()
threads = []
show_command = 'show version'
for device in devices:
thread = threading.Thread(target=run_show_command, args=(device, show_command))
thread.start()
threads.append(thread)
for thread in threads:
thread.join()
