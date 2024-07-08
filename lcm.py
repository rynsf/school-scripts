from preetyprint import leftpad
import sys

def isDivisible(a, b):
    if a%b == 0:
        return True
    return False

def divideAllBy(nums, n):
    result = []
    for i in nums:
        if isDivisible(i, n):
            result.append(i//n)
        else:
            result.append(i)
    return result

def smallestPrimeFactor(nums):
    till = max(nums)
    for n in range(2, till+1):
        for m in nums:
            if isDivisible(m, n):
                return n

def lcm(nums):
    if [n for n in nums if n<=0]:
        print("Only LCM of positive integers allowed")
        sys.exit(-1)
    till = max(nums)
    results = []
    while till > 1:
        n = smallestPrimeFactor(nums)
        results.append([n, nums])
        nums = divideAllBy(nums, n)
        till = max(nums)
    return results

def prettyPrintLcm(nums):
    results = lcm(nums)
    factorLength = len(str(max([n[0] for n in results]))) + 1
    for line in results:
        lineToPrint = ''
        lineToPrint += leftpad(factorLength, str(line[0])) + '|'
        for n in line[1]:
            lineToPrint += f"{n}, "
        print(lineToPrint)
        seprator = ''
        seprator += '_' * factorLength + '|'
        seprator += '_' * (len(lineToPrint) - factorLength)
        print(seprator)
    print(' '*factorLength + '|' + "1, " * len(results[0][1]))
    mul = 1
    mulToPrint = '=> '
    for n in results:
        mulToPrint += f"{n[0]} * "
        mul *= n[0]
    mulToPrint = mulToPrint[:-2] #remove trailing multiply
    print()
    print(mulToPrint, '=', mul)


if __name__ == "__main__":
    nums = []
    i = input('Enter a number(or return to find lcm): ')
    while i:
        nums.append(int(i))
        i = input('Enter a number(or return to find lcm): ')

    if nums:
        prettyPrintLcm(nums)






