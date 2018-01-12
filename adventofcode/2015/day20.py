val = 36000000
top = int(val / 10)
packets = [0 for _ in range(val)]
max_packets = 0
stop = False

for i in range(1, top + 1):
    for j in range(i, top + 1, i):
        # if j not in packets.keys():
        #     packets[j] = 0

        packets[j] += i

        if packets[j] > max_packets:
            max_packets = packets[j]
            print(max_packets)

        if packets[j] >= top:
            stop = True
            print('---')
            print(packets[j])
            print(j)

    if stop:
        exit()

# 3326400 fail
