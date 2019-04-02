#p_14503

NOT_ACCESSIBLE_STATUS = 1
NOT_CLEAR_ROOM = 0
CLEAN_ROOM= 2

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Room:
    def __init__(self, room_height, room_width, room):
        self.room_height = room_height
        self.room_width = room_width
        self.room = room

    def get_room_state(self, loc_x, loc_y):
        return self.room[loc_x][loc_y]

    def set_room_clean(self, loc_x, loc_y):
        self.room[loc_x, loc_y] = CLEAN_ROOM


class Robot_Clener:
    def __init__(self, loc_x, loc_y, dir, room):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.dir = dir
        self.room = room

        self.clean_room_around = 0
        self.num_cleaned_room = 0


    def do_clean(self):
        if self.room.get_room_state(self.loc_x, self.loc_y) == NOT_CLEAR_ROOM:
            self.room.set_room_clean(self.loc_x, self.loc_y)

    def get_left_loc(self):
        if self.dir == NORTH:
            return self.loc_x-1, self.loc_y, WEST
        elif self.dir == EAST:
            return self.loc_x, self.loc_y+1, SOUTH
        elif self.dir == SOUTH:
            return self.loc_x +1, self.loc_y, EAST
        elif self.dir == WEST:
            return self.loc_x, self.loc_y-1, NORTH

    def do_move_back_double():
        if self.dir == NORTH:
            return self.loc_x, self.loc_y-2
        elif self.dir == EAST:
            return self.loc_x-2, self.loc_y
        elif self.dir == SOUTH:
            return self.loc_x, self.loc_y+2
        elif self.dir == WEST:
            return self.loc_x+2, self.loc_y

    def do_move(self):
        temp_loc_x, temp_loc_y,temp_dir = get_left_loc()

        if if self.room.get_room_state(temp_loc_x, temp_loc_y) == NOT_CLEAR_ROOM:
            self.dir = temp_dir
            self.loc_x, self.loc_y = temp_loc_x, temp_loc_y
            self.clean_room_around = 1

            do_clean()
        else
            if self.clean_room_around < 4:
                self.clean_room_around += 1
                self.dir = temp_dir
                do_clean()
            else:
                #do move back_double needs to check
                # whether room is the wall or already clearnd
                do_move_back_double()
                do_clean()

        return ""


def main():
    room_height, room_width = map(int, input().split())
    robot_x, robot_y, robot_dir = map(int,input().split())

    room_list = []
    for each_row in range(room_height):
        room_list.append(list(map(int, input().split())))

    print(room_list)
    room_status = Room(room_height, room_width, room_list)
    robot_status = Robot_Clener(robot_x, robot_y, robot_dir, room_status)


    print(robot_status.do_clean())

if __name__ == "__main__":
    main()
