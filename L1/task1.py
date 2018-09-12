def crossing(x1,y1,x2,y2,x3,y3,x4,y4):
	'''
	Task #1: Function crossing gets 4 points ---
		 A_1(x_1, y_1), A_2(x_2, y_2)
		 B_1(x_3, y_3), B_2(x_4, y_4)

	As we remember, y(x) = k * x + b --- equation of line.
	As we have two lines, we have 2 sets of parameters:
	for line 1 --- k_1 and b_1
	for line 2 --- k_2 and b_2

	We have the following system of linear equations:
	k_1 * x_1 + b_1 = y_1
	k_2 * x_2 + b_2 = y_2
	k_3 * x_3 + b_3 = y_3
	k_4 * x_4 + b_4 = y_3
	From this system we obtain parameters of lines

	As we also know, two lines are parallel, 
	if angular coefficients are equal.

	To calculate coordinates of crossing point we 
	solve the following system of equations:
	y = k_1 * x + b_1
	y = k_2 * x + b_2
	'''
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
	'''
	Task#2: Fibonnachi numbers
	0 1 1 2 3 5 8 13 21 34 ...

	The reccurent formula is as follows:
	F[0] = 0
	F[1] = 1
	F[N] = F[N-1] + F[N-2]
	'''
	if N < 2:
		return N
	return reccurent_fib(N-1) + reccurent_fib(N-2)

def mouse_traj( N ):
	'''
	Task#3: Mouse
	We believe, that the end point 0 can be reached by one trajectory.
	Point 1 can be reached only from point 0.
	Point 2 can be reached from 2 points: 0 and 1.
	Other points can be reached from two points: point K from points K-1 and K-2.
	But points with number K = 7 * q are illegal.
	'''
	if N == 0:
		return 1
	if N <= 2:
		return N
	if N % 7 == 0:
		return 0
	return mouse_traj(N-1) + mouse_traj(N-2)

def is_prime( N ):
	'''
	Task#4: Prime numbers
	1 is not prime
	Then we check, if numbers from 2 to N are devisors of N.
	If N = divisor * q, then N is not prime.
	'''
	if N == 1:
		return 'neither prime, nor non-prime'
	i = 2
	while i < N:
		if N % i == 0: return 'not prime'
		i += 1
	return 'is prime'

def all_divisors( N ):
	'''
	Task#5: Print all divisors of number N
	if N = 1, we will return 1
	else we will check, if number from 2 to N is a divisor.
	if it is a divisor, we will print it.
	'''
	if N == 1:
		return N
	i = 2
	while i < N:
		if N % i == 0: print( i )
		i += 1
	print( N )

def div_decomposition( N ):
	'''
	Task: Number decomposition
	Decompose number N
	'''
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
