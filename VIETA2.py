import math
while True:
    print('Write the a, b and c of any quadratic equation you want: ')
    a = int(input('a = ' ))
    b = int(input('b = ' ))
    c = int(input('c = ' ))
    print('Your equation is:', a,'* x^2 + (',b,'* x) + (',c,') = 0')

    d = int(((b ** 2) - (4 * a * c)))

    if d > 0:
        print(f'The two solutions x1, x2 are: x1 = {(- b + math.sqrt(d))/(2*a)}', f' and x2 ={(- b - math.sqrt(d))/(2*a)}')
    elif d < 0:
        print('This equation has no real solutions.')
    else:
        print(f'This equation has one double solution, x ={(- b )/ (2 *a)}')
