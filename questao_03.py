# Duas palavras podem ser consideradas anagramas de si mesmas
# se as letras de uma palavra podem ser realocadas para formar a
# outra palavra. Dada uma string qualquer, desenvolva um algoritmo que
# encontre o número de pares de substrings que são anagramas.
# Exemplo:
# Exemplo 1)
# Entrada:
# ovo
# Saída:
# 2
# Explicação:
# A lista de todos os anagramas pares são: [o, o], [ov, vo] que estão nas
# posições [[0], [2]], [[0, 1], [1, 2]] respectivamente.

from itertools import groupby


def anagram(text: str) -> int:
    """
    Returns anagram pairs
    :param text:
    :return: anagram pairs
    """
    count = 0
    data = []
    for index in range(0, len(text)):
        for sub_index in range(index + 1, len(text) + 1):
            data.append(sorted(text[index: sub_index]))  # ordenar o texto para que possam ser agrupados como iguais

    data.sort()  # precisa ordenar para conseguir fazer os grupos
    for key, group in groupby(data):
        new_group = list(group)
        if len(new_group) >= 2:  # quando grupo maior que um quer dizer que tem pares de anagrama
            count += 1

    return count
