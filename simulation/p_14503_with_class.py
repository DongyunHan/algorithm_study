# p_14503
# OOP 개념에 맞게 class로 나누어서 풀어봤더니
# 코드가 훨씬 길어져 버림

class Room_State:
    WALL = 1
    NOT_CLEANED_ROOM = 0
    CLEANED_ROOM= 2

class Movement:
    # (dy, dx) => North / East / South / West
    DY = [-1, 0, 1, 0]
    DX = [0, 1, 0, -1]


class Room(Room_State):
    def __init__(self, room):
        self.room = room
        self.num_clean = 0

    def get_clean_room(self):
        return self.num_clean

    def set_room_clean(self, loc_y, loc_x):
        self.num_clean += 1
        self.room[loc_y][loc_x] = Room_State.CLEANED_ROOM

    def is_room_clean(self, loc_y, loc_x):
        if self.room[loc_y][loc_x] == Room_State.CLEANED_ROOM or self.room[loc_y][loc_x] == Room_State.WALL:
            return True
        else:
            return False

    def is_room_wall(self, loc_y, loc_x):
        if self.room[loc_y][loc_x] == Room_State.WALL:
            return True
        else:
            return False


class Robot_Clener(Movement):
    def __init__(self, loc_y, loc_x, dir, room):
        self.loc_y = loc_y
        self.loc_x = loc_x

        self.dir = dir
        self.room = room

    def left_turn(self):
        if self.dir == 0:
            return 3
        else:
            return self.dir-1

    def do_clean(self):
        turn_count = 0

        while True:
            print(self.loc_y , ",", self.loc_x)

            if turn_count == 4:
                # In case 4/
                back_y = self.loc_y - Movement.DY[self.dir]
                back_x = self.loc_x - Movement.DX[self.dir]

                if self.room.is_room_wall(back_y, back_x):
                    # print(count_clean(room))
                    break
                else:
                    self.loc_y, self.loc_x, self.dir, turn_count = back_y, back_x, self.dir, 0

            # 1. Clean the current location
            if not self.room.is_room_clean(self.loc_y, self.loc_x):
                self.room.set_room_clean(self.loc_y, self.loc_x)

            # look left
            turn = self.left_turn()
            temp_y = self.loc_y + Movement.DY[turn]
            temp_x = self.loc_x + Movement.DX[turn]

            if not self.room.is_room_clean(temp_y, temp_x):
                # In case 1
                self.loc_y, self.loc_x, self.dir, turn_count = temp_y, temp_x, turn, 0
            else:
                # In case 2
                self.loc_y, self.loc_x, self.dir ,turn_count = self.loc_y, self.loc_x, turn, turn_count+1

        return self.room.get_clean_room()


def main():
    room_height, room_width = map(int, input().split())
    robot_y, robot_x, robot_dir = map(int,input().split())

    room_list = []
    for each_row in range(room_height):
        room_list.append(list(map(int, input().split())))

    # room_status = Room(room_list)
    robot_status = Robot_Clener(robot_y, robot_x, robot_dir, Room(room_list))

    print(robot_status.do_clean())

if __name__ == "__main__":
    main()
