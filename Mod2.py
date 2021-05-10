import binascii
import codecs
import sys
import csv

file = open("rtcBytes.txt", "r+b")
#file = open("test5t.txt", "r+b")
outFile = open("t092616_sample_hold_mod.txt", "w")

#byte = file.read(3)

valList = [b'\xff\xff',b'\xff\xff', b'$\x10',b'\x10\x06', b'\x03!',b'\xff\xff',b'\xff\xff',b'9\x13',b'\x10\x06',b'\x03!']


count = 0
"""
with open("t092616_sample_hold.txt", "r+b") as input:
    byte = input.read(2)
    #val = int.from_bytes(byte, "little", signed="True")
    with open("out.txt", "w") as output:
        #byte = input.read(2)
        #val = int.from_bytes(byte, "little", signed="True")
        for byte in input:
            #byte = input.read(2)
            val = int.from_bytes(byte, "little", signed="True")
            if val > 2000:
            val = 50
        
        
while True:                             # Really long file parse nested loops

    byte = file.read(2)
    val = int.from_bytes(byte, "little", signed="True")

    with open("test5t.txt", "r+b") as input:
        byte = file.read(2)
           
        with open("out.txt", "w") as output:
            val = int.from_bytes(byte, "little", signed="True")

            if val > 2000:
                val = 50

            if count % 250 == 0:
                output.write(str(val))
                output.write('\n')
           
    if not val:
        break

print("File Parsed")



while True:
    #with open("test5t.txt", "r+b") as input:
        #data = file.readline()
    byte = file.read(2)
    val = int.from_bytes(byte, "little", signed="True")
    count += 1
    
    if val > 3000:
        val = 50
    if val < 0:
        val = 50
	
    if count % 250 == 0:
        outFile.write(str(val))
        outFile.write('\n')
    
    if count > 4000000:
        #if count >= 100000:
        break

print("file parsed")

"""


while count < 10:

   
    byte = file.read(2)                                         #The read() method returns the specified number of bytes from the file.
    val = int.from_bytes(byte, "little", signed="True")        # an int equivalent to the given byte
    #valList = val

    #bytesObj = bytes(str(byte), "utf-8")

    #val = binascii.b2a_hex(bytesObj)
    #val = binascii.unhexlify(byte)
    #val = binascii.hexlify(byte).decode('utf-8')
    #val = binascii.b2a_hex(byte, b'')

    #print(bytesObj)
    #print(ord(byte))
   
    #val = bytes(str(file), 'utf-8')
    #print(val)

    #with open("out.txt", "w") as f:
   	    #f.write(str(val))
   
    #val = from_bytes(byte, "big", signed="True")
    #convert= byte.decode('ASCII')
    #convert = binascii.hexlify(byte).decode('utf-8')
    #convert = format(byte,ord(byte))
    #convert = codecs.decode(byte)
    #byte_array = bytearray.fromhex(byte)
    #byte_array.decode()
    count+=1
    print(val)
    #print("Count: %r %r "%(count, val))

    #outFile.write(str(byte))
    #outFile.write('\n')
    """
    if val > 2000:
        val = 50
    
    if count %250 == 0:
    	outFile.write(str(val))
    	outFile.write('\n')
    """  
    



