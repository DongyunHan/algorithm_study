def return_num_of_digit(num_value):
    if isinstance(num_value, int):
        return len(str(abs(num_value)))
    else:
        raise ValueError("Not Int Error")

def return_digit_list(num, digit):
    digit_list = []

    for i in range(digit):
       digit_list.append(int(str(num)[i]))

    return digit_list

def is_arithmetic_progression(digit_list):
    if(len(digit_list)==1 or len(digit_list)==2):
        return True
    else:
        diff = digit_list[0] - digit_list[1]
        if diff ==0:
            return False

        for i in range(1,len(digit_list)):
            if diff != digit_list[i] - digit_list[i+1]:
                return False

        return True

num=0
input_value = int(input())

for i in range(1,input_value+1):
    digit_list = return_digit_list(i, return_num_of_digit(i))
    if is_arithmetic_progression(digit_list):
        num+=1

print(num)
