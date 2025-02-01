from zeroconf import Zeroconf, ServiceInfo
import socket

# Definir o serviço e a estrutura dos dados
SERVICE_TYPE = "_gpuinfo._tcp.local."
SERVICE_NAME = "RTX_A4000._gpuinfo._tcp.local."
PORT = 5000  # Porta fictícia para representar um serviço associado

# Informações da GPU formatadas para serem anunciadas via TXT records
gpu_data = {
    "name": "NVIDIA RTX A4000",
    "cuda": "6144",
    "base": "735 MHz",
    "boost": "1560 MHz",
    "mem_type": "GDDR6",
    "mem_cap": "16 GB",
    "tdp": "140 W",
    "psu": "550 W",
    "features": "RayTracing, DLSS, VR, CUDA, RTX_IO",
    "apps": "AI, 3D, Video, GameDev, CAD"
}

# Converter os dados para o formato aceito pelo zeroconf (dict de bytes)
properties = {k: v.encode("utf-8") for k, v in gpu_data.items()}

# Obter o IP local
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Criar o serviço DNS-SD
info = ServiceInfo(
    SERVICE_TYPE,
    SERVICE_NAME,
    addresses=[socket.inet_aton(local_ip)],
    port=PORT,
    properties=properties,
    server=hostname + ".local."
)

# Anunciar o serviço na rede
zeroconf = Zeroconf()
zeroconf.register_service(info)
print(f"Serviço anunciado: {SERVICE_NAME} rodando em {local_ip}:{PORT}")
print("Pressione Ctrl+C para parar o serviço.")

try:
    while True:
        pass  # Mantém o serviço ativo
except KeyboardInterrupt:
    print("Desregistrando serviço...")
    zeroconf.unregister_service(info)
    zeroconf.close()
