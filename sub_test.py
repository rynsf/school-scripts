# time for subtraction test

from random import randint

marks = 0
no_of_questions = 10

for i in range(no_of_questions):
    print(f"Question! - {i+1}/{no_of_questions}\n")
    n = randint(0, 9999)
    m = randint(0, n)
    print(f" {n:04d}")
    print(f"-{m:04d}")
    print("_____")
    a = input(" ")
    while not a.isdigit():
        a = input(" ")
    a = int(a)

    if a == n-m:
        print("✅ Right Answer\n")
        marks += 1
    else:
        print("❎ Wrong answer\n")

print(f"Your marks: {marks}/{no_of_questions}")
