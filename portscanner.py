from urllib.parse import urlparse
import socket
import time

print("=" * 50)
print("        kalees_bytes")
print("    Mini Port Scanner v1.0")
print("=" * 50)

def check_port(host, port):
    try:
        socket.create_connection((host, port), timeout=1)
        return True
    except:
        return False

def scan_common_ports(host, ports):
    print(f"\n[+] Scanning common ports on {host}\n")
    for port, service in ports.items():
        try:
            socket.create_connection((host, port), timeout=1)
            print(f"[OPEN]   {port:<5} ({service})")
        except:
            pass

# ---------------- INPUT HANDLING ----------------

target_input = input("\nEnter the target IP address or website: ").strip()
parsed = urlparse(target_input)


if parsed.netloc:
    target = parsed.netloc
else:
    target = parsed.path

# ---------------- OPTIONS ----------------

print("\n1 : Scan DEFAULT ports")
print("2 : Scan SPECIFIC port")
opt = int(input("Choose option: "))

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-ALT"
}

start_time = time.time()

if opt == 1:
    scan_common_ports(target, COMMON_PORTS)

elif opt == 2:
    port = int(input("Enter port number: "))
    result = check_port(target, port)

    if result:
        print(f"\n[OPEN]   Port {port}")
    else:
        print(f"\n[CLOSED] Port {port}")

else:
    print("\n[!] Invalid option")

end_time = time.time()
print(f"\nScan completed in {end_time - start_time:.2f} seconds")
