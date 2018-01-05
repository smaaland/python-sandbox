import hashlib

input_str = 'bgvyzdsv'

num = 0
while True:
    if hashlib.md5((input_str + str(num)).encode('utf-8')).hexdigest().startswith('00000'):
        print(num)
        break
    num += 1

while True:
    if hashlib.md5((input_str + str(num)).encode('utf-8')).hexdigest().startswith('000000'):
        print(num)
        break
    num += 1