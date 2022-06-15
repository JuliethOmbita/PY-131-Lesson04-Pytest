import statistics 
import math 

class Calculator():
	"""Calculator"""
	
	def add(self, *args):
		return sum(args)

	def sub(self, x, y):
		return x - y

	def multi(self, x, y):
		return x * y

	def division(self, x, y):
		if y == 0:
			return None
		return x / y

	def is_even(self, x):
		if x % 2 == 0:
			return True 
		return False 

	def divisors(self, x):
		divisors = []
		for i in range(1,x + 1):
			if x % i == 0:
				divisors.append(i)
		return divisors

	def cosine(self, x):
		return math.cos(x)

	def average(self, nums):
		return statistics.mean(nums)

	def is_prime(self, num):
		return False if num < 2 or [False for x in range(2, int(math.sqrt(num))+1) if num % x == 0] else True

if __name__ == "__main__":
    calc = Calculator()
    x = 3
    y = 3
    val1 = 0
    val2 = 270
    list_avg = [3, 3, 4, 10]
    val3 = 5
    val4 = 7
    val5 = 10
    print("\n")
    print(f"{x} + {y} = {calc.add(3,3)} \n")
    print(f"{x} - {y} = {calc.sub(3,3)} \n")
    print(f"{x} * {y} = {calc.multi(3,3)} \n")
    print(f"Cos({val1}) = {calc.cosine(val1)} \n")
    print(f"Cos({val2}) = {calc.cosine(val2)} \n")
    print(f"The average value of ({list_avg}) is:  {calc.average(list_avg)} \n")
    print(f"Is prime({val3})? {calc.is_prime(val3)} \n")
    print(f"Is prime({val4})? {calc.is_prime(val4)} \n")
    print(f"Is prime({val5})? {calc.is_prime(val5)} \n")

	