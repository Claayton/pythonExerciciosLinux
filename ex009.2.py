#Ex009.2
"""Write a program that reads any interger, and shows your multiplication table on the screen"""

number = int(input('Enter a number to see his multiplication table: '))
print('{:^12}'.format('TABUADA'))
print('{}'.format('-'*12))
print(f'{number} X  1 ={number * 1:>3}')
print(f'{number} X  2 ={number * 2:>3}')
print(f'{number} X  3 ={number * 3:>3}')
print(f'{number} X  4 ={number * 4:>3}')
print(f'{number} X  5 ={number * 5:>3}')
print(f'{number} X  6 ={number * 6:>3}')
print(f'{number} X  7 ={number * 7:>3}')
print(f'{number} X  8 ={number * 8:>3}')
print(f'{number} X  9 ={number * 9:>3}')
print(f'{number} X 10 ={number * 10:>3}')
print('{}'.format('_'*12))
