class student:
    def __init__(self,name,id,major):
        self.name = name
        self.id = id
        self.major = major

#Add elective courses
class AddCourse(student):
    def __init__(self,coursename,):
        self.coursename = coursename

#Withdraw from a course
class WithdrawCourse(student):
    def __init__(self,coursename,):
        self.coursename = coursename

#Query courses
class QueryCourses(student):
    def __init__(self,):
        self


if __name__ =="__main__":
    stu1 = student("Tom","Sp269","Information Engineering")