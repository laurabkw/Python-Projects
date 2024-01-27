times=['América-MG','São Paulo','Ceará','Chapecoense','Flamengo','Corinthians','Palmeiras','Botafogo','Cuiabá','Fluminense','Atlético-GO','Fortaleza','Internacional','Avaí','Ceará','Goiás','Juventude','Bahia','Cruzeiro','Vasco']

#letra a
print('Cinco primeiros colocados: ')
print('1º {}\n2º {}\n3º {}\n4º {}\n5º {}'.format(times[0],times[1],times[2],times[3],times[4]))
#letra b
print('Quatro últimos colocados: ')
print('17º {}\n18º {}\n19º {}\n20º {}'.format(times[16],times[17],times[18],times[19]))
#letra c
print('Times do Brasileirão em ordem alfabética: ')
print(sorted(times))
#letra d
print('O time Chapecoense aparece na {}ª posição.'.format(times.index('Chapecoense')))