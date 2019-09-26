import add_TA

def test_add_TA():
    correctString = "name added to course"
    resultString = add_TA.add_TA_pass("name", "course")
    assert correctString == resultString
