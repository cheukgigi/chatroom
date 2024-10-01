import socket
import threading
host = '127.0.0.1'
port = 9090
# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


# Starting Threads For Listening And Writing
receive_thread_1 = threading.Thread(target=receive)
receive_thread_1.start()

receive_thread_2 = threading.Thread(target=receive)
receive_thread_2.start()

receive_thread_3 = threading.Thread(target=receive)
receive_thread_3.start()

write_thread = threading.Thread(target=write)
write_thread.start()