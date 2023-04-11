import argparse
import socket
import threading

def scan_port(ip, port, log_file):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1) # Increase the timeout if any errors
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
            with open(log_file, 'a') as file:
                file.write(f"\nPort {port} is open on {ip}")
        sock.close()
    except:
        pass

def scan_ip(ip, ports, log_file):
    for port in ports:
        scan_port(ip, port, log_file)

def scan_ips(ips, ports, log_file):
    threads = []
    for ip in ips:
        t = threading.Thread(target=scan_ip, args=(ip, ports, log_file))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def parse_ip_range(ip_range):
    start, end = ip_range.split("-")
    start_parts = [int(x) for x in start.split(".")]
    end_parts = [int(x) for x in end.split(".")]
    ips = []
    for i in range(start_parts[0], end_parts[0]+1):
        for j in range(start_parts[1], end_parts[1]+1):
            for k in range(start_parts[2], end_parts[2]+1):
                for l in range(start_parts[3], end_parts[3]+1):
                    ips.append(f"{i}.{j}.{k}.{l}")
    return ips

def parse_args():
    parser = argparse.ArgumentParser(description="nekros1x scanner")
    parser.add_argument("target", help="IP address or filename containing IP addresses")
    parser.add_argument("-p", "--port", help="Port range to scan (example: 80 or 1-25)", required=True)
    parser.add_argument("-log", "--log_file", help="Name of the log file")
    return parser.parse_args()

def main():
    args = parse_args()
    print(f"Target: {args.target}")
    print(f"Port: {args.port}")
    if args.target.endswith(".txt"):
        with open(args.target) as f:
            ips = []
            for line in f:
                ip_range = line.strip()
                ips.extend(parse_ip_range(ip_range))
    else:
        ips = [args.target]

    if "-" in args.port:
        start, end = [int(x) for x in args.port.split("-")]
        ports = range(start, end+1)
    else:
        ports = [int(args.port)]

    print(f"IPs: {ips}")
    print(f"Ports: {ports}")
    log_file = args.log_file if args.log_file else 'log.txt'
    scan_ips(ips, ports, log_file)


main()
