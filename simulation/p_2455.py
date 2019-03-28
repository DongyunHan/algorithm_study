MAX_PASSENGERS = 10000
num_passengers = [0]

def cal_passengers(prev_passenger, out_passenger, in_passenger):
    cur_passenger = prev_passenger - out_passenger + in_passenger

    if cur_passenger >= MAX_PASSENGERS:
        return 10000
    else:
        return cur_passenger

for i in range(4):
    out_passenger, in_passenger = map(int, input().split())

    current_passenger = cal_passengers(num_passengers[i], out_passenger, in_passenger)
    num_passengers.append(current_passenger)

print(max(num_passengers))
