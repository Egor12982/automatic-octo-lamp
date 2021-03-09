user = int(input('Enter int: '))
current_max = 0
num = user

while num > 0:
    digit = num % 10
    if digit > current_max:
        current_max = digit
        if current_max == 9:
            break
    num = num // 10

print(f'Наибольшая цифра {user}: ', current_max)