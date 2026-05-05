table = [60,61,62,63,64,65,66,67,68,69,97,42,93,529,420,7541]
print('Decimal  Hex  Symbol  Bin  ')
for i in range(0,(len(table))):
    print(table[i],'    ',hex(table[i]),'   ',chr(table[i]),'  ',bin(table[i]))
    'print(table[i],'    ',hex(table[i]),'   ',chr(hex(table[i])),'  ',bin(table[i]))'