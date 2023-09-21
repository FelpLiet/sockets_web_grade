#Servidor TCP
from rich.console import Console
import socket
import threading
import datetime

def informacoes():
   mensagem = "jv bota".encode()
   conn.sendall(mensagem)
   print("mensagem enviada com sucesso")

def hora_atual():
   tempo = datetime.datetime.now()
   hora_formatada = tempo.strftime("%H:%M:%S")
   conn.sendall(f"hora atual {hora_formatada}\n".encode())

def nome_arq():
   pass

def lista_arq():
   pass

def saindo():
   conn.sendall("Fechando a conexão".encode())
   print("ADEUS") 
   conn.close()

def comandos(command):
   if command == "consulta":
      informacoes()
   elif command == "hora":
      hora_atual()
   elif command == "arquivo":
      nome_arq   
   elif command == "listar":
      lista_arq()
   elif command == "sair":
      saindo() 
   else:
      conn.sendall("comando desconhecido".encode())

def identificador_cliente():
   pass

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
   command = data.decode()
   if not data:
      console.print('Fechando a conexão',style="#ff0000 bold")
      #print ('Fechando a conexão')
      conn.close()
      break
   else:
      comandos(command)

"""def start():
   print("iniciando o socket")
   s.listen()
   while(True):
      conn, addr = s.accept()
      thread = threading.thread(target=identificador_cliente ,args=(conn, addr))
      thread.start()"""
