import socket

'''
11.04.18 АВК ОМА Козырев С.А
V 1.0
Определение работоспособности удаленной машины жерез сокетное соединение

модуль отсылает Email с сообщением о состоянии сервера 
это происходит по событию или безусловно в 00:00 каждый день
 
на сервере крутится сокетное соединение и при вриеме контрольной фразы 
она отправляется обратно
у клиента каждые 5 сек на сервер отправляется контрольная фраза
если ответа нет, то регистрируется событие, появление ответа - тоже событие
это прописывается в файл и отправляется Email

'''

                # это серверная часть


sock = socket.socket()
sock.bind(('', 9090))
while True:
    sock.listen(1)
    conn, addr = sock.accept()

    #print ('connected:', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())

conn.close()