import random
class Employee:
    def __init__(self,empid,empname,sal):
        self.empid=empid
        self.empname=empname
        self.sal=sal
    def eligible_for_promotion(self):
        if self.sal > 100:
            return True
        else:
            return False
    def __str__(self):
        return str(self.empid)+str(self.empname)+str(self.sal)
    def __repr__(self):
        return "Employee({}) : {}".format(self.empid, self.empname,self.sal)

if __name__ == '__main__':
    emp1=Employee(1,'dileep',100)
    emp2=Employee(2,'kumar',200)
    print(emp1.empid)
    print(emp1.sal)
    print(emp1.eligible_for_promotion())
    print(emp2.eligible_for_promotion())
    print(emp1)