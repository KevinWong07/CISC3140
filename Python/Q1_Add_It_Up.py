n = int(input("Enter number: "))
def add_it_up(n):
    if type(n) == int:
        result = sum(range(0, n + 1))
        return result
    else:
        return 0
print(add_it_up(n))