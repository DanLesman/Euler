import time

def chain_len(n):
	count = 1
	while n != 1:
		if n%2 == 0:
			n /= 2
			count += 1
		else:
			n = 3 * n + 1
			count += 1
	return count

def longest_seq_in(n):
	seq_lengths = {}
	biggest = 1
	toshow = 0
	i = 1
	while i <= n:
		seq_lengths.setdefault(i, chain_len(i))
		i += 1
	for seq, counts in seq_lengths.iteritems():
		if seq_lengths[seq] > biggest:
			biggest = seq_lengths[seq]
			toshow = (seq)
	return toshow

print longest_seq_in(1 * 10 ** 6)
#	if chain_len(biggest) <= chain_len(i):
##	i += 2
