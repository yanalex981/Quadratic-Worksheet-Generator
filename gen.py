import random
from sympy import *

if __name__ != '__main__':
	print('not main, exiting')
	exit(0)

class problem_item:
	def __init__(self, problem=None, solution=None):
		self._problem = problem
		self._solution = solution

	@property
	def problem(self):
		return self._problem

	@question.setter
	def problem(self, value):
		self._problem = value

	@property
	def solution(self):
		return self._solution

	@answer.setter
	def solution(self, value):
		self._solution = value

def random_sign():
	return random.choice([-1, 1])

def make_vertex_form(a, h, k, var='x'):
	x = symbols(var)
	expr = a * (x + h)**2 + k
	return expr

def make_factored_form(a, b, c, r, s, var='x'):
	x = symbols(var)
	return a*(b*x - r) * (c*x - s)

def make_common_factor(b, n, c, s, var='x'):
	x = symbols(var)
	expr = (b*x)**n * (c*x - s)
	answer = factor(expr)
	question = expand(expr)

	return problem(question, answer)

def make_diff_of_sq(a, b, var='x'):
	x = symbols(var)
	return (a*x)**2 - b**2

def perf_sq1(a, h, var='x'):
	x = symbols(var)
	return (a*x + h)**2

def perf_sq2(a, k, d, c, var='x'):
	x = symbols(var)
	return a*(k*x + d)**2 + c

def make_grouping(a, b, r, s, var='x'):
	x = symbols(var)
	return a*b*x**2 + a*s*x + b*r*x + r*s

def make_decomposition1(a, r, s, var='x'):
	x = symbols(var)
	return (a*x + r) * (x + s)

def make_decomposition2(a, b, r, s, var='x'):
	x = symbols(var)
	return (a*x + r) * (b*x + s)

def make_quadratic_formula(a, b, c, var='x'):
	x = symbols(var)
	return a*x**2 + b*x + c
