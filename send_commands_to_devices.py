import yaml
import concurrent.futures
from netmiko import ConnectHandler

def send_show_command(device, command):
    # Similar to the previous implementation

def send_config_commands(device, config_commands):
    # Similar to the previous implementation

def send_commands(device, *, show=None, config=None):
    # Similar to the previous implementation

def send_commands_to_devices(devices, filename, *, show=None, config=None, limit=3):
    if (show is None and config is None) or (show is not None and config is not None):
        raise ValueError("Exactly one of 'show' or 'config' should be provided.")

    def process_device(device):
        output = send_commands(device, show=show, config=config)
        with open(filename, 'a') as f:
            f.write(f"Device: {device['device_type']} - {device['ip']} - Output:\n{output}\n\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=limit) as executor:
        executor.map(process_device, devices)

if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    filename = "output.txt"
    show_command = "show version"
    config_commands = ["interface GigabitEthernet0/1", "ip address 192.168.1.1 255.255.255.0", "no shutdown"]

    send_commands_to_devices(devices, filename, show=show_command, limit=3)
    send_commands_to_devices(devices, filename, config=config_commands, limit=3)
