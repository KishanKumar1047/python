   #fibonacci 
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


# Driver Program
print(Fibonacci(9))

# # Python 3 program to find 
# # factorial of given number
# def factorial(n):
	
# 	# single line to find factorial
# 	return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))


# # Python 3 program to find 
# # factorial of given number
# def factorial(n):
# 	if n < 0:
# 		return 0
# 	elif n == 0 or n == 1:
# 		return 1
# 	else:
# 		fact = 1
# 		while(n > 1):
# 			fact *= n
# 			n -= 1
# 		return fact

# # Driver Code
# num = 5
# print("Factorial of",num,"is",
# factorial(num))

# # This code is contributed by Dharmik Thakkar
   