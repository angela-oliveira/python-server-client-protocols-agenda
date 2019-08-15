#########  SERVIDOR  #################
import socket
import _thread
import db


HOST = '' # Endereco IP do Servidor
PORT = 5005 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(3)


def conectado(con, cliente):
    print('Conectado por', cliente)
    conec = db.connection()
    while True:
        '''nome = con.recv(1024).decode('utf-8')
        celular = con.recv(1024).decode('utf-8')
        telefone = con.recv(1024).decode('utf-8')'''
        dados_list = con.recv(1024).decode().split(' ')
        if dados_list[0] == 'STOP':
            print('Finalizando conexão com', cliente)
            break
            
        db.insert_table(conec,dados_list[1],dados_list[3],dados_list[5])
        db.select_table(conec) #exibe os dados do banco
        print("Dados recebidos: ",dados_list)
        #con.close()
        #_thread.exit()
            
while True:
 con, cliente = tcp.accept()
 _thread.start_new_thread(conectado, tuple([con, cliente]))
tcp.close()
