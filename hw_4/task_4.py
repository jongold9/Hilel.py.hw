n = int(input("Enter number:"))
if int(n) > 9:
    print("this number > 9")
else:
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(k, end="")
        print()
