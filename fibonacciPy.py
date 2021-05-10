# 0 1 1 2 3 5 8 13 21 34 55 89
"""
def getNthFib(n):
	if n == 0:
		
		return 0
	if n <= 3:
		
		return 1
	
	return getNthFib(n-1) + getNthFib(n-2)

"""

def getNthFib(n,  calculated = {1:0, 2:1, 3:1,}):
		if n in calculated:
			return calculated[n]

		calculated[n] = getNthFib(n-1, calculated) + getNthFib(n-2, calculated)
		return calculated[n]

print(getNthFib(35))
