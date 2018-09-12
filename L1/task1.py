def crossing(x1,y1,x2,y2,x3,y3,x4,y4):

	k1 = ( y2 - y1 ) / ( x2 - x1 )
	k2 = ( y4 - y3 ) / ( x4 - x3 )

	if k1 == k2: 
		print('lines are parallel')
		return None

	b1 = y1 - k1 * x1
	b2 = y3 - k2 * x3

	x = ( b2 - b1 ) / ( k1 - k2 )
	y = k1 * x + b1

	return x, y

def reccurent_fib( N ):
	if N < 2:
		return N
	return reccurent_fib(N-1) + reccurent_fib(N-2)

def mouse_traj( N ):
	if N == 0:
		return 1
	if N <= 2:
		return N
	if N % 7 == 0:
		return 0
	return mouse_traj(N-1) + mouse_traj(N-2)

def is_prime( N ):
	if N == 1:
		return 'neither prime, nor non-prime'
	i = 2
	while i < N:
		if N % i == 0: return 'not prime'
		i += 1
	return 'is prime'

def all_divisors( N ):
	if N == 1:
		return N
	i = 2
	while i < N:
		if N % i == 0: print( i )
		i += 1
	print( N )

def div_decomposition( N ):
	if N == 1:
		return N
	i = 2
	while i <= N:
		if N % i == 0:
			print(i)
			N //= i
		else:
			i += 1 
	return 'success'
