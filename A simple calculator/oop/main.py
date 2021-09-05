from calculator import Calculator
from operation import operations

c = Calculator()

n1 = c.first()


operation = c.operation()
n2 = c.second()

calculation = operations[operation]


ans = c.calculation(n1, n2)
print(ans)

