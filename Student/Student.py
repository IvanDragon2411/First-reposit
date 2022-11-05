import datetime

class Student:
    name=''
    #Я зробив таку дату просто щоб тут щось було.
    DateofBirth=2010
    group=1
    GPA=9
    def __init__(self, name='', DateofBirth=2010, group=1, GPA=9):
        self.name = name
        self.DateofBirth = DateofBirth
        self.group = group
        self.GPA = GPA

    def __str__(self):
        return f'== {self.name} == \n'\
               f'DateofBirth {self.DateofBirth} \n'\
               f'Group {self.group} \n'\
               f'GPA {self.GPA} \n'

    def get_age(self):
        year = datetime.date.today().year
        Student_age = year - self.DateofBirth
        print(Student_age)