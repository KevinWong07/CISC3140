import operator

p = [False, False, True, True]
q = [False, True, False, True]

negate_p = list(map(operator.not_,p))

# ~p v q
exp1 = list(map(operator.or_, negate_p, q))

# p -> q
exp2 = [True, True, False, True]

print(p)
print(q)
print(exp1)
print(exp2)

if exp1 == exp2:
    print('Expressions are equal')
else:
    print('Expressions are not equal')
