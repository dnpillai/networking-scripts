import yaml
from netmiko import ConnectHandler

def send_show_command(device, command):
    # Establish an SSH connection to the device
    connection = ConnectHandler(**device)

    # Send the show command and receive the output
    output = connection.send_command(command)

    # Close the SSH connection
    connection.disconnect()

    return output

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

def send_commands(device, *, show=None, config=None):
    if (show is None and config is None) or (show is not None and config is not None):
        raise ValueError("Exactly one of 'show' or 'config' should be provided.")

    if show is not None:
        return send_show_command(device, show)
    elif config is not None:
        return send_config_commands(device, config)

if __name__ == "__main__":
    commands = ["interface GigabitEthernet0/1", "ip address 192.168.1.1 255.255.255.0", "no shutdown"]
    command = "show ip interface brief"

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        # Testing with show command
        output_show = send_commands(dev, show=command)
        print(f"Device: {dev['device_type']} - {dev['ip']} - Show Command Output: {output_show}")

        # Testing with config commands
        output_config = send_commands(dev, config=commands)
        print(f"Device: {dev['device_type']} - {dev['ip']} - Config Commands Output: {output_config}")
