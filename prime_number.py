def prime(y):
    x = [2,3,5,7]
    s = []
    for num in x:
        if not y % num:
            s.append("notprime")

    if "notprime" in s:
        print(f"{y} is not a Prime Number")
    else:
        print(f"{y} is a Prime Number")

y = int(input("Enter the Number: "))
prime(y)
