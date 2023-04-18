import socket
import subprocess

# replace example.com with the website you want to get the gateway for
website = 'sparci-test-mgmt.uni-koblenz.de'

# get the IP address of the website
ip_address = socket.gethostbyname(website)

# execute a shell command to get the gateway IP address
result = subprocess.check_output(['ip', 'route', 'get', ip_address])

# decode the byte string output to a string
result_str = result.decode('utf-8')

# extract the gateway IP address from the result string
gateway = result_str.split(' ')[2]

print('Gateway IP Address:', gateway)
