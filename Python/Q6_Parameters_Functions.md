6. The parameters in a function’s parameter list match up with and get their values from the arguments in the argument list of a function call in numerical order, not by parameter/argument name.
What does this print?

```python
def myFunc2 (one, two, three):
    print (one, two, three)

one = 1
two = 2
three = 3

print (one, two, three)
myFunc2 (two, three, one)
print (one, two, three)
```
```
Output:
1 2 3
2 3 1
1 2 3
```