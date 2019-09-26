import view_course

def test_view_course():
    #Check to see user 1 can view their own courses only (courseNo = 1)
    courseNo = 2
    viewed = view_course.view_course_fail(courseNo)
    assert viewed == False
