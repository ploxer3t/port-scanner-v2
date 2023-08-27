import socket
import concurrent.futures

def port_scan(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip, port))
        print(f"Port {port} is open")
    except:
        pass
    sock.close()

ip = input("IP adresi girin: ")
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1, 1025):
        executor.submit(port_scan, ip, port)