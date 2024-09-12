import socket
import threading
import time

target = input("target >> ")

try:
    domain = socket.gethostbyname(target)
    print(f"Scanning the {target}....")
except socket.gaierror:
    print(f"name resolution error is occured!")
    exit()

open_ports = []

def port_scan(port):
    server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = server.connect_ex((domain,port))
    if result == 0:
        open_ports.append(port)
    server.close()

start_time = time.time()


for port in range(1,65536):
    thread = threading.Thread(target=port_scan, args=(port,))
    thread.start()

while threading.active_count() > 1:
    time.sleep(0.1)


end_time = time.time()


print(f"Scan completed in {end_time - start_time:.2f} seconds")
print("Open ports:")
for port in open_ports:
    print(f"Port {port} is open.")