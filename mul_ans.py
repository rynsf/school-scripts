from preetyprint import leftpad

a = input("Enter multiplier: ")
b = input("Enter multiplicand: ")

maxlen = len(str(int(a) * int(b)))

print(leftpad(maxlen, a))
print(leftpad(maxlen, 'x'+b))
print("_"*maxlen)

p = 0

for n in b[::-1]:
    out = str(int(n) * int(a))
    print(leftpad(maxlen, out + "X"*p))
    p += 1

print("_"*maxlen)
print(int(a)*int(b))

