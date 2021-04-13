5. A variable defined inside a function is a local variable; otherwise, it is a global variable.  
If a local variable has the same name as a global variable, the local variable is used inside the function.  
What does this print?  

```python
def myFunc1 ():
    one = -1
    print (one, two)

one = 1
two = 2

print (one, two)
myFunc1 ()
print (one two)
```
```
Output:  
1 2  
-1 2  
1 2
```