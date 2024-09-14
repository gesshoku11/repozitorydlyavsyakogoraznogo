# GUI - Graphical User Interface
# CUI - Console User Interface

# input() - ввод одной строки от пользователя

name = input('как тебя зовут?:\n')
age = input('сколько тебе лет?\n')
print('Привет', name)
print('Тебе', age, 'лет')
# рефакторинг

# int(), str(), float(), bool

print(int(input())+int(input()))

# 0 - False, все остальное - true
print(bool(0))
print(bool(1))

print(bool('asdfasf'))
print(bool())

# тернарный оператор
color = input('input the color:\n')
if color == 'red':
    print('Stop')
elif color == 'yellow':
    print('Wait')
elif color == 'green':
    print('Go')
