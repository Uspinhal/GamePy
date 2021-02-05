from random import randint


class Calcular:
    __simbolo: dict = {1: '+', 2: '-', 3: '*'}
    
    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1: somar; 2: subtrair, 3: multiplicar
        self.__resultado: int = self._gerar_resultado
    
    @property
    def dificuldade(self) -> int:
        return self.__dificuldade
    
    @property
    def valor1(self) -> int:
        return self.__valor1
    
    @property
    def valor2(self) -> int:
        return self.__valor2
    
    @property
    def operacao(self) -> int:
        return self.__operacao
    
    @property
    def resultado(self) -> int:
        return self.__resultado
    
    @property
    def simbolo(self) -> dict:
        return Calcular.__simbolo
    
    @property
    def _gerar_valor(self) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)
    
    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2
    
    def checar_resultado(self, resposta: int) -> bool:
        certo: bool = False
        
        if self.resultado == resposta:
            print('CERTA A RESPOSTA!!!!')
            certo = True
        else:
            print('ERROU!!!!')
        
        print(f'{self.valor1} {self.simbolo[self.operacao]} {self.valor2} = {self.resultado}')
        return certo
    
    def mostrar_operacao(self) -> None:
        print(f'{self.valor1} {self.simbolo[self.operacao]} {self.valor2} = ?')
    
    def __str__(self):
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        
        return f'Valor1: {self.valor1}\nValor2: {self.valor2}\nDificuldade: {self.dificuldade}\nOperação: {op}'
