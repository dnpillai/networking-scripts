import concurrent.futures
import subprocess

def ping_ip(ip_address):
    try:
        # Use subprocess to run the ping command with a timeout of 2 seconds
        subprocess.run(["ping", "-c", "1", "-W", "2", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return ip_address, True  # IP address is reachable
    except subprocess.CalledProcessError:
        return ip_address, False  # IP address is not reachable

def ping_ip_addresses(ip_list, limit=3):
    available_ips = []
    unavailable_ips = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=limit) as executor:
        # Use executor.map to apply the ping_ip function to each IP address in parallel
        results = executor.map(ping_ip, ip_list)

        for ip, is_available in results:
            if is_available:
                available_ips.append(ip)
            else:
                unavailable_ips.append(ip)

    return available_ips, unavailable_ips

if __name__ == "__main__":
    # Example usage
    ip_list = ["192.168.1.1", "8.8.8.8", "10.0.0.1", "nonexistentip"]
    available_ips, unavailable_ips = ping_ip_addresses(ip_list)
    
    print("Available IPs:", available_ips)
    print("Unavailable IPs:", unavailable_ips)
