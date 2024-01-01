# script to print out the answer of a long division

num1 = int(input("Enter Divisor: "))
num2 = input("Enter Divident: ")
now_div = ""
print(" "*len(str(num1)) + "┌" + "─"*len(num2) + "┐")
print(f"{num1}│{num2}│{int(num2) // int(num1)}")
space_count = len(str(num1)) + 1
first = True

for n in num2:
    now_div += n
    int_div = int(now_div)
    if first:
        if int_div < num1:
            continue
        first = False
    else:
        print(f"{n}")

    remainder = int_div % num1
    minus = int_div - remainder
    print(" "*(space_count-1)+ "-" + " "*(len(now_div) - len(str(minus))) + f"{minus}")
    print(" "*(space_count-1) + "─"*(len(now_div)+2))
    space_count += len(now_div) - len(str(remainder))
    print(" "*(space_count) + f"{remainder}", end = "")
    now_div = str(remainder)

print("")
