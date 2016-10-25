def array_left_rotation(a, n, k):
	n, k = map(int, raw_input().strip().split(' '))
	a = map(int, raw_input().strip().split(' '))
	answer = (a[k:]+a[:k]);
	print ' '.join(map(str,answer))


a = [1, 2, 3, 4, 5]
n = len(a)
k = 4
array_left_rotation(a, n, k)