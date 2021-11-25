def getMaxXor(k):
	k = (2 ** k) - 1
	LXR = 0 ^ k 

	msbPos = 0
	while(LXR):
		msbPos += 1
		LXR >>= 1
	maxXOR, two = 0, 1
	while (msbPos):
		maxXOR += two
		two <<= 1
		msbPos -= 1
	return maxXOR
def getFact(n):
	f = 1
	for i in range(1, n + 1):
		f = f * i
	return f
res = getMaxXor(2)
from itertools import permutations
def getAllPairs(n, k):
	k = (2 ** k) - 1
	k = getFact(k)
	print(k)
	r = k - n
	r = getFact(r)
	print(k, r, k / r)

	# for perm in p:
		# print(p)
res = getAllPairs(4, 3)
