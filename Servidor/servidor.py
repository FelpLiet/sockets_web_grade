#Servidor TCP

import socket
import threading
import datetime

def informacoes():
   mensagem = "jv bota".encode()
   conn.sendall(mensagem)
   print("mensagem enviada com sucesso")

def comandos(command):
   if command == "consulta":
      informacoes()
"""   elif command == "hora":
      hora_atual()
   elif command == "arquivo":
      nome_arq   
   elif command == "listar":
      lista_arq()
   elif command == "sair":
      adeus()     
   else:
      comando_desconhecido()  """

def identificador_cliente():
   pass

HOST  = '127.0.0.2'
PORT  = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print ('Aguardando conexão de um cliente')
conn, ender = s.accept()
print ('Conectado em', ender)
thread = threading.thread(target=identificador_cliente ,args=(conn, ender))
thread.start()
while True:
   data = conn.recv(1024)
   command = data.decode()
   if not data:
      print ('Fechando a conexão')
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
