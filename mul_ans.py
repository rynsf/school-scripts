a = input("Enter multiplier: ")
b = input("Enter multiplicand: ")

maxlen = len(str(int(a) * int(b)))

print(" "*(maxlen-len(a)) + a)
print(" "*(maxlen-len(b)-1) + "x" + b) # TODO just write a left pad function!
print("_"*maxlen)

p = 0

for n in b:
    out = str(int(n) * int(a))
    print(" "*(maxlen-len(str(out))-p) + out + "X"*p)
    p += 1

print("_"*maxlen)
print(int(a)*int(b))

