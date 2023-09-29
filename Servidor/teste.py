from rich.console import Console
import socket
import threading
import datetime
import os

def informacoes(conn):
    mensagem = "jv bota".encode()
    conn.sendall(mensagem)
    print("mensagem enviada com sucesso")

def hora_atual(conn):
    tempo = datetime.datetime.now()
    hora_formatada = tempo.strftime("%H:%M:%S")
    conn.sendall(f"hora atual {hora_formatada}\n".encode())

def dados_arq(conn, nome_arquivo):
    try:
        with open(nome_arquivo, "rb") as f:
            dados = f.read()
        conn.sendall(dados)
        print(f"Enviado arquivo {nome_arquivo} para o cliente")
    except FileNotFoundError:
        conn.sendall("Arquivo não encontrado".encode())

def lista_arq(conn):
    diretorio = os.path.dirname(os.path.abspath(__file__))
    pasta_dos_arquivos = os.path.join(diretorio, "Arquivos")
    arquivos_na_pasta = os.listdir(pasta_dos_arquivos)
    lista = "\n".join(arquivos_na_pasta)
    conn.sendall(f"LISTA DE ARQUIVOS:\n{lista}\n".encode())

def saindo(conn):
    conn.sendall("Fechando a conexão".encode())
    print("ADEUS")

def comandos(conn, command):
    if command == "consulta":
        informacoes(conn)
    elif command == "hora":
        hora_atual(conn)
    elif command.startswith("arquivo_"):
        nome_arquivo = command.split("_")[1]
        dados_arq(conn, nome_arquivo)
    elif command == "listar":
        lista_arq(conn)
    elif command == "sair":
        saindo(conn)
    else:
        conn.sendall("comando desconhecido".encode())

def identificador_cliente(conn, ender):
    print("Conectado em", ender)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                console.print(f'Fechando a conexão com {ender}', style="#ff0000 bold")
                conn.close()
                break
            else:
                command = data.decode()
                comandos(conn, command)
    except ConnectionResetError:
        console.print('Erro de conexão: conexão resetada pelo cliente', style="#ff0000 bold")

console = Console()

HOST = '127.0.0.2'
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
console.print('Aguardando conexão de um cliente', style="#0033D6 bold")

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=identificador_cliente, args=(conn, addr))
    thread.start()