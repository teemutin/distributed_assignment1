import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))



def info():
    print("***Welcome to the chatroom***")
    print("Press 2 to change rooms ")
    print("Press 3 to send private message ")
    print("Press 0 to quit")
    print("Option ")
    print("Option ")
    choice = input("Your choice:   ")
    if choice == 2:
           print("Option ") 
    if choice == 3:
           print("Option ")
    if choice == 0:
        print("Cya later mate")

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
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

info()