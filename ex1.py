lista = ['Homem de ferro' , 'Capitão America', 'Thor', 'Hulk', 'Viuva Negra','Gavião Arqueiro']

lista.append('Homem Aranha')

print(f'A posição de Thor é {lista.index('Thor')}')

lista.pop(0)
lista.pop(4)

print(lista)