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
  