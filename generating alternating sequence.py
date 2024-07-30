n = int(input("Enter the value of n: "))
sequence = [(-1)**i * (i+1) * 50 for i in range(n)]
print(sequence)
