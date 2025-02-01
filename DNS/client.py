from zeroconf import Zeroconf, ServiceBrowser, ServiceListener

class MyListener(ServiceListener):
    def add_service(self, zeroconf, type, name):
        print(f"Serviço encontrado: {name}")
        info = zeroconf.get_service_info(type, name)
        if info:
            address = socket.inet_ntoa(info.addresses[0])
            print(f"  IP: {address}")
            print(f"  Porta: {info.port}")
            print(f"  Propriedades: {info.properties}")

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

try:
    input("Pressione Enter para parar a descoberta...\n")
finally:
    zeroconf.close()
