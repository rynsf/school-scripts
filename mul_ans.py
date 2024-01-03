# Thursday 04 January 2024 11:53:49 PM IST
# Friday 05 January 2024 12:10:43 AM IST -- done with preety printing

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

