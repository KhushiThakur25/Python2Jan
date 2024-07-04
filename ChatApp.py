import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit
from PyQt5.QtCore import QThread, pyqtSignal
import socket
import threading

class ChatClient(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 5000))
        
        self.receive_thread = ReceiveThread(self.client_socket)
        self.receive_thread.message_received.connect(self.display_message)
        self.receive_thread.start()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        layout.addWidget(self.chat_area)
        
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        input_layout.addWidget(self.input_field)
        
        send_button = QPushButton('Send')
        send_button.clicked.connect(self.send_message)
        input_layout.addWidget(send_button)
        
        layout.addLayout(input_layout)
        
        self.setLayout(layout)
        self.setWindowTitle('Chat Client')
        self.show()

    def send_message(self):
        message = self.input_field.text()
        if message:
            self.client_socket.send(message.encode())
            self.input_field.clear()
    def display_message(self,message):
        self.chat_area.append(message)

class ReceiveThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            try:
                data = self.client_socket.recv(1024).decode()
                if data:
                    self.message_received.emit(data)
            except:
                break

class ChatServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind(('localhost',5000))
        self.server_socket.listen(5)
        self.clients = []
    def start(self):
        print("Server started.. waiting for connection..")
        while True:
           client_socket,addr =  self.server_socket.accept()  
           print(f"New connection from {addr}")
           self.clients.append(client_socket)
           client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
           client_thread.start()
    def handle_client(self,client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Received : {message}")
                    self.broadcast(message,client_socket)
            except:
                self.clients.remove(client_socket) 
                client_socket.close()
                break      
                   
    def broadcast(self,message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode())
                except:
                    self.clients.remove(client)
                    client.close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        server = ChatServer()
        server.start()
    else:
        app = QApplication(sys.argv)
        client = ChatClient()
        sys.exit(app.exec_())