import view_course

def test_view_course():
    #Check to see user 1 can only view their courses (courseNo = 1)
    courseNo = 2
    viewed = view_course.view_course_fail(courseNo)
    assert viewed == False
