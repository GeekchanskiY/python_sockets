import socket

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

addr = ("", 8080)  # all interfaces, port 8080
if socket.has_dualstack_ipv6():
    s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
else:
    s = socket.create_server(addr)

print(socket.gethostbyaddr("127.0.0.1"))
