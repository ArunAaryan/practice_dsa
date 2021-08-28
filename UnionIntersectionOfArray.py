class Solution:
    def find_union_intersection(self, nums1, nums2):
        nums3 = []
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                nums3.append(nums2[j])
                j += 1
            else:
                nums3.append(nums1[i])
                i += 1
                j += 1
        if i < m:
            nums3 += nums1[i:]
        if j < n:
            nums3 += nums2[j:]
        nums4 = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                nums4.append(nums1[i])
                i += 1
                j += 1
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    i += 1
            if i < m and j < n:
                if nums2[j] < nums1[i]:
                    j += 1
            else:
                break
        return (nums3, nums4)

c = Solution()
union, intersection = c.find_union_intersection([1,3, 5],[5,1,2,4])
print(union, intersection)