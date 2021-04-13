7. Eliminate global variables with main functions.
What does this print?
```python
def myFunc4 (one, two, three): #(2,3,1)
    sum = (one + two) – three #(2 + 3) - 1
    return sum
def main ():
    one = 1
    two = 2
    three =3
    result = myFunc4 (two, three, one) #(2,3,1)
    print (result)
main ()
```
```
Output:
4
```



