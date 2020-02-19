def get_multip(sum):
    for a in range(1, sum):
        for b in range(a, sum):
            if 2*a*b + sum**2 == 2*sum*(a + b):
                return a * b * (sum - a - b)

	
print(get_multip(1000))