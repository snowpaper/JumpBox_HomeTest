# Fibonacci series using recursion
def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)

# Input number for output Fibonacci Number.
if __name__ == "__main__":
#	n = 9
	n = int(input("Input  : n = "))
	print("Output : ",fibonacci(n))
