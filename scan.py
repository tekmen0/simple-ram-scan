import sys
import psutil

bomb = []

MB = 1024*1024
GB = MB*1024

GB_limit = int(input("MAx GB's to fill? :"))

for i in range(GB_limit):
	for j in range(1024):
		bomb.append(' '* MB) 
		mem = psutil.virtual_memory()
		total, free, used = int(mem.total/MB), int(mem.available/MB), int(mem.used/MB)
		print("Total: {} in-use: {} free: {} program-used: {}" .format(total, used, free, i*1024+j),end='\r')
		if free <= 100 : 
			print()
			print("100 MB of memory available, exiting")
			sys.exit(0);
	print()
	print("{}/{} GB has been allocated on RAM".format(i+1,GB_limit))
	
sys.exit(0)

