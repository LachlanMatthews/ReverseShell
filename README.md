# ReverseShell
Created and tested with two Virtual Machines running at the same time. Assumes the script will be somehow executed on the target machine. The attacking machine listens for port 5555 using netcat and finds a connection once the script is executed on the target machine.

On the kali machine:
	nc ‐v ‐l ‐p 5555
On the ubuntu machine:
	python client.py
	    or
	python3 client.py

on the kali machine:
	enter commands and type quit when done
