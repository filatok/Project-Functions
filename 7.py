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
        return max(self.li)
    
    def MinGrade(self):
        return min(self.li)
    
    def MO_Grade(self):
        return sum(self.li)/8
    
s = Student()
s.SetData()
s.PrintData()
print(f'Max grade: {s.MaxGrade()}')
print(f'Max grade: {s.MinGrade()}')
print(f'Mesos oros: {s.MO_Grade()}')