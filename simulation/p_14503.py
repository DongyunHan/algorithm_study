#p_14503

WALL = 1
NOT_CLEANED_ROOM = 0
CLEANED_ROOM= 2

# 헷갈릴 수 있음!!!!
# dy는 세로축 dx는 가로축으로 삼는다.
# 단, array, list의 2D 배열에서 표현 방식은 list[y][x]가 되니까 주의
# (dy, dx) => North / East / South / West
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def count_clean(room):
    num_cleaned_room = 0

    for room_y in room:
        for element in room_y:
            if element == CLEANED_ROOM:
                num_cleaned_room +=1

    return num_cleaned_room

def left_turn(d):
    if d == 0:
        return 3
    else:
        return d-1

def room_clean(room, y, x, d):
    # print(x)
    turn_count = 0

    while True:

        if turn_count == 4:
            # In case 4
            back_y = y - dy[d]
            back_x = x - dx[d]

            if room[back_y][back_x] == WALL:
                print(count_clean(room))
                break
            else:
                y, x, d, turn_count = back_y, back_x, d, 0

        # 1. Clean the current location
        if room[y][x] == NOT_CLEANED_ROOM:
            room[y][x] = CLEANED_ROOM

        # look left
        turn = left_turn(d)
        temp_y = y + dy[turn]
        temp_x = x + dx[turn]

        if room[temp_y][temp_x] == NOT_CLEANED_ROOM:
            # In case 1
            y, x, d, turn_count = temp_y, temp_x, turn, 0
        else:
            # In case 2
            y, x, d ,turn_count = y, x, turn, turn_count+1


def main():
    room_height, room_width = map(int, input().split())
    robot_y, robot_x, robot_dir = map(int, input().split())

    room = []
    for i in range(room_height):
        room.append(list(map(int, input().split())))

    room_clean(room, robot_y, robot_x, robot_dir)
    # print(room)

if __name__ == "__main__":
    main()
