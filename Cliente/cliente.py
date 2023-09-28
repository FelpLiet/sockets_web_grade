import socket
from rich.console import Console

console = Console()

def menu():
    console.print("Menu de opções",style="#0033D6 bold")
    console.print("1 - Consultar informações do sistema", style="#0033D6 bold")
    console.print("2 - Consultar hora do servidor", style="#0033D6 bold")
    console.print("3 - Consultar nome de um arquivo", style="#0033D6 bold")
    console.print("4 - Listar arquivos do diretório", style="#0033D6 bold")
    console.print("5 - Sair", style="#0033D6 bold")
    opcao = input("Digite a opção desejada: ")
    return opcao

HOST = '127.0.0.2'
PORT = 5000
ADDR = (HOST, PORT)


connec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connec.connect(ADDR)
print('Conectado ao servidor')
while True:
    opcao = menu()
    print(opcao)
    if opcao == '1':
        connec.sendall(str.encode("consulta"))
        data = connec.recv(1024)
        print('Mensagem ecoada:', data.decode())
    elif opcao == '2':
        connec.sendall(str.encode("hora"))
        data = connec.recv(1024)
        print('Mensagem ecoada:', data.decode())
    elif opcao == '3':
        connec.sendall(str.encode("arquivo"))
        nome = input("Digite o nome do arquivo: ")
        connec.sendall(str.encode(nome))
        data = connec.recv(1024)
        print('Mensagem ecoada:', data.decode())
    elif opcao == '4':
        connec.sendall(str.encode("listar"))
        data = connec.recv(1024)
        print('Mensagem ecoada:', data.decode())
    elif opcao == '5':
        connec.sendall(str.encode("sair"))
        print("Saindo do programa")
        break
