def summa(num):
    result = sum(map(int, num))
    return result

def summ(num):

    sum_ = 0
    for digit in num:
        if digit.isdigit():
            sum_ += int(digit)
    return sum_

print(summa('1232'))
print(summ('123m2k'))



