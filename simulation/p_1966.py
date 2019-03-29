#p_1966

def make_printout(queue, target):
    if queue[0] == max(queue):
        if target == 0:
            return queue[1:]
        else:
            return make_printout(queue[1:], target-1)
    else:
        if target-1 < 0:
            target = len(queue)

        return make_printout(queue[1:] + queue[:1], target-1)

def get_output_time(queue, target):
    output_queue = make_printout(queue, target)
    return len(queue) - len(output_queue)

num_cases = int(input())

for each_case in range(num_cases):
    num_doc, target_index = map(int, input().split())

    print_queue= list(map(int, input().split()))
    print(get_output_time(print_queue, target_index))
