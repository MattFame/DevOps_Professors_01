# this code prints fibonacci numbers from 1 to given number limit
limit = 55
num1 = 1
num2 = 2
count = 0

# while num1 < limit:
while num1 <= limit:
    print(num1)
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    count += 1
    # print(num1)
