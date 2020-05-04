range_input = int(input("Please give your range to create fibonacci series: "))
fib_num = [1, 1]
new_fib = 0
for i in range(1, range_input):
    new_fib = fib_num[i] + fib_num[i-1]
    fib_num.append (new_fib)
print(fib_num)