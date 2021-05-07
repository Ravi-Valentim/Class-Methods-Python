class Carro:

    def __init__(self, marca, modelo, cor, combustível, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustível = combustível
        self.velocidade = velocidade
    

    def LigarCarro(self):
        from time import sleep
        if (self.velocidade == 0):
            if (self.combustível > 0):
                self.velocidade = 300
                print(f'Ligando o {self.modelo}... ', end='', flush=True)
                sleep(1.5)
                print('Pronto, seu carro já está ligado!')
                return
            print(f'{self.modelo} está sem combustível!')
            return
        
        print(f'{self.modelo} já está ligado!')


    def DesligarCarro(self):
        from time import sleep
        if (self.velocidade > 0):
            if (self.combustível > 0):
                self.velocidade = 0
                print(f'Desligando o {self.modelo}... ', end='', flush=True)
                sleep(1.5)
                print('Pronto, seu carro já está desligado.')
                return
        
        print(f'O {self.modelo} já está desligado!')


    def ColocarCombustível(self, litros):
        if (self.combustível <= 5):
            if (litros < 0 or litros == 0):
                print(f'Não é possível colocar combustível!')
                return
            self.combustível = litros
            print(f'Você acabou de colocar {litros}L de gasolina no seu veículo!')
            return
        
        print(f'{self.modelo} já tem combustível!')
    

    def ColocarCarroPraAndar(self):
        if (self.combustível > 5):
            print('Estamos em movimento uuuuh!')
            self.combustível -= 20
            if (self.combustível == 0):
                self.velocidade = 0
        
    def ObterInfo(self):
        print(f'''Informações do veículo:
        >>>>> Marca: {self.marca}
        >>>>> Modelo: {self.modelo}
        >>>>> Cor: {self.cor}
        >>>>> Velocidade: {self.velocidade}''')
