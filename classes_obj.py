class Student: 
    def __init__(self, name, major, gpa1, gpa2, is_on_probation):
        self.name = name
        self.major = major
        self.gpa1 = gpa1
        self.gpa2 = gpa2
        self.tgpa = (gpa1 + gpa2)/2
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if(self.tgpa) >= 3.5:
            return True
        else:
            return False
        
