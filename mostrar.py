n = int(input("Digite a quantidade de numeros sa serem adicionados: "))

#foma compacta de adicionar numeros
lista = [int(input(f"Digite o {i}º numero:")) for i in range(1,n+1)]


print(lista)

