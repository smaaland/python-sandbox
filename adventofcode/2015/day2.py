with open('input2.txt', 'r') as f:
    total = 0
    for line in f:
        parts = line.split('x')
        smallest = 100000
        for exclude in range(3):
            to_check = [x for x in range(3) if x != exclude]
            total += to_check[0] * to_check[1]
            #smallest = total if total < smallest
