#!/usr/bin/env python

# TODO: write me!
def sum_divisible(n):
    ''' gives the sum of all the numbers up to but not including n
    that are divisible by 3 or by 5 '''
    i = 0
    total = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            total += i
        i += 1
    return total

# NOTE: this is an encoded solution
#       the programme will decode it automatically
#         so you can check your results against it yourself
#       it will create a function called `solution'
solution = None
exec 'fbyhgvba = ynzoqn a: fhz(k sbe k va kenatr(a)' \
     'vs abg k%3 be abg k%5)'.decode('rot13') in locals(), globals()

if __name__ == '__main__':
	# NOTE: some simple tests
	assert sum_divisible(10)      == solution(10)      == 23
	assert sum_divisible(100)     == solution(100)     == 2318
	assert sum_divisible(1000)    == solution(1000)    == 233168
	assert sum_divisible(1000000) == solution(1000000) == 233333166668

	print 'All the tests passed! Great job!'
