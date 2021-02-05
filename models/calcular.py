from random import randint


class Calcular:
    
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
    def _gerar_valor(self) -> int:
        pass
    
    @property
    def _gerar_resultado(self) -> int:
        pass
    
    def checar_resultado(self) -> bool:
        pass
    
    def mostrar_operacao(self) -> None:
        pass
    
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
