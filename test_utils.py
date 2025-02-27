import pytest
import utils

def test_fact():
    # À compléter...
    assert utils.fact(3) == 6

def test_roots():
    # À compléter...
    assert utils.roots(2, 3, 1) == (-0.5, -1)

def test_integrate():
    # À compléter...
    assert utils.integrate("x", 0, 1) == 0.5
