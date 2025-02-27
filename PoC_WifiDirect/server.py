import socket
import torch

# Configura o socket
HOST = "0.0.0.0"  # Aceita conexões de qualquer IP
PORT = 5001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Aguardando conexão...")
conn, addr = server.accept()
print(f"Conectado a: {addr}")

# Recebe os dados e processa na GPU
data = conn.recv(1024).decode()
tensor_data = torch.tensor([float(i) for i in data.split(",")]).cuda()
result = tensor_data.sum().item()

# Envia resposta
conn.send(str(result).encode())
conn.close()
