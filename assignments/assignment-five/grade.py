from database import USER1

#successfully updates user 1's grade
def grade_pass(grade):
    USER1["grade"] = grade
    return

def grade_fail(grade):
    USER1["grade"] = USER1["grade"]
    return
