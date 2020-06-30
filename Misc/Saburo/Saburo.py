from pwn import *

context.log_level = 'error'

def mean(a):
    return sum(a)/len(a)

n = [chr(i) for i in range(0x20,0x7F)]


qqqq = 'A1r1ght_U_4r3_my_3n3nnies'
while True:
    print('AIS3{' + qqqq)
    d = {}
    for j in n:
        nn = []
        for i in range(5):
            r = remote('60.250.197.227',11001)
            r.recvuntil(':')
            r.sendline('AIS3{'+ qqqq +j)
            l = r.recvuntil('.')
            # print(l.split(' ')[5])
            nn.append(int(l.split(' ')[5]))
            r.close()
        d[j] = mean(nn)
        print(d)


    print(d.keys()[d.values().index(max(d.values()))],max(d.values()))
    qqqq += d.keys()[d.values().index(max(d.values()))]