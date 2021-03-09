revenue = float(input('Выручка: '))
costs = float(input('Издержки: '))

result = revenue - costs

if result > 0:
    print('Компания работает с прибылью: ', result)
    print('Рентабельность: ', result / revenue)
    people = int(input('Численность сотрудников: '))
    print(f'Прибыль на одного сотрудника: {result / people:.2f}')
elif result < 0:
    print('Компания работает с убытком: ', result)
else:
    print('Компания работает в 0')