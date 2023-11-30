from netmiko import ConnectHandler

def send_config_commands(device, config_commands):
    # Establish an SSH connection to the device
    connection = ConnectHandler(**device)

    # Enter configuration mode
    connection.config_mode()

    # Send configuration commands
    output = connection.send_config_set(config_commands)

    # Exit configuration mode
    connection.exit_config_mode()

    # Close the SSH connection
    connection.disconnect()

    return output

if __name__ == "__main__":
    config_commands = ["interface GigabitEthernet0/1", "ip address 192.168.1.1 255.255.255.0", "no shutdown"]

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        output = send_config_commands(dev, config_commands)
        print(f"Device: {dev['device_type']} - {dev['ip']} - Command Output: {output}")
