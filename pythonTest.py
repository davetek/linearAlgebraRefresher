from decimal import getcontext, Decimal, ROUND_UP

getcontext().prec = 20

rawResult = (Decimal(10478) / Decimal(3))
roundedResult = round((Decimal(10478) / Decimal(3)), 3)
print('raw result: ' + str(rawResult))
print('rounded result: ' + str(roundedResult))

decNum = (Decimal(0.825))
decNum = round(decNum,2)
print('Decimal #: ' + str(decNum))

x = Decimal(16.0/7)
print(str(x))

output = round(x,2)
print(output)

z = Decimal(7.82369784)
print(z)

zplus = z.quantize(Decimal('0.001'), rounding=ROUND_UP)
print(zplus)

v = Decimal('1.0826146331693060657')
b = Decimal('2.6717616886457058218')

v = v.quantize(Decimal('.001'), rounding=ROUND_UP)
print(v)

product = [v, b]
product = [coordinate.quantize(Decimal('.001'), rounding=ROUND_UP) for coordinate in product]
print(product)
