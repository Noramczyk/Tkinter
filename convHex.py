import codecs
"""
with open("testHex.txt", 'r') as f:
	data = f.read()
	for i in range(len(data)//2):
		print(codecs.decode(data[i*2:i*2+2], "hex").decode("utf-8"), end="")

print(codecs.decode("200260003B003B003B003B003B003B003B003B003B003B003B003B003A003B003B003B00", "hex").decode("utf-16"))



def hex2dec(s):
    return the integer value of a hexadecimal string s
    return int(s, 16)
"""

print(int("2B202B202B202B202B202B202B202B202B202B202B202B202B202A202B202B20", 16))
print(int(hex, 32),"2B202B202B202B202B202B202B202B202B202B202B202B202B202A202B202B20")