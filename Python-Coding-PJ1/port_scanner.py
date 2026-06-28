import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port)) # ipaddress , port are 2 parameter required
        print(f"[+] Port Open! Port: {port}")
        sock.close()
    except:
        pass

targets = input("[*] Enter targets to scan (split them by ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))

if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr,ports)

else:
    scan(targets, ports)



#ports = []

# while True:
#     user_input = input("Enter the port to scan. enter 's' to start.\nYour Input: ")

#     if user_input.isdigit():
#         ports.append(user_input)
#         continue

#     if user_input in ['q', 'Q']:
#         print("Started scanning...\n")

#     else:
#         print("Invalid Input!\n")





