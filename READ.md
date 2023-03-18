### The python team work on a program that has to do with variables, functions, iteration, and strigs. some of these functions include: def,  for, return, and etc. we also study about operators, which include: =, +, *, <, >, /, and etc.we wrote a program that reads and check in numbers and print the largest value of the number. we also work on a program that repeatedly reads numbers, and print out the total, count, and the average of the numbers. 


```pythons
def read(numbers):
    numbers = [ 15', '25', '45', '65', '75', '95]
for numbers in numbers:
    print('odd numbers:', numbers)
print('Done!')

total = 0
for itervar in [15, 25, 45, 65, 75, 95]:
    total = total + itervar
print('total: ', total)

count = 0
for itervar in [15, 25, 45, 65, 75, 95]:
    count = count + 1
print('Count: ', count)

average = 0
for itervar in [15, 25, 45, 65, 75, 95]:
    average = average + 1
print('average: ', average)


```python
def max(values):
    largest = None
    for value in values:
        if largest is None or value < largest:
            largest = value
    return largest

    largest = None
print('Before:', largest)
for itervar in [2, 3, 41, 12,90, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print('Print from small to large number:', itervar, largest)
print('Bigger:', largest)
```
