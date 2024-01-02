# time for addition test

from random import randint

marks = 0
no_of_questions = 10

for i in range(no_of_questions):
    print(f"Question! - {i+1}/{no_of_questions}\n")
    n = randint(0, 9999)
    m = randint(0, 9999)
    print(f" {n:04d}")
    print(f"+{m:04d}")
    print("_____")
    a = input("" if len(str(n+m)) > 4 else " ")
    while not a.isdigit():
        a = input("" if len(str(n+m)) > 4 else " ")
    a = int(a) 

    if a == n+m:
        print("✅ Right Answer\n")
        marks += 1
    else:
        print("❎ Wrong answer\n")

print(f"Your marks: {marks}/{no_of_questions}")
