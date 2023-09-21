from typing import Tuple, List
from fractions import Fraction
import math

def standard_form(pnt_1: Tuple[float, float], pnt_2: Tuple[float, float])\
	-> Tuple[int, int, int]:
	"""	This function outputs the standard form of a line based on two 
		unique input cartesian points. 

		Due to how floating point values are stored (in base 2 not base 
		10) there can be inaccuracies when dealing with certain float 
		values. 

		For example 1/10 = 0.1 this float does not repeat in base 10 
		but it does in base 2 which means converting it to a fraction 
		loses some precision. 

		For this reason an input of (1.1, 2.1), (5.1, 7.7) which would 
		have an expected output of 
			=> 5x - 4y = -3 
			actually outputs 
			=> 50x -40y = -29

		Args:
			pnt_1: Tuple of cartesian coordinates (x, y) for 1st point
			pnt_2: Tuple of cartesian coordinates (x, y) for 2nd point

		Returns:
			Tuple with three int values representing A, B, and C from
			standard form of line Ax + By = C
	"""
	#vertical or horizontal line 
	if((pnt_1[0] == pnt_2[0]) and not(pnt_1[1] == pnt_2[1])):
		lcm = least_common_denominator(\
			[Fraction(pnt_1[0]).limit_denominator()])
		return (1, 0, int(pnt_1[0] * lcm))
	elif((pnt_1[1] == pnt_2[1]) and not(pnt_1[0] == pnt_2[0])):
		lcm = least_common_denominator(\
			[Fraction(pnt_1[1]).limit_denominator()])
		return (0, 1, int(pnt_1[1] * lcm))

	m = slope(pnt_1, pnt_2)
	# point-slope form => [ y - y_1 = m(x - x_1) ]
	# convert to standard form => [ m(x) - 1(y) = m(x_1) - y_1 ]
	A = m
	B = Fraction(-1)
	C = m * Fraction(pnt_1[0]).limit_denominator()\
		  - Fraction(pnt_1[1]).limit_denominator()
	# to follow standard form A, B and C must be integers 
	lcm = least_common_denominator((A,B,C))
	if A < 0:
		return (int(-A * lcm), int(-B * lcm), int(-C * lcm))
	else:
		return (int(A * lcm), int(B * lcm), int(C * lcm))

def slope(pnt_1: Tuple[float, float], pnt_2: Tuple[float, float]) -> Fraction:
	""" This function calculates the slope of a line based on two 
		unique input cartesian points. """
	numerator = Fraction(pnt_2[1] - pnt_1[1]).limit_denominator() 
	denominator = Fraction(pnt_2[0] - pnt_1[0]).limit_denominator()
	return Fraction(numerator, denominator)

# this came from reddit user:lejar from this post:
# https://www.reddit.com/r/learnpython/comments/9c89pk/python_how_to_find_leastcommon_denominator/
def least_common_denominator(fractions: List[Fraction]) -> int:
	""" This function finds the least common denominator for a list of 
		fractions. """
	denominators = [Fraction(r).denominator for r in fractions]
    
	lcm = denominators[0]
	for d in denominators[1:]:
		lcm = lcm // math.gcd(lcm, d) * d

	return lcm