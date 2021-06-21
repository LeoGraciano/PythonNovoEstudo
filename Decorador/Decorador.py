from time import time, sleep


def velocidade(fun):
    def slave(*args, **kwargs):
        start = time()
        resultado = fun(*args, **kwargs)
        end = time()
        tempo = end - start
        print(f'\nA função {fun.__name__}'
              f'levou {tempo:.2f}s para executar'
              )
        return resultado
    return slave


@velocidade
def teste_velocidade():
    for _ in range(500000):
        print(_)


if __name__ == '__main__':
    teste_velocidade()
