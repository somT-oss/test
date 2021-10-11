import calculator 

class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add_two_num(1, 3)

    def test_subtraction(self):
        assert 6 == calculator.subtract_two_num(10, 4)