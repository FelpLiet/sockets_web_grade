import socket
from rich.console import Console
from rich.table import Table

console = Console()

def menu():
    table = Table(title="[#FFB703]Opções Disponiveis", style="#FB8500")

    table.add_column("Opções", justify="center")
    table.add_column("Descrição", justify="center")

    table.add_row("1", "Consultar informações do sistema")
    table.add_row("2", "Consultar hora do servidor")
    table.add_row("3", "Consultar nome de um arquivo")
    table.add_row("4", "Listar arquivos do diretório")
    table.add_row("5", "Sair")

    console.print(table)

    opcao = console.input("[#8ECAE6]Digite a opção desejada: ")
    return opcao

def nome_cliente(client_socket):
    nome = console.input('Digite seu nome: ')
    client_socket.sendall(nome.encode())

HOST = '127.0.0.2'
PORT = 5000
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Solicita ao cliente que forneça seu nome
nome_cliente(client)

print('Conectado ao servidor')
while True:
    opcao = menu()
    if opcao == '1':
        client.sendall(str.encode('consulta'))
        data = client.recv(1024)
        console.print('Infos do Servidor: ', data.decode(), style="#009A05 bold")

    elif opcao == '2':
        client.sendall(str.encode('hora'))
        data = client.recv(1024)
        console.print(':watch:', data.decode(), style="#009A05 bold")

    elif opcao == '3':
        nome = console.input(':file_folder: [#8ECAE6]Digite o Nome do Arquivo:')
        nome = "arquivo_" + nome + ".txt"
        client.sendall(nome.encode())

        data = client.recv(1024)

        if "Arquivo nao encontrado" in data.decode():
            console.print("Arquivo não encontrado no servidor",
                          style="#ff0000 bold")
        else:
            with open(nome.split("_")[1], "wb") as f:
                f.write(data)
            console.print(
                f"Arquivo {nome} recebido com sucesso", style="#009A05 bold")
            print(data)

    elif opcao == '4':
        client.sendall(str.encode('listar'))
        data = client.recv(1024)
        console.print('Mensagem ecoada:', data.decode(), style="#009A05 bold")

    elif opcao == '5':
        client.sendall(str.encode('sair'))
        data = client.recv(1024)
        console.print('Bye Bye ! ', data.decode(), style="#06d6a0 bold")
        client.close()
        break
    else:
        console.print('Opção inválida', style="#ff0000 bold")