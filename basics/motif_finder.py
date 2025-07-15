def motif_finder(s,t):
	position=[]
	for i in range(len(s)-len(t)+1):
		if s[i:i+len(t)]==t:
			position.append(i+1)
	return position
if __name__=="__main__":
	s=input("Enter a dna seq: ").strip().upper()
	t=input("Enter a motif seq: ").strip().upper()
	result=motif_finder(s,t)
	print("Motif found at position: ")
	print(" ".join(str(pos)for pos in result))
