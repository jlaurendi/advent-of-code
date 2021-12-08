import sys
a = 1
b = 81
c = b
d = 0
e = 0
f = 0
g = 0
h = 0

b *= 100
b -= -100000
c = b + 17000
# 108100 125100
while True:
	f = 1
	d = 2

	while True:
		if b % d == 0:
			f = 0
			break
		# e = 2
		# while True:
		# 	if d * e == b:
		# 		f = 0
		# 	e += 1
		# 	if e == b:
		# 		break
		d += 1
		if d >= b**.5: 
			break
	if f == 0:
		h += 1
	if b == c:
		print h
		sys.exit()
	b += 17
# set f 1
# set d 2
# set e 2 // -13
# set g d // -8
# mul g e
# sub g b
# jnz g 2
# set f 0
# sub e -1
# set g e
# sub g b
# jnz g -8 // -8
# sub d -1
# set g d
# sub g b
# jnz g -13 // -13
# jnz f 2
# sub h -1
# set g b
# sub g c
# jnz g 2
# jnz 1 3
# sub b -17
# jnz 1 -23