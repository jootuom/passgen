#!/usr/bin/env python3
import os

def passgen(length=20, specials=False):
	"""
	Generate [length] random password guaranteed to
	have at least a-z A-Z 0-9 and optionally some 
	special characters too.
	
	For optimal performance the urandom read size
	needs to be set based on the password length.
	"""
	pool = set()
	
	# ASCII codes for uppercase alphabet
	u = set(range(65,91))
	# ASCII codes for lowercase alphabet
	l = set(range(97,123))
	# ASCII codes for numbers
	n = set(range(48,58))
	# ASCII codes for some special characters
	s = set(range(33,47))
	
	pool.update(u, l, n)
	if specials: pool.update(s)
	
	if length <= 6:
		rsize = 24
	elif length <= 8:
		rsize = 32
	elif length <= 12:
		rsize = 48
	elif length <= 16:
		rsize = 64
	elif length <= 20:
		rsize = 96
	else:
		raise ValueError("bad password length")

	while True:
		rand = set(os.urandom(rsize))
		m = rand & pool
		
		matches = [bool(u & m), bool(l & m), bool(n & m)]
		if specials: matches += [bool(s & m)]
		
		# TODO: maybe this could be done without requiring
		# exactly matching length?
		if all(matches) and len(m) == length:
			return "".join([chr(b) for b in m])

if __name__ == "__main__":
	import timeit

	for n in [6, 8, 10, 12, 14, 16, 20]:
		t = timeit.timeit(
			"passgen({})".format(n),
			setup="from passgen import passgen",
			number=100000
		)

		print("length: {0}, time: {1}".format(n, t))

