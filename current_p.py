# p_13460
# -> Timeout ...

# BFS 를 활용해야하는 것 같음.
# 왼쪽 오른쪽 위 아래 기울이는 것으로 각 스텝마다 4개의 child를 가지게 됨.
# 그 중에서 기울인 후의 공의 위치가 동일하다면 버릴 것.

import copy
import math

WALL = '#'
EMPTY = '.'
GOAL = 'O'
history = []

height = 0
width = 0

# east west south  north
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

class Box_Status:
    def __init__(self, box , depth):
        self.box= box
        self.depth = depth

        for i in range(height):
            for j in range(width):
                if self.box[i][j] == 'B':
                    self.b_ball_x = j
                    self.b_ball_y = i

                if self.box[i][j] == 'R':
                    self.r_ball_x = j
                    self.r_ball_y = i
                    # print("R : " ,i , ' ', j)

                if self.box[i][j] == 'O':
                    self.g_x = j
                    self.g_y = i

    def isOut(self):
        if (self.b_ball_y, self.b_ball_x) == (self.g_y, self.g_x):
            return -1
        elif (self.r_ball_y, self.r_ball_x) == (self.g_y, self.g_x):
            return 1
        else:
            return 0

    def set_r(self, y, x):
        self.r_ball_y = y
        self.r_ball_x = x

    def showBox(self):
        for line in self.box:
            print(line)

def move_r(box, d):

    for i in range(width*abs(dx[d]) + height*abs(dy[d])):
        if (box.box[box.r_ball_y + dy[d]][box.r_ball_x + dx[d]] == EMPTY):
            box.box[box.r_ball_y][box.r_ball_x] = EMPTY

            box.r_ball_y = box.r_ball_y + dy[d]
            box.r_ball_x = box.r_ball_x + dx[d]

            box.box[box.r_ball_y][box.r_ball_x] = 'R'
        elif box.box[box.r_ball_y+ dy[d]][box.r_ball_x+ dx[d]] == GOAL:
            box.box[box.r_ball_y][box.r_ball_x] = EMPTY

            box.r_ball_y = box.r_ball_y + dy[d]
            box.r_ball_x = box.r_ball_x + dx[d]

            # box.box[box.r_ball_y][box.r_ball_x] = 'R'
            break
        else:
            break
        # elif box.box[box.r_ball_y+ dy[d]][box.r_ball_x+ dx[d]] == GOAL:
        #     break


    # box.r_ball_x = 0
    # box.set_r(0,0)
    # box.showBox()
    return box

def move_b(box, d):
    # temp_box = box.box
    # temp_b_y = box.b_ball_y
    # temp_b_x = box.b_ball_x

    for i in range(width*abs(dx[d]) + height*abs(dy[d])):
        if (box.box[box.b_ball_y+ dy[d]][box.b_ball_x+ dx[d]] == EMPTY) :
            box.box[box.b_ball_y][box.b_ball_x] = EMPTY

            box.b_ball_y = box.b_ball_y + dy[d]
            box.b_ball_x = box.b_ball_x + dx[d]

            box.box[box.b_ball_y][box.b_ball_x] = 'B'

        elif (box.box[box.b_ball_y+ dy[d]][box.b_ball_x+ dx[d]] == GOAL):
            box.box[box.b_ball_y][box.b_ball_x] = EMPTY

            box.b_ball_y = box.b_ball_y + dy[d]
            box.b_ball_x = box.b_ball_x + dx[d]

            break
        else:
            break

    # box.set_r(0,0)
    # box.r_ball_x = 0
    # box.showBox()

    return box


def get_rotate_box(box_status, d):
    temp_box = box_status
    if dx[d] == 1:
        if box_status.r_ball_x < box_status.b_ball_x:
            print("box_status.r_ball_x < box_status.b_ball_x")
            move_b(temp_box, d)
            move_r(temp_box, d)
        else:
            move_r(temp_box, d)
            move_b(temp_box, d)
    elif dx[d] == -1:
        if box_status.r_ball_x < box_status.b_ball_x:
            move_r(temp_box, d)
            move_b(temp_box, d)
        else:
            move_b(temp_box, d)
            move_r(temp_box, d)

    elif dy[d] == 1:
        if box_status.r_ball_y < box_status.b_ball_y:
            move_b(temp_box, d)
            move_r(temp_box, d)
        else:
            move_r(temp_box, d)
            move_b(temp_box, d)
    elif dy[d] == -1:
        if box_status.r_ball_y < box_status.b_ball_y:
            move_r(temp_box, d)
            move_b(temp_box, d)
        else:
            move_b(temp_box, d)
            move_r(temp_box, d)

    return temp_box


def bfs_getout_ball(box_status):
    queue = [box_status]

    while queue:
        current_state = queue[0]
        queue = queue[1:]
        cur_depth = current_state.depth

        if cur_depth > 10:
            continue

        print("*" *10)
        current_state.showBox()

        for i in range(len(dx)):
            temp_box = copy.deepcopy(current_state)
            get_rotate_box(temp_box, i)

            print("=" *10)
            temp_box.showBox()

            if temp_box.box != current_state.box:
                # temp_state = Box_Status(temp_box)

                if temp_box.isOut() == 1:
                    print("OUT")
                    print(cur_depth + 1)
                    # print(math.floor(math.log(len(history)+1, 2)))
                    return True
                elif temp_box.isOut() == 0:
                    temp_box.depth = cur_depth + 1
                    queue.append(temp_box)
            else:
                history.append(0)


        print(-1)
        print("=" *10)
        print("=" *10)


if __name__ == "__main__":
    height, width = map(int, input().split())
    box=[]
    for i in range(height):
        box.append(list(input()))

    current_state = Box_Status(box, 0)
    # current_state.showBox()
    bfs_getout_ball(current_state)
