#ip 2

regs= [1,0,0,0,0,0]
r4 = r2*(r5+7)+4+ 11*r2*(r4+2)^2
r4 = 10551394
if regs[0] == 1:
	r3 = 1
	while r3<=r4:
		r1 = 1
		while r1 <= r4:
			if r4 == r3*r1:
				r0 = r3 + r0

			r1 += 1
		r3 += 1


	r5=14*r2^4+14*r2^3

	r4 = r4 + r5

	r0 = 0


sum = 0
for i in xrange(1, 10551394+1):
	if 10551394 % i == 0:
		sum += i