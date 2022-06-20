#1.
print(sum(map(int, list(input("Enter a three-digit number: ")))))
#2.
x = float(input("Enter number#2: "))
print(float(x) - int(x))
y = int(x*10) % 10
print(y)
#3.
list_ten = [10, 20, 30, 40, 50]
list_ten.reverse()
print(list_ten)
#4.
list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
print(list(map(lambda t: t if t < 150 and t % 5 == 0 else None, list_of_six)))
#5.
import random
rnd = random.randint(1, 10)
count = 0
while True:
    number = int(input("Enter number 1 - 10: "))
    if number == rnd:
        print("You won!")
        break
    else:
        print("You lose")
        print("You have", 2 - count, "attempts left")
        count += 1
        if count > 2:
            break
#6.
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
#7.
n = int(input("Enter number: "))
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print("factorial: ", factorial)