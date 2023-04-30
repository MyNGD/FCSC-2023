from pwn import *

HOST, PORT = "challenges.france-cybersecurity-challenge.fr", 2052

def comparer(x, y):
	io.sendlineafter(b">>> ", f"comparer {x} {y}".encode())
	return int(io.recvline().strip().decode())

def echanger(x, y):
	io.sendlineafter(b">>> ", f"echanger {x} {y}".encode())

def longueur():
	io.sendlineafter(b">>> ", b"longueur")
	return int(io.recvline().strip().decode())

def verifier():
	io.sendlineafter(b">>> ", b"verifier")
	r = io.recvline().strip().decode()
	if "flag" in r:
		print("\n" + r + "\n")
	else:
		print(io.recvline().strip().decode())
		print(io.recvline().strip().decode())

def quick_sort(debut, fin):
	if debut < fin:
		pivot = partition(debut, fin)
		quick_sort(debut, pivot-1)
		quick_sort(pivot+1, fin)

def partition(debut, fin):
	pivot_index = (debut + fin) // 2
	echanger(pivot_index, fin)
	i = debut - 1
	for j in range(debut, fin):
		if comparer(j, fin) == 1:
			i += 1
			echanger(i, j)
	echanger(i+1, fin)
	return i+1

def trier(N):
	quick_sort(0, N-1)

io = remote(HOST, PORT)

N = longueur()

trier(N)

verifier()

io.close()
