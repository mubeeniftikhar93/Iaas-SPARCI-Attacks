import socket

website = "sparci-test-mgmt.uni-koblenz.de"  # Replace with the website you want to get the IP address of

ip_address = socket.gethostbyname(website)

print("The IP address of", website, "is", ip_address)
