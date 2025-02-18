from zeroconf import Zeroconf, ServiceInfo
import socket

service_name = "MyWebServer._http._tcp.local."
service_type = "_http._tcp.local."
port = 8080
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

info = ServiceInfo(
    service_type,
    service_name,
    addresses=[socket.inet_aton(local_ip)],
    port=port,
    properties={"version": "1.0", "description": "My web server"},
    server=hostname + ".local."
)

zeroconf = Zeroconf()
zeroconf.register_service(info)
print(f"Service announced: {service_name} running in {local_ip}:{port}")

try:
    input("Press Enter to stop...\n")
finally:
    zeroconf.unregister_service(info)
    zeroconf.close()