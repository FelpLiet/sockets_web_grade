#Servidor TCP
from rich.console import Console
import socket
import threading
import datetime
import os

def informacoes():
   mensagem = "jv bota".encode()
   conn.sendall(mensagem)
   print("mensagem enviada com sucesso")

def hora_atual():
   tempo = datetime.datetime.now()
   hora_formatada = tempo.strftime("%H:%M:%S")
   conn.sendall(f"hora atual {hora_formatada}\n".encode())


def dados_arq(nome_arquivo):
   diretorio = os.path.dirname(os.path.abspath(__file__))
   pasta_dos_arquivos = os.path.join(diretorio, "Arquivos")
   caminho = os.path.join(pasta_dos_arquivos, nome_arquivo)
   try:
      with open(caminho, "rb") as f:
         dados = f.read()
      conn.sendall(dados)
      console.print(f"Enviado arquivo {nome_arquivo} para o cliente",style="#0033D6 bold")
   except FileNotFoundError:
      conn.sendall("Arquivo nao encontrado".encode())


def lista_arq():
   diretorio = os.path.dirname(os.path.abspath(__file__))
   pasta_dos_arquivos = os.path.join(diretorio, "Arquivos")
   arquivos_na_pasta = os.listdir(pasta_dos_arquivos)
   lista = "\n".join(arquivos_na_pasta)
   conn.sendall(f"LISTA DE ARQUIVOS:\n{lista}\n".encode())

def saindo():
   conn.sendall("Fechando a conexão".encode())
   print("ADEUS")


def comandos(command):
   if command == "consulta":
      informacoes()
   elif command == "hora":
      hora_atual()
   elif command.startswith("arquivo_"):
      
      nome_arquivo = command.split("_")[1]
      dados_arq(nome_arquivo)         
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
ADDR  = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()
console.print('Aguardando conexão de um cliente',style="#0033D6 bold")
conn, ender = s.accept()
console.print('Conectado em', ender,style="#009A05 bold")
while True:
   data = conn.recv(1024)
   command = data.decode()
   if not data:
      console.print('Fechando a conexão',style="#ff0000 bold")
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
