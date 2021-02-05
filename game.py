from models.calcular import Calcular


def main():
    pontos: int = 0
    jogar(pontos)
    
    
def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado (1, 2, 3 ou 4):'))
    
    calc: Calcular = Calcular(dificuldade)
    
    print('Qual a resposta para a operação abaixo:')
    calc.mostrar_operacao()
    resultado: int = int(input())
    
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s)')
        
    continuar: str = input('Deseja continuar? [S - sim, N - não]').upper()
    
    if continuar == 'S':
        jogar(pontos)
    elif continuar == 'N':
        print(f'Você conseguiu {pontos} pontos')
        print('Até a próxima!')
        

if __name__ == '__main__':
    main()
