s=input("enter a dna seq: ").upper()
compliment_dict={
"A":"T",
"G":"C",
"T":"A",
"C":"G"}
compl_seq="".join(compliment_dict[base]for base in s)
reverser_seq=s[::-1]
reverse_compl=compl_seq[::-1]
print("compliment of give seq",s,"is",compl_seq)
print("reverse of given seq",s,"is",reverser_seq)
print("reverse compliment of given seq",s,"is",reverse_compl)
