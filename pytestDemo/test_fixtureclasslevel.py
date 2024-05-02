import pytest


@pytest.mark.usefixtures("newsetup")
class testingfixture:

    def test_greetme(self):
        print("i will be executing right after the before method")

    def test_1(self):
        print("execute1")

    def test_2(self):
        print("execute2")

    def test_3(self):
        print("execute3")

    def test_4(self):
        print("execute4")