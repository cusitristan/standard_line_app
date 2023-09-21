import pytest
import line 
from fractions import Fraction

# Testing slope() function
def test_slope_non_unique_points():
	pnt_1 = (1,2)
	pnt_2 = pnt_1
	with pytest.raises(ZeroDivisionError):
		line.slope(pnt_1, pnt_2)

def test_slope_return_val_type():
	pnt_1 = (1,2)
	pnt_2 = (2,1)
	assert type(line.slope(pnt_1, pnt_2)) == Fraction

def test_slope_with_zero_point():
	pnt_1 = (0,0)
	pnt_2 = (2,1)
	assert line.slope(pnt_1, pnt_2) == 0.5

def test_slope_positive_int_positive_slope():
	pnt_1 = (1,2)
	pnt_2 = (5,7)
	assert line.slope(pnt_1, pnt_2) == 1.25

def test_slope_negative_int_positive_slope():
	pnt_1 = (-1,-2)
	pnt_2 = (-5,-7)
	assert line.slope(pnt_1, pnt_2) == 1.25

def test_slope_positive_int_negative_slope():
	pnt_1 = (1,9)
	pnt_2 = (5,4)
	assert line.slope(pnt_1, pnt_2) == -1.25

def test_slope_negative_int_negative_slope():
	pnt_1 = (-1,-9)
	pnt_2 = (-5,-4)
	assert line.slope(pnt_1, pnt_2) == -1.25

def test_slope_mixed_int():
	pnt_1 = (2,-7)
	pnt_2 = (-1,9)
	assert line.slope(pnt_1, pnt_2) == Fraction(16,-3)

def test_slope_positive_float_positive_slope():
	pnt_1 = (1.5,2.5)
	pnt_2 = (5.5,7.5)
	assert line.slope(pnt_1, pnt_2) == 1.25

def test_slope_negative_float_positive_slope():
	pnt_1 = (-1.25,-2.25)
	pnt_2 = (-5.25,-7.25)
	assert line.slope(pnt_1, pnt_2) == 1.25

def test_slope_positive_float_negative_slope():
	pnt_1 = (1.1,9.1)
	pnt_2 = (5.1,4.1)
	assert line.slope(pnt_1, pnt_2) == -1.25

def test_slope_negative_float_negative_slope():
	pnt_1 = (-1.0,-9.0)
	pnt_2 = (-5.0,-4.0)
	assert line.slope(pnt_1, pnt_2) == -1.25

def test_slope_mixed_float():
	pnt_1 = (2.0,-7.0)
	pnt_2 = (-1.0,9.0)
	assert line.slope(pnt_1, pnt_2) == Fraction(16,-3)

# Testing least_common_denominator() function
def test_least_common_denominator_return_val_type():
	f1 = Fraction(1,2)
	f2 = Fraction(2,3)
	f3 = Fraction(3,5)
	assert type(line.least_common_denominator([f1,f2,f3])) == int

def test_least_common_denominator_one_input_value():
	f1 = Fraction(1,2)
	assert line.least_common_denominator([f1]) == 2

def test_least_common_denominator_postive_values():
	f1 = Fraction(1,2)
	f2 = Fraction(2,3)
	f3 = Fraction(3,5)
	assert line.least_common_denominator([f1,f2,f3]) == 30

def test_least_common_denominator_negative_values():
	f1 = Fraction(-1,2)
	f2 = Fraction(-2,3)
	f3 = Fraction(-3,5)
	assert line.least_common_denominator([f1,f2,f3]) == 30

def test_least_common_denominator_mixed_values():
	f1 = Fraction(-1,2)
	f2 = Fraction(2,3)
	f3 = Fraction(-3,5)
	assert line.least_common_denominator([f1,f2,f3]) == 30

# Testing standard_form() function
def test_standard_form_non_unique_points():
	pnt_1 = (1,2)
	pnt_2 = pnt_1
	with pytest.raises(ZeroDivisionError):
		line.standard_form(pnt_1, pnt_2)

def test_standard_form_return_val():
	pnt_1 = (1,2)
	pnt_2 = (2,1)
	assert type(line.standard_form(pnt_1, pnt_2)) == tuple
	assert type(line.standard_form(pnt_1, pnt_2)[0]) == int
	assert type(line.standard_form(pnt_1, pnt_2)[1]) == int
	assert type(line.standard_form(pnt_1, pnt_2)[2]) == int
	assert len(line.standard_form(pnt_1, pnt_2)) == 3

def test_standard_form_vertical_line():
	pnt_1 = (8,9)
	pnt_2 = (8,13)
	assert line.standard_form(pnt_1, pnt_2) == (1,0,8)

def test_standard_form_horizontal_line():
	pnt_1 = (4,9)
	pnt_2 = (8,9)
	assert line.standard_form(pnt_1, pnt_2) == (0,1,9)

def test_standard_form_swap_points():
	pnt_1 = (4,9)
	pnt_2 = (8,9)
	assert line.standard_form(pnt_1,pnt_2) == line.standard_form(pnt_2,pnt_1)

def test_standard_form_positive_int():
	pnt_1 = (1,2)
	pnt_2 = (5,7)
	assert line.standard_form(pnt_1, pnt_2) == (5,-4,-3)

def test_standard_form_negative_int():
	pnt_1 = (-1,-2)
	pnt_2 = (-5,-7)
	assert line.standard_form(pnt_1, pnt_2) == (5,-4,3)

def test_standard_form_positive_float():
	pnt_1 = (1.1,2.1)
	pnt_2 = (5.1,7.1)
	assert line.standard_form(pnt_1, pnt_2) == (50,-40,-29)

def test_standard_form_negative_float():
	pnt_1 = (-1.25,-2.75)
	pnt_2 = (-5.75,-7.25)
	assert line.standard_form(pnt_1, pnt_2) == (2,-2,3)
