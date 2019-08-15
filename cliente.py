########### CLIENTE #############
import socket
import json

# TCP
# socket

HOST = '127.0.0.1'  # Endereco IP do Servidor

PORT = 5005  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print('Para sair use CTRL+X\n')

print("Agenda")
print("Para fechar a agenda digite 'stop'")

dados_bd = {}


while True:

    nome = input('Nome: ')

    if nome == 'stop':
        tcp.sendall('STOP'.encode())
        print("Agenda fechada!")
        tcp.close()
        break
    if nome == '':
        print("Insira um nome")
        continue
        
    celular = str(input('Celular: '))
    telefone = str(input('Telefone: '))
    
    dados_bd['Nome'] = nome
    dados_bd['Celular'] = celular
    dados_bd['Telefone'] = telefone


    dadosJson = json.dumps(dados_bd)
    

    tcp.sendall(dadosJson.encode()) #dadosenviados

    print(tcp.recv(1024).decode()) #Resposta do banco

    # tcp.sendall(nome.encode() + " ".encode() + celular.encode() + " ".encode() + telefone.encode())
    # celular = str(input('celular: '))
    # telefone = str(input('telefone: '))
        
tcp.close()
