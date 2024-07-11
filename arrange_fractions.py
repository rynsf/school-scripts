import lcm

def printArangedFrac(fractions, sign):
    lines = ["", "", ""]
    for f in fractions:
        lines[0] += f"{f[0]} " #todo pretty print
    lines[1] = (f"_ {sign}"*len(fractions))[:-1]
    for f in fractions:
        lines[2] += f"{f[1]} "
    
    for l in lines:
        print(l)

def ppArangedFraction(fractions):
    l = lcm.prettyPrintLcm([n[1] for n in fractions])
    fracSameDenom = []
    for f in fractions:
        mul = l // f[1]
        newFrac = [f[0]*mul, f[1]*mul]
        fracSameDenom.append([newFrac, f])
        print(f"{f[0]}   {mul}   {newFrac[0]}")
        print(f"{'_'*len(str(f[0]))} x {'_'*len(str(mul))} =")
        print(f"{f[1]}   {mul}   {newFrac[1]}")
        print()

    sortedFrac = sorted(fracSameDenom, key=lambda x: x[0][0])
    printArangedFrac([n[0] for n in sortedFrac], '<')
    print()
    printArangedFrac([n[1] for n in sortedFrac], '<')


print("Enter fractions, or return to sort")
fractions = []
i = input("Enter fraction(in the form N/D): ")
while i:
    fraction = [int(n) for n in i.split('/')] #todo error handling
    fractions.append(fraction)
    i = input("Enter fraction(in the form N/D): ")

if fractions:
    ppArangedFraction(fractions)
