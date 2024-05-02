#Pytest framework is helpfull in running Test Cases from all files
#Pytest files and methods should always be name as test_
#All methods defined under pytest files are called Test Cases
#By using Pytest we can able to run all Smoke, BVT and Regression Test Cases defined under pytest files
#commands to run from pytest are py.test is used to run all Test Cases from all files
#py.test -v -s command is used to run all test cases and print the logs as shown in output
#py.test -k, py.test -m stands for mark
#py.test -m bvt/smoke/regression

import pytest


# @pytest.mark.smoke
def test_greet():
    print("Good Morning")

def test_verify():
    a=10
    b=20
    c=60
    assert a+b>c,"Test Failed"

