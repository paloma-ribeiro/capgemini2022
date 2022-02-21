from questao_01 import create_stair
from questao_02 import validate_password
from questao_03 import anagram

if __name__ == '__main__':
    result: str = create_stair(n=6)
    print(result)

    result: int = validate_password(password='Ya3')
    print(result)

    result = anagram("ifailuhkqq")
    print(result)
