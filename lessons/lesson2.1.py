i = 0
while True:
    if i == 100:
        break
        print(i)
    i += 1
    print(i)
for i in range(124125, 523857238572389, 414):
    if i % 17 == 0:
        print(f'{i} - красное число')
        break
    if i % 14 == 0:
         print(f'{i} -  синее число')
         break
else:
    print('Все числа черные!') # Сработает если не было break






