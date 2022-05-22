


def sd_op(digit):
    
    if digit < 10:
        return digit
    else:
        separated_numbers = sum([int(digits) for digits in str(n)])
    return separated_numbers


def superDigit(n, k):
    sd = k*sd_op(int(n))
    return sd
    


if __name__ == "__main__":

    super_digit = input("join 2 numbers n and k: ").rstrip().split()

    n = super_digit[0] #first number
    k = int(super_digit[1]) #repetitions

    digit = int(n)

    resultado = superDigit(n, k)

    print(resultado)



