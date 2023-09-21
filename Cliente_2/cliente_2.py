# Cliente TCP
from rich.console import Console
import socket

console = Console()

HOST = '127.0.0.2'
PORT = 5000
ADDR = (HOST, PORT)

def consulta():
    pass

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.sendall(str.encode('Bom dia'))
data = client.recv(1024)
console.print('Mensagem ecoada:',data.decode(),style="#009A05 bold")
#print('Mensagem ecoada:', data.decode())
