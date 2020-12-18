def unit_matching(digit):
    if digit==1 or digit==2 or digit==6:
        return 3
    elif digit==4 or digit==9:
        return 4
    elif digit==3 or digit==5 or digit==7 or digit==8:
        return 5
    else:
        return 0

def teens_matching(teen):
    if teen==10:
        return 3
    elif teen==11 or teen==12:
        return 6
    elif teen==15 or teen==16:
        return 7
    elif teen==13 or teen==14 or teen==18 or teen==19:
        return 8
    else:
        return 9

def multiples_ten_matching(num):
    if num==4 or num==5 or num==6:
        return 5
    elif num==2 or num==3 or num==8 or num==9:
        return 6
    else:
        return 7

def letter_count_of_and_below(n=1000):
    grand_sum=0
    hundreds_digit=None
    tens_digit=None
    units_digit=None
    for i in range(1,n+1):
        sum=0
        hundreds_digit=i//100
        if i==1000:
            sum=11
        elif i==hundreds_digit*100:
            sum=sum+unit_matching(hundreds_digit)+7
        else:
            if hundreds_digit != 0:
                sum=sum+unit_matching(hundreds_digit)+10
            i=i-hundreds_digit*100
            tens_digit=i//10
            if tens_digit>1:
                sum=sum+multiples_ten_matching(tens_digit)
            elif tens_digit==1:
                sum=sum+teens_matching(i)
            units_digit=i-tens_digit*10
            if tens_digit != 1:
                sum=sum+unit_matching(units_digit)
        grand_sum=grand_sum+sum
    print('\n\nThe grand sum is', grand_sum)
    return
letter_count_of_and_below()
