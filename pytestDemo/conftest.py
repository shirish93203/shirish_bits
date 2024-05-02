import pytest


@pytest.fixture(autouse=True)
def setup():
    print("i will be executing first")
    yield
    print("I will be executing right after test_greetme")

@pytest.fixture(autouse=True)
def newsetup():
    print("i will be executing first")
    yield
    print("I will be executing right after test_greetme")