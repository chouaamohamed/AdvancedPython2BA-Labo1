import pytest
import utils

def test_fact():
    # À compléter...
    assert utils.fact(3) == 6

    with pytest.raises(ValueError) as message:
        utils.fact(-1)
    assert str(message.value) == "Le nombre ne peut pas être négatif."

def test_roots():
    # À compléter...
    assert utils.roots(2, 3, 1) == (-0.5, -1)

    with pytest.raises(ValueError) as message:
        utils.roots(1, 1, 5)
    assert str(message.value) == "Le delta n'admet aucune solution."

def test_integrate():
    # À compléter...
    assert utils.integrate("x", 0, 1) == 0.5

    with pytest.raises(ValueError) as message:
        utils.integrate("x", 1, 0)
    assert str(message.value) == "La borne du dessous doit être égale ou plus petite que la borne du dessus."
