import datetime

import pytest


# @pytest.mark.bvt
def test_firstname():
    name ="shirish meduri"
    assert "shirish" in name,"Test Passed"

def test_calcualteAge():
    DOB='25/05/1991'
    birthyear=DOB.split("/")
    currentyear=datetime.MINYEAR
    print(currentyear)
    Actualage=int(currentyear)-int(birthyear[2])
    assert Actualage>35,"Candidate is not eligible for UPSC exams"