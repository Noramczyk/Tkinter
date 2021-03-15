# Todo: Need to change FFFF values to 0 for inactivity. Currently reads as 255 and does not accurately display
#  inactivity
def HexToDec(file):
    with open("Hex1_out2.txt", 'w') as out_file, open('Hex1.txt') as in_file:
        for hex in in_file.read().split():
            print(int(hex, 32), file=out_file)
    return out_file.name
