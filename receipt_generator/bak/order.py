import socket

ip = "192.168.1.100"
port = 9100


data = (
    "\x1b@"                         # Initialise
    "\x1b\x61\x01"                 # Centre
    "\x1b\x45\x01"                 # Bold on
    "PYTHON TEST RECEIPT\n"
    "\x1b\x45\x00"                 # Bold off
    "PYTHON TEST RECEIPT\n"
    "\n"
    "\x1b\x61\x00"                 # Left align
    "--------------------------------\n"
    "Item 1 - £12.00\n"
    "--------------------------------\n"
    "\x1b\x45\x01"
    "TOTAL                  £13.00\n"
    "\x1b\x45\x00"
    "\n\n\n"
    "\n\n\n"
    "\n\n\n"
    "\x1d\x56\x00"                 # Cut paper
)

with socket.create_connection((ip, port), timeout=5) as printer:
    printer.sendall(data.encode("cp437"))

print("Receipt sent.")