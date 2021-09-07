class student:
    num_students = 0

    def total(self, m1, m2, m3):
        if type(m1) and type(m2) and type(m3) is not int:
            raise TypeError('raise typeerror')
        return m1+m2+m3

    def average(self, m1, m2, m3):
        if type(m1) and type(m2) and type(m3) is not int:
            raise TypeError('raise typeerror')
        return (m1+m2+m3)/3

    def display(self):
        return self.total()

    def display1(self):
        return self.average()


#s1 = student()
#print(s1.total(70,70,70))
#print(s1.average(70,70,70))




