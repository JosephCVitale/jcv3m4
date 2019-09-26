from database import USER1
import grade

def test_grade():
    #check if instructor successfully updates student's grade
    score = 100
    grade.grade_fail(score)
    assert USER1["grade"] == score
