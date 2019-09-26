#failing function
def add_TA_fail(name, course):
    #incorrectly formats result string
    string = "%s added to %s" % (course, name)
    return string

def add_TA_pass(name, course):
    string = "%s added to %s" % (name, course)
    return string
