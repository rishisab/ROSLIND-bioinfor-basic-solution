def kmer_count(s,k):
	kmer=[]
	for i in range(len(s)-k):
		kmer.append(s[i:i+k])
	return kmer
if __name__=="__main__":
	s=input("enter a dna seq: ").strip().upper()
	k=int(input("enter a kmer number: "))
	count= kmer_count(s,k)
	for kmer in count:
		print(kmer)
	
