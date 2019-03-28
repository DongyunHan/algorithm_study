#p_1094

INIT_LENGTH = 64

def get_lengthX(target_length, current_length, num_bar=1):
    if current_length > target_length:
        return get_lengthX(target_length, current_length/2, num_bar)
    elif current_length < target_length:
        return get_lengthX(target_length - current_length, current_length, num_bar+1)
    else:
        return num_bar

target_length = int(input())
print(get_lengthX(target_length, INIT_LENGTH))
