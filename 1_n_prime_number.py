# Add git

# Function
def is_prime(n):
    prime = True
    for i in range(2,int(n**0.5) + 1): # improve alghoritm
        if n % i == 0:
            prime = False
            break # improve code
    return prime

#main
prime_count = 0
Last_prime_number = 0
for i in range(1,1000001):
    if is_prime(i):
        prime_count += 1
        Last_prime_number = i

print("total prime :",prime_count)
print("Last prime number :",Last_prime_number)
