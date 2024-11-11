# 13
prime_numbers_list: list[int] = []
while True:
    prime_check = int(input("Enter a num: "))
    if prime_check > 1:
        for i in range(2, prime_check):
            if (prime_check % i) == 0:
                #print("not a prime number")
                break
        else:
            prime_numbers_list.append(prime_check)
    if prime_check == 0:
        print("Prime numbers:", " ".join(str(x) for x in prime_numbers_list))
        break