from random import randint

n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valores sorteados foram: ',end='')
for num in n:
    print('{}'.format(num),end=' ')
print('\nO maior valor sorteado foi: {}'.format(max(n)))
print('O menor valor sorteado foi: {}'.format(min(n)))