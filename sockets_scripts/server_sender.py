import socket, cv2, pickle,struct,time
import pyshine as ps

mode =  'send'
name = 'Artesh Serri Server Side'
audio,context= ps.audioCapture(mode=mode)
#ps.showPlot(context,name)

# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '0.0.0.0'
port = 4982
backlog = 5
socket_address = (host_ip,port)
print('Server Started',socket_address,'...')
server_socket.bind(socket_address)
server_socket.listen(backlog)

while True:
	client_socket,addr = server_socket.accept()
	print('Room-User Connected:',addr)
	if client_socket:

		while(True):
			frame = audio.get()
			
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			
	else:
		break

client_socket.close()