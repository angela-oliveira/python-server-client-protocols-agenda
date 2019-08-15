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
        
    celular = str(input('Celular: '))
    telefone = str(input('Telefone: '))
    
    dados_bd['Nome'] = nome
    dados_bd['Celular'] = celular
    dados_bd['Telefone'] = telefone


    dadosJson = json.dumps(dados_bd)
    print('{} Inserido na lista'.format(nome))

    tcp.sendall(dadosJson.encode()) #dadosenviados

    # tcp.sendall(nome.encode() + " ".encode() + celular.encode() + " ".encode() + telefone.encode())
    # celular = str(input('celular: '))
    # telefone = str(input('telefone: '))
        
tcp.close()


'''
#Biblioteca json
import json

#Criando dicionario
dados_bd = {}

#Inserindo no dicionario
dados_bd['nome'] = "Andreia"
dados_bd['tel'] = 123
dados_bd['cel'] = 1234

#Printando o dicionario
print(dados_bd)

print("\n")

#Printando dados com for
for i in dados_bd:
    print(dados_bd[i])

print('\n')

#Printando um dado pela chave nome
print(dados_bd['nome'])
print('\n')

#Transformando em json
exemplo_json = json.dumps(dados_bd)

#JSON
print(exemplo_json)
'''