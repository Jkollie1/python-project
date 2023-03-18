fruit = 'cassava'
letter = fruit[0]
print(letter)

length = len(fruit)
last = [length-1]
print(last)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
        
fruit = 'cassava'
print(fruit[3:])
print(fruit[:3])


greeting = 'hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

world = 'cassava'
count = 0
for letter in world:
    if letter == 'a':
        count = count + 1
print(count)

word = 'cassava'
new_word = word.upper()
print(new_word)
