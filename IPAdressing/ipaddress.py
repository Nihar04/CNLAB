def validate_ip(ip):
    # Split the IP address into parts
    parts = ip.split(".")

    # Check if the IP address has four parts
    if len(parts) != 4:
        print("Invalid IP address format. It should have four octets separated by periods.")
        return False

    for part in parts:
        if not part.isdigit():
            print(f"Invalid IP address part '{part}'. IP address should contain only numbers.")
            return False

        # Convert part to integer
        part_int = int(part)

        # Check if each part of the IP address is within the valid range
        if part_int < 0 or part_int > 255:
            print(f"IP address part '{part_int}' out of range. Each part must be between 0 and 255.")
            return False

    return True


def get_ip_class(ip):
    # Get the first octet of the IP address
    first_octet = int(ip.split(".")[0])

    # Determine the class and netmask based on the first octet
    if 0 <= first_octet <= 127:
        return "Class A", "255.0.0.0"
    elif 128 <= first_octet <= 191:
        return "Class B", "255.255.0.0"
    elif 192 <= first_octet <= 223:
        return "Class C", "255.255.255.0"
    elif 224 <= first_octet <= 239:
        return "Class D", "Reserved"
    elif 240 <= first_octet <= 255:
        return "Class E", "Reserved"


def ip_to_int(ip):
    """Convert IP address to an integer."""
    parts = map(int, ip.split('.'))
    return sum(part << (8 * (3 - i)) for i, part in enumerate(parts))


def int_to_ip(ip_int):
    """Convert an integer back to an IP address."""
    return '.'.join(str((ip_int >> (8 * i)) & 0xFF) for i in reversed(range(4)))


def calculate_first_last_ip(ip, netmask):
    """Calculate the first and last IP addresses in the subnet."""
    ip_int = ip_to_int(ip)
    netmask_int = ip_to_int(netmask)

    # Calculate the first IP address using bitwise AND
    first_ip_int = ip_int & netmask_int

    # Calculate the last IP address using bitwise OR with the complement of the netmask
    last_ip_int = ip_int | (~netmask_int & 0xFFFFFFFF)

    return int_to_ip(first_ip_int), int_to_ip(last_ip_int)


def main():
    # Accept IP address from the user
    ip_address = input("Enter an IP address: ")

    # Validate the IP address
    if not validate_ip(ip_address):
        return

    # Get the IP class and netmask
    ip_class, netmask = get_ip_class(ip_address)

    # Display the class and netmask information
    print(f"The IP address {ip_address} belongs to {ip_class}.")
    if netmask != "Reserved":
        print(f"The default subnet mask for {ip_class} is {netmask}.")
    else:
        print(f"{ip_class} is reserved for special purposes.")
        return

    # Calculate the first and last IP addresses in the subnet
    first_ip, last_ip = calculate_first_last_ip(ip_address, netmask)

    # Display the first and last IP addresses
    print(f"The first IP address in the subnet is: {first_ip}")
    print(f"The last IP address in the subnet is: {last_ip}")


if __name__ == "__main__":
    main()
