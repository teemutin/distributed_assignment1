import socket

def mainprogram() :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),1234))
    s.listen(5)
    print("Terkkuja!asdasd")

mainprogram()