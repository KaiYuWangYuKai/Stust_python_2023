class student:
    def __init__(self,name,id,major,course):
        self.name = name
        self.id = id
        self.major = major
        self.course = course
    @property
    def course_name(self):
        return self.course
    @course_name.setter
    def course_name(self,value):
        self.course = value
    def practice(self):
        print("YY")

#Add elective courses
class AddCourse(student):
    def __init__(self,coursename,add):
        super().__init__(coursename)
        self.add = add
    @property
    def AddCourse_add(self):
        return self.add
    
    def practice(self):
        print("Add elective courses")    

#Withdraw from a course
class WithdrawCourse(student):
    def __init__(self,coursename,withdraw):
        super().__init__(coursename)
        self.withdraw = withdraw

    @property
    def WithdrawCourse_withdraw(self):
        return self.withdraw

    def practice(self):
        print("Withdraw from a course")

#Query courses
class QueryCourses(student):
    def __init__(self,coursename,query):
        super().__init__(coursename)
        self.query = query

    @property
    def QueryCourse_query(self):
        return self.query

    def practice(self):
        print("Query courses")


if __name__ =="__main__":
    stu1 = student("Tom","Sp269","Information Engineering","none")
    stu1.course = AddCourse("CSIC")