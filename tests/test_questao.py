import pytest

from questao_01 import stair_step, create_stair


def test_stair_step():
    expected_result = '   *\n'
    result = stair_step(current_step=1, stair_size=4)
    assert result == expected_result

    expected_result = '****\n'
    result = stair_step(current_step=4, stair_size=4)
    assert result == expected_result

    with pytest.raises(ValueError):
        stair_step(current_step=0, stair_size=4)

    with pytest.raises(ValueError):
        stair_step(current_step=5, stair_size=4)


def test_create_stair():
    expected_result = '   *\n  **\n ***\n****\n'
    result = create_stair(n=4)
    assert expected_result == result

    expected_result = ''
    result = create_stair(n=0)
    assert expected_result == result

    expected_result = '  *\n **\n***\n'
    result = create_stair(n=3)
    assert expected_result == result
