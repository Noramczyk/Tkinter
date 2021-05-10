import binascii
import codecs
import sys
import csv

def convertHex(inputFile):

    count = 0
    while True:

        byte = inputFile.read(2)
        val = int.from_bytes(byte, "little", signed="True")
        count += 1
	    
        if val > 3000:
            val = 50
        if val < 0:
            val = 50
        if count % 250 == 0:
            yield val
 
        if not val:                      
	        #if count >= 100000:
            break

def hexGenerator(inputFile):
    with open(inputFile, 'r+b') as f, open("out.txt", "w") as out_file:
        for line in convertHex((f)):
            print(int(line), file=out_file)
            #print("\n", file=out_file)

    return out_file.name


print("Parsing File....")