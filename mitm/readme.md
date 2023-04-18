Pip commands
sudo pip install scapy


arp_poisning.py is a Python script that implements ARP poisoning to perform a MITM attack on a local network. The script uses Scapy, a powerful packet manipulation tool for network engineering and security, to send fake ARP messages to the network to associate the MAC address of the attacker's device with the IP address of the target device.

The script requires the following arguments to run:
target_ip: IP address of the target device on the local network host_ip: IP address of the attacker's device on the local network The script has two main functions:
_enable_linux_iproute() and _enable_windows_iproute(): These functions enable IP forwarding in the operating system so that the attacker's device can forward network traffic between the target device and the internet.
spoof(target_ip, host_ip, verbose=True): This function sends fake ARP messages to the target device to associate the MAC address of the attacker's device with the IP address of the target device. This allows the attacker to intercept and modify network traffic between the target device and the internet.
pseudocode for arp_poisning.py:
function _enable_linux_iproute():
// Enables IP route ( IP Forward ) in linux-based distro
function _enable_windows_iproute():
// Enables IP route (IP Forwarding) in Windows
function enable_ip_route(verbose=True):
// Enables IP forwarding
function get_mac(ip):
// Returns MAC address of any device connected to the network
// If ip is down, returns None instead
function spoof(target_ip, host_ip, verbose=True):
// Spoofs `target_ip` saying that we are `host_ip`.
// It is accomplished by changing the ARP cache of the target (poisoning)
// Sends the fake ARP message
// Prints the status message if verbose=True
http_pkts.py is another Python script that uses Scapy to capture and display HTTP packets in real-time. It can be used in combination with arp_poisning.py to intercept and monitor HTTP traffic between the target device and the internet.
To run http_pkts.py, simply execute the script in a terminal: python http_pkts.py
pseudocode for http_pkts.py:
function packet_callback(packet):
// Callback function to process the captured packet
// If the packet has a TCP layer and payload
// Decode the payload as UTF-8 and print the contents
try:
// Start capturing packets that match the filter criteria sniff(prn=packet_callback, filter="tcp and port 80")
except KeyboardInterrupt:
// Exit gracefully if the user interrupts the program print("\nExiting...")
To perform a man-in-the-middle attack using arp_poisoning.py and http_pkts.py, you can follow these steps:
1.	RUN arp -a
2.	Note down the  host is dns is winroute.uni-koblenz.de (141.26.64.9) at 00:00:5e:00:01:2a [ether] on ens3
3.	Now let suppose the target if is sparci-test-guestvm14.uni-koblenz.de (141.26.68.159) at 1e:00:26:00:00:1d
[ether] on ens3
4.	Now run the command
Sudo python3 arp_poisning.py 141.26.68.159 141.26.64.9 –verbose
5.	Open an other terminal and run http_pkts.py in another terminal window. This script listens for and intercepts HTTP packets being sent between the victim and the router. When a packet is intercepted, it prints out the contents of the packet.
6.	The command should look something like this: sudo python3 http_pkts.py
7.	Once both scripts are running, any HTTP traffic sent between the victim and the router will be intercepted and printed out in the http_pkts.py terminal window.
This includes any login credentials or other sensitive information sent over HTTP.
VPN Helps in preventing MITM Attacks
Regarding the security of performing a man-in-the-middle attack through a VPN, using a VPN can provide some level of protection against MITM attacks, as it encrypts the traffic between the client and the VPN server, making it more difficult for an attacker to intercept and read the traffic.
However, if the VPN server itself is compromised, the attacker could still intercept the traffic. After running the http_pkts.py you have noticed there is no packets captured.
 

## References:
https://en.wikipedia.org/wiki/Man-in-the-middle_attack 
https://www.cloudflare.com/learning/ssl/what-is-ssl-encryption/
https://www.owasp.org/index.php/Certificate_pinning
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
https://www.thepythoncode.com/code/building-arp-spoofer-using-scapy



To run codes ssh mubeen@141.26.68.158 -p 22 password 12345
cd mitm
ls
