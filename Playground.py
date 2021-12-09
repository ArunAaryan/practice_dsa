def combinationSum4(nums, target):
	nums, combs = sorted(nums), [1] + [0] * (target)
	for i in range(target + 1):
		for num in nums:
			if i == target:
				print('here')
			if num  > i: break
			if num == i: combs[i] += 1
			if num  < i: combs[i] += combs[i - num]
	print(combs)
	return combs[target]
res = combinationSum4([1,2,3], 4)
print(res)
	