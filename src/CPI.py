class CPI:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no = roll_no
        self.marks=marks
        if 51<=self.marks <=60:
            self.cpi=6.0
        elif 61<=self.marks <=70:
            self.cpi=7.0
        elif 71<=self.marks<=80:
            self.cpi=8.0
        elif 81<=self.marks <=90:
            self.cpi=9.0
        elif 91<=self.marks<=100:
            self.cpi=10.0
    def get_name(self):
        return self.name
    def set_name(self,aryan):
        self.name =aryan
    def get_roll_no(self):
        return self.roll_no
    def set_roll_no(self,roll_no):
        self.roll_no=7
    def get_marks(self):
        return self.marks
    def set_marks(self,marks):
        self.marks=marks
a=CPI('aryan',7,65)
b=CPI('tushar',26,85)
c=CPI('divyanshu',10,55)
print(a.cpi)
print(b.cpi)
print(c.cpi)



