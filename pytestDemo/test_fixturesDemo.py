import pytest

@pytest.mark.usefixtures("setup")

class notify:

    def test_greetme(self):
        print("i will be executing right after the before method")


    def test_executeme1(self):
        print("execute1")


    def test_executeme2(self):
        print("execute2")


    def test_executeme3(self):
        print("execute3")


    def test_executeme4(self):
        print("execute4")