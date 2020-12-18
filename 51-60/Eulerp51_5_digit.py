import math
final_digit=[1,3,7,9]
other_digit=[1,2,3,4,5,6,7,8,9,0]
def prime(num):
    is_prime=True
    max_divisor_check=int(math.sqrt(num))
    for divisor in range(1,max_divisor_check+1):
        if num%divisor==0:
            is_prime=False
            return is_prime
    return is_prime
for units_digit in final_digit:
    for tens_digit in other_digit:
        family_count=0
        for i in range(0,10):
            j=units_digit+tens_digit*10+i*100+i*1000+i*10000
            if prime(j):
                family_count+=1
        if family_count==8:
            print('case 1', tens_digit, units_digit)

for units_digit in final_digit:
    for hundreds_digit in other_digit:
        family_count=0
        for i in range(0,10):
            j=units_digit+i*10+hundreds_digit*100+i*1000+i*10000
            if prime(j):
                family_count+=1
        if family_count==8:
            print('case 2', hundreds_digit, units_digit)

for units_digit in final_digit:
    for thousands_digit in other_digit:
        family_count=0
        for i in range(0,10):
            j=units_digit+i*10+i*100+thousands_digit*1000+i*10000
            if prime(j):
                family_count+=1
        if family_count==8:
            print('case 3', thousands_digit, units_digit)
    )
for units_digit in final_digit:
    for tenthousands_digit in other_digit:
        family_count=0
        for i in range(0,10):
            j=units_digit+i*10+i*100+i*1000+tenthousands_digit*10000
            if prime(j):
                family_count+=1
        if family_count==8:
            print('case 4', tenthousands_digit, units_digit)
