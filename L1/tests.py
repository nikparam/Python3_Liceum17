from task1 import *

print('Task#1')

print( crossing( -1, 0, 1, 0, 0, -1, 0, 1 ) )
print( crossing( -1, -1, 1, 1, -1, 1, 1, -1 ) )
print( crossing( -1, -1, -1, 1, 1, 1, 1, -1 ) )
print( crossing( -1, 0, 0, -1, 0, -1, 1, 0 ) )
print( crossing( 0, 3, 0, 4, 0, -5, 0, -1 ) )
print('-----------------------------------------')

print('Task#2')

print( 'N =', 0, 'Fibonnachi number =', reccurent_fib( 0 ) )
print( 'N =', 1, 'Fibonnachi number =', reccurent_fib( 1 ) )
print( 'N =', 5, 'Fibonnachi number =', reccurent_fib( 5 ) )
print( 'N =', 10, 'Fibonnachi number =', reccurent_fib( 10 ) )
print( 'N =', 20, 'Fibonnachi number =', reccurent_fib( 20 ) )
print('-----------------------------------------')

print('Task#3')

print( 'N =', 0, 'Number of trajectories =', mouse_traj( 0 ) )
print( 'N =', 1, 'Number of trajectories =', mouse_traj( 1 ) )
print( 'N =', 2, 'Number of trajectories =', mouse_traj( 2 ) )
print( 'N =', 7, 'Number of trajectories =', mouse_traj( 7 ) )
print( 'N =', 10, 'Number of trajectories =', mouse_traj( 10 ) )
print('-----------------------------------------')

print('Task#4')
print( 0, is_prime(0) )
print( 1, is_prime(1) )
print( 2, is_prime(2) )
print( 10, is_prime(10) )
print( 101, is_prime(101) )
print('-----------------------------------------')

print('Task#5')
print(10, 'divisors:', end = ' ')
all_divisors(10)
print(128, 'divisors:', end = ' ')
all_divisors(128)
print(324, 'divisors:', end = ' ')
all_divisors(324)
print('-----------------------------------------')


