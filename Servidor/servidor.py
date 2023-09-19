#Servidor TCP
from rich.console import Console
import socket

console = Console()

HOST  = '127.0.0.2'
PORT  = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
console.print('Aguardando conexão de um cliente',style="#0033D6 bold")
#print ('Aguardando conexão de um cliente')
conn, ender = s.accept()
console.print('Conectado em',ender,style="#009A05 bold")
#print ('Conectado em', ender)
while True:
   data = conn.recv(1024)
   if not data:
      console.print('Fechando a conexão',style="#ff0000 bold")
      #print ('Fechando a conexão')
      conn.close()
      break
   conn.sendall(data)
