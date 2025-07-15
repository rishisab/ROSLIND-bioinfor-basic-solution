def gc_content(seq):
	gc=seq.count("G")+seq.count("C")
	return (gc/len(seq)) *100 if seq else 0
seq=input("enter a dna seq: ").upper()
print("your enter seq is: ",seq)
print("gc_content of given seq is: ",gc_content(seq))
