__author__ = 'smaaland'

elf = 2
packets = dict()

current_house = 1

while True:

    for y in range(1, current_house+1):
        # Go through the elves
        # Should elf x put packets in house y?
        if current_house%y == 0:
            # Yes
            if not y in packets:
                packets[y] = 0
            packets[y] += 10*y
    # packets[elf] = elf
    current_house += 1
    if current_house == 3:
        print(packets)
        exit()