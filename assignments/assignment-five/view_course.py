from database import USER1

def view_course_pass(courseNo):
    if courseNo == USER1["courseNo"]:
        return True
    else:
        return False

def view_course_fail(courseNo):
    if courseNo == USER1["courseNo"]:
        return True
    else:
        return True
