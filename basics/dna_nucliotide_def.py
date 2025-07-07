def base_count(s):                         #defining a function
    A=s.count("A")                         
    T=s.count("T")
    G=s.count("G")
    C=s.count("C")
    return A,T,G,C                         #function output
s = input("Enter a DNA sequence: ").upper()

if all(base in "ATGC" for base in s):
    print("Valid DNA sequence entered.")
    print(base_count(s))
else: 
    print("Invalid DNA sequence. Only A, T, G, C allowed.")
