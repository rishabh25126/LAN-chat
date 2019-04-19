#############################################################
#############################################################
#############################################################
#############################################################
###### THIS IS THE MAIN CLIENT FILE #########################
###### THIS FILE CREATE CLIENT ##############################
#############################################################
#############################################################
###### CREATED BY RISHABH ROY################################
#############################################################
#############################################################


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import socket
from datetime import datetime

#############################################################
#############################################################
# making the storing file empty
file_ini = open('Client_data.txt', 'w+')
file_ini.write('')
file_ini.close()
#############################################################
#############################################################

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        #############################################################
        #############################################################
        # Dimensions of window
        self.title = 'Client'
        self.left = 100
        self.top = 100
        self.width = 540
        self.height = 550
        #############################################################
        #############################################################

        self.initUI()


    def initUI(self):
        #############################################################
        #############################################################
        # Setting windows features
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #############################################################
        #############################################################

        #############################################################
        #############################################################
        # Create Labels
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)

        self.label1.setText("NAME :")
        self.label2.setText("IP :")
        self.label3.setText("Message :")
        self.label4.setText("Write a Message")

        self.label1.move(20,20)
        self.label2.move(240,20)
        self.label3.move(20,55)
        self.label4.move(20,480)
        #############################################################
        #############################################################

        #############################################################
        #############################################################
        # Create textbox
        self.textbox = QLineEdit(self) # textbox of message sending
        self.textbox.move(20,510)
        self.textbox.resize(350, 20)

        self.textbox1 = QPlainTextEdit(self) # receiving message box
        self.textbox1.move(20,80)
        self.textbox1.resize(500, 400)
        self.textbox1.setReadOnly(True)

        self.textbox2 = QLineEdit(self) #Name
        self.textbox2.move(70,25)
        self.textbox2.resize(150, 20)

        self.textbox3 = QLineEdit(self) #IP
        self.textbox3.move(280,25)
        self.textbox3.resize(150,20)
        #############################################################
        #############################################################

        #############################################################
        #############################################################
        # Create a button in the window
        self.button = QPushButton('Enter \\ Refresh', self)
        self.button.move(400,500)
        self.button.resize(100,40)
        self.button.clicked.connect(self.on_click) # Command on pressing the button
        #############################################################
        #############################################################

        self.show()

    #############################################################
    #############################################################
    #  main function of the client
    def clientfunc(self):
        self.hostnameOfClient = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostnameOfClient)
        print("The client IP address is ", self.ip)
        self.ip = self.textbox3.text() # ---> inputed IP address
        self.server_address = (self.ip, 6789) # IP address and port number to which the client has to connect
        self.max_size = 100000  # Max size of bytes send per data
        print("Starting the client at ", datetime.now())
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creating socket
        self.input1 = self.textbox.text() # message input
        self.input_data = self.input1.encode() # message is encoded to send
    #############################################################
    #############################################################

    #############################################################
    #############################################################
    # button press commands
    @pyqtSlot()
    def on_click(self):
        self.clientfunc()
        if self.input1 != "" and self.input1 != " " and self.input1 != "  ":

            #############################################################
            #############################################################
            # File handling
            self.file = open('Client_data.txt', 'w')
            self.file.write(self.textbox2.text() + ': ')
            self.file.write(self.input1)
            self.file.write("""
""")
            self.file.close()
            # openning the file in read mode
            self.file = open('Client_data.txt', 'r')
            self.dataFromFile = self.file.read()
            self.file.close()
            #############################################################
            #############################################################
            #############################################################
            self.dataFromFile_encode = self.dataFromFile.encode()
            self.client.sendto(self.dataFromFile_encode, self.server_address)  # sending the data

            self.data, self.server = self.client.recvfrom(self.max_size)  # receiving from client
            self.data_decode = self.data.decode()  # decoding the data

            #############################################################
            #############################################################
            # showing the data in the message box
            self.textbox1.setPlainText(self.data_decode)
            print("message :")
            print(self.data_decode)
            self.textbox.setText('')
            #############################################################
            #############################################################

        else :
            #############################################################
            #############################################################
            # File handling
            # openning the file in read mode
            self.file = open('Client_data.txt', 'r')
            self.dataFromFile = self.file.read()
            self.file.close()
            #############################################################
            #############################################################
            #############################################################
            self.dataFromFile_encode = self.dataFromFile.encode()
            self.client.sendto(b'', self.server_address)  # sending the data

            self.data, self.server = self.client.recvfrom(self.max_size)  # receiving from client
            self.data_decode = self.data.decode()  # decoding the data

            #############################################################
            #############################################################
            # showing the data in the message box
            self.textbox1.setPlainText(self.data_decode)
            self.textbox.setText('')
            #############################################################
            #############################################################


    #############################################################
    #############################################################
    #############################################################


#############################################################
#############################################################
# Constructing the main method
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
