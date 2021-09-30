# def digSum( n):
# 	sum = 0
# 	while(n > 0 or sum > 9):
# 		if(n == 0):
# 			n = sum
# 			sum = 0
# 		sum += n % 10
# 		n //= 10
# 	return sum
# number = int(input())
# if digSum(number) == 1:
#     print("UNO")
# else:
#     print("NOT UNO")


# Python3 implementation of
# the above approach

# Function to print the final position
# of the point after traversing through
# the given directions
def finalCoordinates(SX, SY, D):
	
	# Traversing through the given directions
	for i in range (len(D)):
		
		# If its north or south the point
		# will move left or right
		if (D[i] == 'N'):
			SY += 1
		elif (D[i] == 'S'):
			SY -= 1
			
		# If its west or east the point
		# will move upwards or downwards
		elif (D[i] == 'E'):
			SX += 1
		else :
			SX -= 1

	# Returning the final position
	ans = '(' + str(SX) + ',' + str(SY) + ')'
	print (ans)
	
# Driver Code
if __name__ == '__main__':
	SX, SY = 2,2
	D = "NESW"
	
	finalCoordinates(SX, SY, D)
	

# This code is contributed by parna_28
