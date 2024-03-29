#############################################################
#############################################################
#############################################################
#############################################################
###### THIS IS THE MAIN SERVER FILE #########################
###### THIS FILE CREATE SERVER ##############################
#############################################################
#############################################################
###### CREATED BY RISHABH ROY################################
#############################################################
#############################################################


from datetime import datetime
import socket

#############################################################
#############################################################
# making the storing file empty
file_ini = open('Server_data.txt', 'w+')
file_ini.write('')
file_ini.close()
#############################################################
#############################################################

#############################################################
#############################################################
# getting the ip address of the host PC
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("The host IP address is ", ip)  # ip --> IP address of the host pc

server_address = (ip, 6789)  # port and ip address
max_size = 100000  # number of bytes send per data
print("Starting the server at ", datetime.now())
print('Waiting for the client to call')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # creating socket
server.bind(server_address)  # binding the address
#############################################################
#############################################################


decision = True
while decision:

    data1, client = server.recvfrom(max_size)

    print('At', datetime.now(), client, 'said', data1)
    #####################################################
    #####################################################
    # Storing the data in a file
    if data1 != b'':
        dataforfile = data1.decode()
        file = open('Server_data.txt', 'a')
        file.write(dataforfile)
        file.close()
    # opening the file in read mode
    file = open('Server_data.txt', 'r')
    data = file.read()
    file.close()
    #############################################################
    #############################################################

    data_encode = data.encode() # encoding the data
    server.sendto(data_encode, client) # sending the encoding data

    #############################################################
    #############################################################

server.close()
