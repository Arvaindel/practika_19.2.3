import  pytest
from app.calculator import Calculator
class Test_cal:
    def setup(self):
        self.cal=Calculator

    def test_miltiply(self):
        assert self.cal.multiply(self, 2, 2)==4

    def test_division(self):
        assert self.cal.division(self, 4, 2)==2

    def test_subtraction(self):
        assert self.cal.subtraction(self, 4, 2)==2

    def test_adding(self):
        assert self.cal.adding(self, 4, 4)==8