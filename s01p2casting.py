import binascii
mac_address = input("Enter MAC address (in XX:XX:XX:XX:XX:XX format): ")
# Step 1: Extract MAC address into byte string
mac_bytes = binascii.unhexlify(mac_address.replace(':', ''))
# Step 2: Insert FFFE
mac_bytes = mac_bytes[:3] + b'\xFF\xFE' + mac_bytes[3:]
# Step 3: Invert U/L bit
interface_id = bytearray(mac_bytes)
interface_id[0] ^= 2
# Step 4: Construct IPv6 address
ipv6_address = 'fe80::' + ':'.join(hex(b)[2:].zfill(2) for b in
interface_id)
print("IPv6 address:", ipv6_address)