'''
    ========================================
This package contains some usful tools in daily work
The version is 1.0
'''

def echo(line,reflect=False):
    if reflect==True:
        idx = []
        i = len(line)
        for e in range(i):
            if line[e] == " ":
                continue
            idx.append(line[e:i])
        return '\n'.join(idx)
    elif reflect==False:
        return line
    else:
        raise RuntimeError("'reflect' must be bool type")

def to_decimal(number, fom):        #<-- is "from"
    result = 0
    x = 0
    while number:
        result += number%10*(fom**x)
        number = number//10
        x += 1
    return result

def from_decimal(number, tobe):
    result = 0
    x = 0
    while number:
        x += (number%tobe) * (10**i)
        number = number//tobe
        i += 1
    return x

def mean(*numbers):
    result = 0
    for x in numbers:
        result += x
    return result/len(numbers)
