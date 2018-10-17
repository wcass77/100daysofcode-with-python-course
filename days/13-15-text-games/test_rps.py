import random
import pytest

from rps import Roll, ROLLS


@pytest.fixture
def set_seed():
    random.seed(0)


def test_roll(set_seed):
    roll0 = Roll(ROLLS[0])
    roll_rand1 = Roll()
    roll_rand2 = Roll("random")
    with pytest.raises(Exception) as e:
        roll_invalid = Roll("Nosense")

    assert roll0.name == ROLLS[0]
    assert roll_rand1.name == ROLLS[1]
    assert roll_rand2.name == ROLLS[1]
    assert "Invalid role" in str(e)

