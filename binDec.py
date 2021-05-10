# Todo: Need to change FFFF values to 0 for inactivity. Currently reads as 255 and does not accurately display
#  inactivity
import binascii
import mmap


def convertHex(inputFile):
    j = 0
    # convert the bytes to a utf-8 string and split the fields
    # binascii.hexlify = convert binary to hex
    
    while True:
        data = inputFile.readline()
        content = binascii.hexlify(data).decode('utf-8')
        content = " ".join(content[i:i + 2] for i in range(0, len(content), 2))
        
        for b in content.split():
            yield b
        if not data:
            break
        """
        j += 1

        if j % 250 == 0:
                
            for b in content.split():
            #j += 1
            #if j % 250 == 0:
                yield b

        if not data:
            break
        """

inputFile = "t092616_sample_hold.txt"
with open(inputFile, 'r+b') as f, open("outSampleComp.txt", "w") as out_file:
    for line in convertHex((f)):
        print(int(line, 16), file=out_file)

        #return out_file.name



print("File Parsed")