# Cliente TCP
from rich.console import Console
from rich.table import Table
import socket

console = Console()


def menu():
    table = Table(title="[#FFB703]Opções Disponiveis", style="#FB8500")
    table.add_column("Opção", justify="center", style="#8ECAE6", no_wrap=True)
    table.add_column("Descrição", style="#8ECAE6")

    table.add_row("1", "Consulta informações")
    table.add_row("2", "Hora do servidor")
    table.add_row("3", "Arquivos")
    table.add_row("4", "Listar Arquivos")
    table.add_row("5", "Fechar Conexão")
    console.print(table)
    opcao = console.input('[#8ECAE6]Digite uma opção: ')
    return opcao
    
HOST = '127.0.0.2'
PORT = 5000
ADDR = (HOST, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while(True):

    opcao = menu()
    if opcao == '1':
        client.sendall(str.encode('consulta'))
        data = client.recv(1024)
        console.print('Mensagem ecoada:',data.decode(),style="#009A05 bold")
    elif opcao == '2':
        client.sendall(str.encode('hora'))
        data = client.recv(1024)
        console.print(':watch:',data.decode(),style="#009A05 bold")
    elif opcao == '3':
        client.sendall(str.encode('arquivo'))
        nome = console.input(':file_folder: [#8ECAE6]Digite o Nome do Arquivo:')
        try:
            with open(nome, 'r') as f:
                file_contents = f.read()
                client.sendall(str.encode(file_contents))
                data = client.recv(1024)
                console.print('Mensagem ecoada:',data.decode(),style="#009A05 bold")
        except FileNotFoundError:
            console.print(f'Arquivo {nome} não encontrado',style="#FF0000 bold")
    elif opcao == '4':
        client.sendall(str.encode('listar'))
        data = client.recv(1024)
        console.print('Mensagem ecoada:',data.decode(),style="#009A05 bold")
    elif opcao == '5':
        client.sendall(str.encode('sair'))
        data = client.recv(1024)
        console.print('Bye Bye ! ',data.decode(),style="#06d6a0 bold")
        break

#print('Mensagem ecoada:', data.decode())
