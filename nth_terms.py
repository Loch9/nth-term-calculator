def nth_terms():
    sequence = input('Enter your sequence, with numbers seperated by a space (up to quintic sequence): \n')
    
    numbers = []

    numbers = sequence.split()
    numbers = [int(i) for i in numbers]

    first_difference = []
    second_difference = []
    third_difference = []
    forth_difference = []
    fifth_difference = []
    sixth_difference = []

    i = len(numbers)
    for x in range(0, i - 1):
        if x != i:
            first_difference.append(numbers[x + 1] - numbers[x])

    if len(set(first_difference)) == 1:
        print(linear_sequence(first_difference, numbers))
        return

    i = len(first_difference)
    for x in range(0, i - 1):
        if x != i:
            second_difference.append(first_difference[x + 1] - first_difference[x])

    if len(set(second_difference)) == 1:
        print(quadratic_sequence(second_difference, numbers))
        return

    i = len(second_difference)
    for x in range(0, i - 1):
        if x != i:
            third_difference.append(second_difference[x + 1] - second_difference[x])

    if len(set(third_difference)) == 1:
        print(cubic_sequence(third_difference, numbers))
        return

    i = len(third_difference)
    for x in range(0, i - 1):
        if x != i:
            forth_difference.append(third_difference[x + 1] - third_difference[x])

    if len(set(forth_difference)) == 1:
        print(quartic_sequence(forth_difference, numbers))
        return

    i = len(forth_difference)
    for x in range(0, i - 1):
        if x != i:
            fifth_difference.append(forth_difference[x + 1] - forth_difference[x])

    if len(set(fifth_difference)) == 1:
        print(quintic_sequence(fifth_difference, numbers))
        return

    i = len(fifth_difference)
    for x in range(0, i - 1):
        if x != i:
            sixth_difference.append(fifth_difference[x + 1] - fifth_difference[x])

    if len(set(sixth_difference)) == 1:
        print(sextic_sequence(sixth_difference, numbers))
        return

def linear_sequence(fd, s):
    difference = []
    sequence = []
    sequence = s
    difference = fd

    b = 0

    arithmetic_sequence = []

    for x in range(0, len(sequence)):
        arithmetic_sequence.append(difference[0]*(x+1))

    if sequence[0] - arithmetic_sequence[0] == 0:
        b = 0
    else:
        b = sequence[0] - arithmetic_sequence[0]

    a = difference[0]

    if a == 0 and b == 0:
        return ''
    elif a == 0 and b > 0:
        return str(b)
    elif a == 0 and b < 0:
        return '- ' + str(abs(b))
    elif b == 0:
        return str(a) + 'n'
    elif b > 0:
        return str(a) + 'n + ' + str(b)
    elif b < 0:
        return str(a) + 'n - ' + str(abs(b))

def quadratic_sequence(sd, s):
    second_difference = []
    sequence = []
    sequence = s
    second_difference = sd

    i = len(sequence)
    n = []
    for x in range(0, i - 1):
        if second_difference[0] * (x + 1) == sequence[x]:
            n.append(1)

    a = second_difference[0] / 2

    first_difference = []
    arithmetic_sequence = []

    for x in range(0, len(sequence)):
        first_difference.append(sequence[x] - a*((x+1)**2))

    for x in range(0, len(first_difference) - 1):
        if x != len(first_difference):
            arithmetic_sequence.append(first_difference[x + 1] - first_difference[x])

    linear = linear_sequence(arithmetic_sequence, first_difference)

    if a == 1 and linear == '':
        return 'n^2'
    elif a == 1 and list(linear)[0] == '-':
        return 'n^2 ' + linear
    elif a == 1:
        return 'n^2 + ' + linear
    elif linear == '':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^2'
        else:
            return str(a) + 'n^2'
    elif list(linear)[0] == '-':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^2 + ' + linear 
        else:
            return str(a) + 'n^2 + ' + linear
    else:
        if a < 0:
            return '- ' + str(abs(a)) + 'n^2 + ' + linear
        else:
            return str(a) + 'n^2 + ' + linear 

def cubic_sequence(td, s):
    third_difference = []
    sequence = []
    third_difference = td
    sequence = s

    a = third_difference[0] / 6

    quadratic_sequence_v = []

    for x in range(0, len(sequence)):
        quadratic_sequence_v.append(sequence[x] - a*((x+1)**3))

    first_difference = []
    second_difference = []

    i = len(quadratic_sequence_v)
    for x in range(0, i - 1):
        if x != i:
            first_difference.append(quadratic_sequence_v[x + 1] - quadratic_sequence_v[x])

    i = len(first_difference)
    for x in range(0, i - 1):
        if x != i:
            second_difference.append(first_difference[x + 1] - first_difference[x])

    quadratic = quadratic_sequence(second_difference, quadratic_sequence_v)

    if a == 1 and quadratic == '':
        return 'n^3'
    elif a == 1 and list(quadratic)[0] == '-':
        return 'n^3 ' + quadratic
    elif a == 1:
        return 'n^3'
    elif quadratic == '':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^3'
        else:
            return str(a) + 'n^3'
    elif list(quadratic)[0] == '-':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^3 ' + quadratic
        else:
            return str(a) + 'n^3 ' + quadratic
    else:
        if a < 0:
            return '- ' + str(abs(a)) + 'n^3 + ' + quadratic
        else:
            return str(a) + 'n^3 + ' + quadratic

    
def quartic_sequence(fdf, s):
    forth_difference = []
    sequence = []
    forth_difference = fdf
    sequence = s

    a = forth_difference[0] / 24

    cubic_sequence_v = []

    for x in range(0, len(sequence)):
        cubic_sequence_v.append(sequence[x] - (a*((x+1)**4)))

    third_difference = []
    third_difference_first = []
    third_difference_second = []

    for x in range(0, len(cubic_sequence_v) - 1):
        if x != len(cubic_sequence_v):
            third_difference.append(cubic_sequence_v[x + 1] - cubic_sequence_v[x])

    for x in range(0, len(third_difference) - 1):
        if x != len(third_difference):
            third_difference_first.append(third_difference[x + 1] - third_difference[x])

    for x in range(0, len(third_difference_first) - 1):
        if x != len(third_difference_first):
            third_difference_second.append(third_difference_first[x + 1] - third_difference_first[x])

    cubic = cubic_sequence(third_difference_second, cubic_sequence_v)

    if a == 1 and cubic == '':
        return 'n^4'
    elif a == 1 and list(cubic)[0] == '-':
        return 'n^4 ' + cubic
    elif a == 1:
        return 'n^4'
    elif cubic == '':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^4'
        else:
            return str(a) + 'n^4'
    elif list(cubic)[0] == '-':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^4 ' + cubic
        else:
            return str(a) + 'n^4 ' + cubic
    else:
        if a < 0:
            return '- ' + str(abs(a)) + 'n^4 + ' + cubic
        else:
            return str(a) + 'n^4 + ' + cubic


def quintic_sequence(fdff, s):
    fifth_difference = []
    sequence = []
    fifth_difference = fdff
    sequence = s

    a = fifth_difference[0] / 120

    quartic_sequence_v = []

    for x in range(0, len(sequence) - 1):
        quartic_sequence_v.append(sequence[x] - (a*((x+1)**5)))

    forth_difference = []
    forth_difference_first = []
    forth_difference_second = []
    forth_difference_third = []

    for x in range(0, len(quartic_sequence_v) - 1):
        if x != len(quartic_sequence_v):
            forth_difference.append(quartic_sequence_v[x + 1] - quartic_sequence_v[x])

    for x in range(0, len(forth_difference) - 1):
        if x != len(forth_difference):
            forth_difference_first.append(forth_difference[x + 1] - forth_difference[x])

    for x in range(0, len(forth_difference_first) - 1):
        if x != len(forth_difference_first):
            forth_difference_second.append(forth_difference_first[x + 1] - forth_difference_first[x])

    for x in range(0, len(forth_difference_second) - 1):
        if x != len(forth_difference_second):
            forth_difference_third.append(forth_difference_second[x + 1] - forth_difference_second[x])


    quartic = quartic_sequence(forth_difference_third, quartic_sequence_v)

    if a == 1 and quartic == '':
        return 'n^5'
    elif a == 1 and list(quartic)[0] == '-':
        return 'n^5 ' + quartic
    elif a == 1:
        return 'n^5'
    elif quartic == '':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^5'
        else:
            return str(a) + 'n^5'
    elif list(quartic)[0] == '-':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^5 ' + quartic
        else:
            return str(a) + 'n^5 ' + quartic
    else:
        if a < 0:
            return '- ' + str(abs(a)) + 'n^5 + ' + quartic
        else:
            return str(a) + 'n^5 + ' + quartic


def sextic_sequence(sdf, s):
    sixth_difference = []
    sequence = []
    sixth_difference = sdf
    sequence = s

    a = sixth_difference[0] / 720

    quintic_sequence_v = []

    for x in range(0, len(sequence) - 1):
        quintic_sequence_v.append(sequence[x] - (a*((x+1)**6)))

    fifth_difference = []
    fifth_difference_first = []
    fifth_difference_second = []
    fifth_difference_third = []
    fifth_difference_forth = []

    for x in range(0, len(quintic_sequence_v) - 1):
        if x != len(quintic_sequence_v):
            fifth_difference.append(quintic_sequence_v[x + 1] - quintic_sequence_v[x])

    for x in range(0, len(fifth_difference) - 1):
        if x != len(fifth_difference):
            fifth_difference_first.append(fifth_difference[x + 1] - fifth_difference[x])

    for x in range(0, len(fifth_difference_first) - 1):
        if x != len(fifth_difference_first):
            fifth_difference_second.append(fifth_difference_first[x + 1] - fifth_difference_first[x])

    for x in range(0, len(fifth_difference_second) - 1):
        if x != len(fifth_difference_second):
            fifth_difference_third.append(fifth_difference_second[x + 1] - fifth_difference_second[x])

    for x in range(0, len(fifth_difference_third) - 1):
        if x != len(fifth_difference_third):
            fifth_difference_forth.append(fifth_difference_third[x + 1] - fifth_difference_third[x])

    quintic = quintic_sequence(fifth_difference_forth, quintic_sequence_v)

    if a == 1 and quintic == '':
        return 'n^6'
    elif a == 1 and list(quintic)[0] == '-':
        return 'n^6 ' + quintic
    elif a == 1:
        return 'n^6'
    elif quintic == '':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^6'
        else:
            return str(a) + 'n^6'
    elif list(quintic)[0] == '-':
        if a < 0:
            return '- ' + str(abs(a)) + 'n^6 ' + quintic
        else:
            return str(a) + 'n^6 ' + quintic
    else:
        if a < 0:
            return '- ' + str(abs(a)) + 'n^6 + ' + quintic
        else:
            return str(a) + 'n^6 + ' + quintic

    
def generate_sequence():
    type_of_sequence = input('What sequence is this (linear [l], quadratic [q], cubic [c], quartic [qu], quintic [qi], sextic [s]): ')
    if type_of_sequence.lower() == 'linear'.lower() or type_of_sequence.lower() == 'l'.lower():
        generate_linear()
    elif type_of_sequence.lower() == 'quadratic'.lower() or type_of_sequence.lower() == 'q'.lower():
        generate_quadratic()
    elif type_of_sequence.lower() == 'cubic'.lower() or type_of_sequence.lower() == 'c'.lower():
        generate_cubic()
    elif type_of_sequence.lower() == 'quartic'.lower() or type_of_sequence.lower() == 'qu'.lower():
        generate_quartic()
    elif type_of_sequence.lower() == 'quintic'.lower() or type_of_sequence.lower() == 'qi'.lower():
        generate_quintic()
    elif type_of_sequence.lower() == 'sextic'.lower() or type_of_sequence.lower() == 's'.lower():
        generate_sextic()

def generate_linear():
    print('Enter your linear equation: ')
    a = int(input('\033[1;31;40ma\033[1;37;40mx+b: '))
    b = int(input('ax+\033[1;31;40mb\033[1;37;40m: '))
    n = int(input('How many numbers of the sequence to generate: '))

    numbers = []
    snumbers = ''

    for x in range(1, n + 1):
        numbers.append((a*x)+b)
        snumbers = snumbers + str(numbers[x - 1]) + ' '

    print(snumbers)
    
def generate_quadratic():
    print('Enter your quadratic equation: ')
    a = int(input('\033[1;31;40ma\033[1;37;40mn^2+bn+c: '))
    b = int(input('an^2+\033[1;31;40mb\033[1;37;40mn+c: '))
    c = int(input('an^2+bn+\033[1;31;40mc\033[1;37;40m: '))
    n = int(input('How many numbers of the sequence to generate: '))

    numbers = []
    snumbers = ''

    for x in range(1, n + 1):
        numbers.append((a*(x**2)+(b*x)+c))
        snumbers = snumbers + str(numbers[x - 1]) + ' '

    print(snumbers)

def generate_cubic():
    print('Enter your cubic equation: ')
    a = int(input('\033[1;31;40ma\033[1;37;40mx^3+bx^2+cx+d: '))
    b = int(input('ax^3+\033[1;31;40mb\033[1;37;40mx^2+cx+d: '))
    c = int(input('ax^3+bx^2+\033[1;31;40mc\033[1;37;40mx+d: '))
    d = int(input('ax^3+bx^2+cx+\033[1;31;40md\033[1;37;40m: '))
    n = int(input('How many numbers of the sequence to generate: '))

    numbers = []
    snumbers = ''

    for x in range(1, n + 1):
        numbers.append((a*(x**3))+(b*(x**2))+(c*x)+d)
        snumbers = snumbers + str(numbers[x - 1]) + ' '

    print(snumbers)

def generate_quartic():
    print('Enter your quartic equation: ')
    a = int(input('\033[1;31;40ma\033[1;37;40mx^4+bx^3+cx^2+dx+e: '))
    b = int(input('ax^4+\033[1;31;40mb\033[1;37;40mx^3+cx^2+dx+e: '))
    c = int(input('ax^4+bx^3+\033[1;31;40mc\033[1;37;40mx^2+dx+e: '))
    d = int(input('ax^4+bx^3+cx^2+\033[1;31;40md\033[1;37;40mx+e: '))
    e = int(input('ax^4+bx^3+cx^2+dx+\033[1;31;40me\033[1;37;40m: '))
    n = int(input('How many numbers of the sequence to generate: '))

    numbers = []
    snumbers = ''

    for x in range(1, n + 1):
        numbers.append((a*(x**4))+(b*(x**3))+(c*(x**2))+(d*x)+e)
        snumbers = snumbers + str(numbers[x - 1]) + ' '

    print(snumbers)

def generate_quintic():
    print('Enter your quintic equation: ')
    a = int(input('\033[1;31;40ma\033[1;37;40mx^5+bx^4+cx^3+dx^2+ex+f: '))
    b = int(input('ax^5+\033[1;31;40mb\033[1;37;40mx^4+cx^3+dx^2+ex+f: '))
    c = int(input('ax^5+bx^4+\033[1;31;40mc\033[1;37;40mx^3+dx^2+ex+f: '))
    d = int(input('ax^5+bx^4+cx^3+\033[1;31;40md\033[1;37;40mx^2+ex+f: '))
    e = int(input('ax^5+bx^4+cx^3+dx^2+\033[1;31;40me\033[1;37;40mx+f: '))
    f = int(input('ax^5+bx^4+cx^3+dx^2+ex+\033[1;31;40mf\033[1;37;40m: '))
    n = int(input('How many numbers of the sequence to generate: '))

    numbers = []
    snumbers = ''

    for x in range(1, n + 1):
        numbers.append((a*(x**5)+(b*(x**4))+(c*(x**3))+(d*(x**2))+(e*x)+f))
        snumbers = snumbers + str(numbers[x - 1]) + ' '

    print(snumbers)

def generate_sextic():
    print('Enter your sextic equation: ')
    a = int(input('\033[1;31;40ma\033[1;37;40mx^6+bx^5+cx^4+dx^3+ex^2+fx+g: '))
    b = int(input('ax^6+\033[1;31;40mb\033[1;37;40mx^5+cx^4+dx^3+ex^2+fx+g: '))
    c = int(input('ax^6+bx^5+\033[1;31;40mc\033[1;37;40mx^4+dx^3+ex^2+fx+g: '))
    d = int(input('ax^6+bx^5+cx^4+\033[1;31;40md\033[1;37;40mx^3+ex^2+fx+g: '))
    e = int(input('ax^6+bx^5+cx^4+dx^3+\033[1;31;40me\033[1;37;40mx^2+fx+g: '))
    f = int(input('ax^6+bx^5+cx^4+dx^3+ex^2+\033[1;31;40mf\033[1;37;40mx+g: '))
    g = int(input('ax^6+bx^5+cx^4+dx^3+ex^2+fx+\033[1;31;40mg\033[1;37;40m: '))
    n = int(input('How many numbers of the sequence to generate: '))

    numbers = []
    snumbers = ''

    for x in range(1, n + 1):
        numbers.append((a*(x**6)+(b*(x**5))+(c*(x**4))+(d*(x**3))+(e*(x**2))+(f*x)+g))
        snumbers = snumbers + str(numbers[x - 1]) + ' '

    print(snumbers)

