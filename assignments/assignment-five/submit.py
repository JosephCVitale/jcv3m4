
#This function returns true if the filetype is valid (pdf or docx), and false if it is not
def submit_pass(filename, filetype):
    submitted = False
    if filetype == "pdf" or filetype == "docx":
        submitted = True
    return submitted

def submit_fail(filename, filetype):
    submitted = True
    return submitted
