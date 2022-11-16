def to_binary(typecv, number): #from dec to bin
    if typecv.lower() == 'b':
        raise Exception("Can't convert from binary to binary!")
    if typecv.lower() != 'd': # if type is currently hex, swap to decimal
        number = to_decimal(typecv, number)
    binform = []
    quotinent = number
    while quotinent > 0:
        remainder = quotinent % 2
        quotinent = int(quotinent / 2)
        binform.append(str(remainder))
    return ''.join(reversed(binform))


def to_decimal(typecv, number): #swap from bin/hex to decimal
    if typecv.lower() == 'b': #binary to dec
        bin_num = 0
        bpwr = 0 #current power 2
        for belm in reversed(list(str(number))):
            belm = int(belm)
            if belm == 1:
                bin_num += (2 ** bpwr)
            bpwr += 1
        return bin_num
    elif typecv.lower() == 'h': #hex to dec
        hexnum = 0
        pwr = 0 #current power of 16
        for item in reversed(list(str(number))):
            if item.upper() == 'A':
                hexnum += (10 * (16 ** pwr))
            elif item.upper() == 'B':
                hexnum += (11 * (16 ** pwr))
            elif item.upper() == 'C':
                hexnum += (12 ** (16 ** pwr))
            elif item.upper() == 'D':
                hexnum += (13 * (16 ** pwr))
            elif item.upper() == 'E':
                hexnum += (14 * (16 ** pwr))
            elif item.upper() == 'F':
                hexnum += (15 * (16 ** pwr))
            elif int(item) < 10:
                hexnum += (int(item) * (16 ** pwr))
            pwr += 1
        return hexnum


    else:
        raise Exception('Accepted Format: h for hex or b for binary .')


def to_hex(typecv, number):
    if typecv.lower() == 'h':
        raise Exception("Can't convert from hex to hex!")
    hexformat = []
    if typecv != 'd':
        number = to_decimal(typecv, number)
    quotinent = number
    for step in range(0, len(str(number))):

        if quotinent == 0:
            break
        remainder = str(quotinent % 16)
        quotinent = int(quotinent / 16)
        if remainder == '10':
            hexformat.append('A')
        elif remainder == '11':
            hexformat.append('B')
        elif remainder == '12':
            hexformat.append('C')
        elif remainder == '13':
            hexformat.append('D')
        elif remainder == '14':
            hexformat.append('E')
        elif remainder == '15':
            hexformat.append('F')
        else:
            hexformat.append(remainder)
        step += 1
    return ''.join(reversed(hexformat))