# Escreva um algoritmo que mostre na tela uma escada de tamanho n
# utilizando o caractere * e espaços. A base e altura da escada devem
# ser iguais ao valor de n. A última linha não deve conter nenhum espaço.

def stair_step(current_step: int, stair_size: int) -> str:
    """
    Create a stair step
    :param current_step: >= 1 and <= stair_size
    :param stair_size:
    :return: str
    """
    if current_step < 1:
        raise ValueError('current_step is less than one')
    if current_step > stair_size:
        raise ValueError('current_step is bigger than stair_size')

    text = ''
    for index in range(0, stair_size - current_step):
        text += ' '
    for index in range(0, current_step):
        text += '*'
    return text + '\n'


def create_stair(n: int) -> str:
    """
    Create a stair
    :param n:
    :return: str
    """
    stair_text = ''
    for index in range(1, n + 1):
        stair_text += stair_step(current_step=index, stair_size=n)
    return stair_text
