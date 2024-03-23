import socket
import threading
chat = []
all_threads = []
channels= {}
groups= {}
connections = {}
def handle_client(conn, addr):

    while(True):
        print("[thread] starting")

        # recv message
        try:
            message = conn.recv(1024)
            
            
        except:
            break
            

        message = message.decode()
        print("[thread] client:", addr, 'recv:', message)
        l = []
        x = message.split(';')
        if(x[0] == "chatinfo"):
            
            connections[x[1]] = conn
            chat.append(x[1])
            print(x[1], " connected...")
        if(x[0] == "createchannel"):# message type : createchannel;channelname 
            if(x[1] not in channels):
                channels[x[1]] = []
                channels[x[1]].append(conn)
                print(x[1])

        if(x[0] == "joinchannel"):# message type : joinchannel;channelname;username
            channels[x[1]].append(connections[x[2]])
            print(x[2],' joined...')

        if(x[0] == "sendtochannel"): # message type sendtochannel;channelname;username;message
            for i in channels[x[1]]:
                msg = ";".join(x)
                print(msg)
                i.send(msg.encode())
        if(x[0] == "creategroup"):# message type : creategroup;groupname 
            if(x[1] not in groups):
                groups[x[1]] = []
                groups[x[1]].append(conn)
                print(x[1])

        if(x[0] == "joingroup"):# message type : joingroup;groupname;username
            groups[x[1]].append(connections[x[2]])
            print(x[2],' joined...')

        if(x[0] == "sendtogroup"): # message type sendtogroup;groupname;username;message
            for i in groups[x[1]]:
                msg = ";".join(x)
                print(msg)
                i.send(msg.encode())

        if(x[0] == "getChat"):
            l.append("getChat")
            for i in chat:
                if(i == x[1]):
                    l.append(i)
            for i in channels:
                if(i.startswith(x[1])):
                    l.append(i)
            for i in groups:
                if(i.startswith(x[1])):
                    l.append(i)

        if(x[0] == "send"):
            connections[x[1]].send(message.encode())
            continue
            
        message = ";".join(l)
        print(message)
        message = message.encode()
        conn.send(message)
        print("[thread] client:", addr, 'send:', message)
        

    

host = '127.0.0.1'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((host, port))
s.listen()
try:
    while True:
        print("Waiting for client")
        conn, addr = s.accept()
        
        print("Client:", addr)
        
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
    
        all_threads.append(t)
except KeyboardInterrupt:
    print("Stopped by Ctrl+C")
finally:
    if s:
        s.close()
    for t in all_threads:
        t.join()