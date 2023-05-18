# Python-Port-Scanner
Complete port scanner made in Python with several options.
 
This program is used to scan ports on one or multiple IP addresses. It can take a single IP address as an argument or a file containing a range of IP addresses and a range of ports to scan. Additionally, an optional log file can be specified to store the scan results.

With this program I was able to scan 1 port in 2.2 million different ip addresses (my whole country ip's) in 560-600 seconds, it's really fast because we are using threading.
<br><br>

**Help:**

If the program is given the -h parameter, it displays the help and description of accepted arguments:
```
python scanner.py -h
```
<br>

**Examples of usage:**


Scan a port on a single IP address.
This command scans port 80 on the IP address 192.168.1.1:
```
python scanner.py 192.168.1.1 -p 80
```
<br>


Scan a range of ports on a single IP address.
This command scans ports 1 to 100 on the IP address 192.168.1.1:
```
python scanner.py 192.168.1.1 -p 1-100
```
<br>


Scan a port on multiple IP addresses.
This command reads IP addresses from the "ips.txt" file and scans port 22 on each of them:
```
python scanner.py ips.txt -p 22
```
<br>


Scan a range of ports on multiple IP addresses.
This command reads IP addresses from the "ips.txt" file and scans ports 1 to 100 on each of them:
```
python scanner.py ips.txt -p 1-100
```
<br>


Scan a port on multiple IP addresses and log the results to a file.
This command reads IP addresses from the "ips.txt" file, scans port 80 on each of them, and saves the results to the "results.txt" file:
```
python scanner.py ips.txt -p 80 -log results.txt
```
<br>


Scan a range of ports on multiple IP addresses and log the results to a file.
This command reads IP addresses from the "ips.txt" file, scans ports 1 to 100 on each of them, and saves the results to the "results.txt" file:
```
python scanner.py ips.txt -p 1-100 -log results.txt
```
<br>

Planning to add:

Range of ips in arguments.

<br><br>






***Only Standard Libraries are used in this project:***

argparse: https://docs.python.org/3/library/argparse.html

socket: https://docs.python.org/3/library/socket.html

threading: https://docs.python.org/3/library/threading.html
