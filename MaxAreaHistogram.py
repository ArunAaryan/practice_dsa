def maxAreaHistogram(arr):
    n = len(arr)
    left_smaller = [-1] * n
    right_smaller = [n] * n
    i  = 0
    st = [-1]
    while i < n:
        while st and st[-1] != -1 and arr[st[-1]] > arr[i]:
            right_smaller[st[-1]] = i
            st.pop()
        if i > 0 and arr[i] == arr[i - 1]:
            left_smaller[i] = left_smaller[i - 1]
        else:
            left_smaller[i] = st[-1]
        st.append(i)
        i += 1
    print(left_smaller)
    print(right_smaller)
    area = 0
    for i in range(n):
        area = max(area , arr[i] * (right_smaller[i] - left_smaller[i] - 1))
    print(area)


maxAreaHistogram([6, 2, 5, 4, 5, 1, 6])
