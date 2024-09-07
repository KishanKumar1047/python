# n = int(input("Enter : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")

# n = int(input("Enter : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end="")
#     print("")


# n = int(input("Enter : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("")


# n = int(input("Enter : "))
# for i in range(1,n+1):
#     m = 65
#     for j in range(1,i+1):
#         print(chr(m),end="")
#         m += 1

#     print("")


def print_number_pyramid(rows):
	for i in range(1, rows + 1):
		# Print spaces
		for j in range(rows - i):
			print(" ", end="")
		# Print numbers
		for j in range(2 * i - 1):
			print(j + 1 , end=" ")
		# Move to the next line after each row
		print()

# Example usage
num_rows = 5
print_number_pyramid(num_rows)
