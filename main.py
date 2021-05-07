from carro import Carro
from os import system

system('cls')

carro1 = Carro('BMW', 'BMW Série 1', 'Azul', 0, 0)
carro1.ColocarCombustível(10)
carro1.LigarCarro()
carro1.DesligarCarro()
carro1.DesligarCarro()

print()

carro1.ObterInfo()

carro2 = Carro('Chevrolet', 'Camaro', 'Cinza', 0, 0)
carro2.ColocarCombustível(100)
carro2.LigarCarro()
for c in range(0, 110):
    carro2.ColocarCarroPraAndar()

carro2.LigarCarro()
carro2.ColocarCombustível(100)
carro2.LigarCarro()
print()

carro2.ObterInfo()