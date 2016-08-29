o = open('prime10000.csv', 'w')
o.write('n,prime(n)\n')
i = 0

f = open('primes.txt', 'r')
for line in f:
	for num in line.split(' '):
		if num.isdigit():
			i += 1
			o.write('{},{}\n'.format(i,num))
			print num