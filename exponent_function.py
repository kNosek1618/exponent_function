
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 4))

print("")

def speed(acceleration, iteration):
    result = 1
    for sec in range(iteration):
        result = result * acceleration
    return result

print(speed(2, 3))


