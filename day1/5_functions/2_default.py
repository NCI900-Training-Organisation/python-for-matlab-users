
def calc_discount(base_value, discount = .05):
    return base_value - (base_value * discount)

val = calc_discount(100)
print('Discounted = ', val)

val = calc_discount(100, .10)
print('Discounted = ', val)