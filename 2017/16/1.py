import sys
with open('advent-input.txt') as f:
    a = f.readlines()[0].split(",");

s = ""
for i in xrange(16):
	s += (chr(97+i))

init_s = s
for j in xrange(1000000000%30):
	for instr in a:
		op = instr[0]
		if op == 's':
			x = int(instr[1:])
			s = s[len(s)-x:] + s[0:len(s)-x]

		elif op == 'x':
			A,B = instr[1:].split('/')
			A,B = int(A), int(B)

			tmp = s[B]
			s = s[0:B] + s[A] + s[B+1:]
			s = s[0:A] + tmp + s[A+1:]
		elif op == 'p':
			A,B = instr[1:].split('/')

			tmpIndA = s.index(A);
			tmpIndB = s.index(B);

			tmpA = s[tmpIndA];
			tmpB = s[tmpIndB];

			s = s[0:tmpIndA] + tmpB + s[tmpIndA+1:]
			s = s[0:tmpIndB] + tmpA + s[tmpIndB+1:]

		else:
			print "Op is " + str(op)
			sys.exit()
	if s == init_s:
		period = j+1
		print period
		sys.exit()


print s