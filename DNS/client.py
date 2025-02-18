from zeroconf import Zeroconf, ServiceBrowser, ServiceListener

class MyListener(ServiceListener):
    def add_service(self, zeroconf, type, name):
        print(f"Service found: {name}")
        info = zeroconf.get_service_info(type, name)
        if info:
            address = socket.inet_ntoa(info.addresses[0])
            print(f"  IP: {address}")
            print(f"  Port: {info.port}")
            print(f"  Properties: {info.properties}")

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

try:
    input("Press Enter to stop discovery...\n")
finally:
    zeroconf.close()
