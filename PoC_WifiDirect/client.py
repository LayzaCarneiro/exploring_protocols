import socket

# HOST = "192.168.1.1"  # IP do servidor Wi-Fi Direct
HOST = "127.0.0.1"  # IP local (loopback)
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Enviar dados para a GPU processar
data = "1.5,2.3,3.7"  # Simulação de dados
client.send(data.encode())

# Receber resultado da GPU
response = client.recv(1024).decode()
print("Resultado da GPU:", response)

client.close()
