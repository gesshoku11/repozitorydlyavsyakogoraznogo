# DRY = Don't Repeat Yourself
name = 'Ilya'
print('Привет', name)
print(f'Привет {42*2}')
pi = 3.14159
e = 2.718281828459045
print(f'{pi}')
print(f'{pi:.2f}')
print(f'{pi:.1f}')
# loop
print('Hello world')
for elem in 1, 2, 3: # Заголовок цикла
    print(elem)
for elem in '1, 2, 3': # Заголовок цикла
    print(elem)
# range  - диапазон
# range (end) - генерирует числа от 0 до end (не включительно)
print(*range(5))
print(*range(10))
print(*range(43))
print(*range(11))
# range (start, end) - генерирует числа от start до emd (не включительно)
print(*range(1, 11))
# range (start, end, step) - генерирует числа от start до end (не включительно) с шагом step
print(*range(10, 100))
print(*range(10, 100, 1))
print(*range(10, 100, 2))
# * - операция распоковки

for i in range(10, -1, -2):
    print(i)
print('поехали')

num = int(input())
while num != 0:
    print(f'{num} - хорошее число!')
    num = int(input())