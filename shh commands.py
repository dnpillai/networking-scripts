from netmiko import ConnectHandler

def send_show_command(device, command):
    # Establish an SSH connection to the device
    connection = ConnectHandler(**device)

    # Send the command and receive the output
    output = connection.send_command(command)

    # Close the SSH connection
    connection.disconnect()

    return output

if __name__ == "__main__":
    command = "sh ip int br"
    
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        output = send_show_command(dev, command)
        print(f"Device: {dev['device_type']} - {dev['ip']} - Command Output: {output}")