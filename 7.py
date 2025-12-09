class Student:
    am = ''
    name = ''
    li = []

    def SetData(self):
        self.am = input('Arithmo mitroou:')
        self.name = input('Onomateponimo:')
        li = []
        for i in range (0,8):
            list_element = int(input("Give a grade: "))
            li.append(list_element)
        self.li = li

    def PrintData(self):
        print(f'Arithmo mitroou: {self.am}')
        print(f'Onomateponimo: {self.name}')
        print(f'Grades: {self.li}')

    def MaxGrade(self):
        max_grade = self.li[0]
        for i in self.li:
            if i>max_grade:
                max_grade = i
        return max_grade
    
    def MinGrade(self):
        min_grade = self.li[0]
        for i in self.li:
            if i<min_grade:
                min_grade = i
        return min_grade
    
    def MO_Grade(self):
        sum_grade = 0
        for i in self.li:
            sum_grade+=i
        return sum_grade/8
    
s = Student()
s.SetData()
s.PrintData()
print(f'Max grade: {s.MaxGrade()}')
print(f'Max grade: {s.MinGrade()}')
print(f'Mesos oros: {s.MO_Grade()}')