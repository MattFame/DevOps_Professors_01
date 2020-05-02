num = int(input('Enter the end number: '))

prime_list = []
for number in range(2, num+1):
    is_number = True
    for interval_num in range(2, number):
        if number % interval_num == 0:
            is_number = False
            break

    if is_number:
        prime_list.append(number)
print(prime_list)
