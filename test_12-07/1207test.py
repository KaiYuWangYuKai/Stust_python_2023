#建立類別
class student ():

    SchoolName = "STUST"
    Schooladdress = "南台街1號"
    def __init__(self) -> None:
        pass
    def __init__(self,SchoolName,Department,ID,grade,Score,Grade_GPA,name):
        self.SchoolName = SchoolName
        self.Department = Department
        self.ID = ID
        self.Drade = grade
        self.Score = Score
        self.Grade_GPA = Grade_GPA
        self.name = name

    @property
    def student_name(self):
        print(f'"{self.name}"was accessed')
        return self.name
    @student_name.setter
    def student_name(self,value):
        print(f'"{self.name}"is now"{value}".')
        self.name = value
    @student_name.deleter
    def student_name(self):
        print(f'"{self.name}"was deleted')
        del self.name


    def get_SchoolName(self):
        return self.SchoolName

    def set_SchoolName(self,value):
        self.SchoolName = value

    def get_Department(self):
        return self.Department

    def set_Department(self,value):
        self.Department = value

    def get_ID(self):
        return self.ID

    def set_ID(self,value):
        self.ID = value

    def get_grade(self):
        return self.grade

    def set_grade(self,value):
        self.grade = value
    
    def get_Score(self):
        return self.Score

    def set_Score(self,value):
        self.Score = value
    
    def get_Grade_GPA(self):
        return self.Grade_GPA

    def set_Grade_GPA(self,value):
        self.Grade_GPA = value

#建立類別為student的物件stu1

if __name__=="__main__":
    stu1 = student("STUST","CSIE","4B0G0147","3","69","3.00","GG")
    print(stu1.student_name)
    stu1.set_SchoolName("TSUTS")
    print(stu1.get_SchoolName())