import submit

def test_submit():
    # check that user cannot submit an invalid filetype (jpg)
    submitted = submit.submit_fail("Project Two", "jpg")
    assert submitted == False
