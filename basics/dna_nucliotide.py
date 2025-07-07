# A DNA string were given count the number of each bases present in the given dna seq
# taking input from user and converting its to capital letter
s = input("Enter a DNA sequence: ").upper()

if all(base in "ATGC" for base in s):   #to check proper base were entered
    print("Valid DNA sequence entered.")
    
    a_count = 0                      #start the count with 0
    t_count = 0
    g_count = 0
    c_count = 0

    for base in s:
        if base == "A":
            a_count += 1
        elif base == "T":
            t_count += 1
        elif base == "G":
            g_count += 1
        elif base == "C":
            c_count += 1

    print(f"{a_count}   {t_count}   {g_count}   {c_count}")
