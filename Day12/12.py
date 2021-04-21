# Main program

f = open("./InputData.txt", "r")
raw_data = f.read()
input_commands = [[i[0], int(i[1:])] for i in raw_data.split('\n')]


def direction_to_angle(direction):
    """
    Gets a cardinal direction and converts it to an angle.
    """
    if direction == 'N':
        return 90
    elif direction == 'E':
        return 0
    elif direction == 'W':
        return 180
    elif direction == 'S':
        return 270


def angle_to_direction(angle):
    """
    Gets a angle in degrees and converts it to a cardinal direction.
    :param angle: int(degrees)
    :return: str(Cardinal direction)
    """

    if angle == 0:
        return 'E'
    elif angle == 90:
        return 'N'
    elif angle == 180:
        return 'W'
    elif angle == 270:
        return 'S'


def change_direction(old_dir, rotation, rotation_angle):
    """
    Gets an direction of rotation L/R and converts a cardinal direction.s
    :param old_dir: cardinal direction
    :param rotation: left/right
    :param rotation_angle: degrees
    :return: cardinal direction
    """
    new_angle = 0
    if rotation == 'L':
        new_angle = (direction_to_angle(old_dir) + rotation_angle) % 360
    elif rotation == 'R':
        new_angle = (direction_to_angle(old_dir) - rotation_angle) % 360
    return angle_to_direction(new_angle)


def get_extended_commands(list_of_commands):
    cardinal_directions = ['N', 'E', 'S', 'W']
    ext_command = ['E', 0, 'E']  # Cardinal Direction, Travel Distance, Ship Direction
    ext_command_list = []
    for command in list_of_commands:
        if command[0] in cardinal_directions:
            ext_command = [command[0], command[1], ext_command[2]]
        elif command[0] == 'R' or command[0] == 'L':
            ship_dir = change_direction(ext_command[2], command[0], command[1])
            ext_command = [ext_command[0], 0, ship_dir]
        elif command[0] == 'F':
            ext_command = [ext_command[2], command[1], ext_command[2]]
        ext_command_list.append(ext_command)
    return ext_command_list


def get_manhattan_distance(list_of_commands):
    """
    Gets a list of cardinal directions and magnitudes in a list and calculates manhattan distance.
    (East - West) + (North - South)
    :param list_of_commands: list[travel direction, value, ship direction]
    :return: manhattan_distance
    """
    dir_list = [0, 0]
    for c in list_of_commands:
        if c[0] == 'N':
            dir_list[0] += c[1]
        elif c[0] == 'S':
            dir_list[0] -= c[1]
        elif c[0] == 'E':
            dir_list[1] += c[1]
        elif c[0] == 'W':
            dir_list[1] -= c[1]
    total_travel_distance = abs(dir_list[0]) + abs(dir_list[1])
    return total_travel_distance


def move_coordinate(command_list):
    """
    Moves the waypoint given by the cardinal direction.
    TODO: This functions uses vertical, horizontal notation. Need to change it to horizontal, vertical.
    :param command_list:
    :return: list[2] - waypoint_pos, list[2] - ship_pos:
    """
    waypoint_pos = [10, 1]  # Vertical , Horizontal
    ship_pos = [0, 0]
    for c in command_list:
        if c[0] == 'N':
            waypoint_pos[1] += c[1]
        elif c[0] == 'S':
            waypoint_pos[1] -= c[1]
        elif c[0] == 'E':
            waypoint_pos[0] += c[1]
        elif c[0] == 'W':
            waypoint_pos[0] -= c[1]
        elif c[0] == 'F':
            ship_pos[1] += (waypoint_pos[1] * c[1])
            ship_pos[0] += (waypoint_pos[0] * c[1])
        elif c[0] == 'L' or c[0] == 'R':
            waypoint_pos = rotate_coordinate(c[0], c[1], waypoint_pos)
        else:
            pass
    return waypoint_pos, ship_pos


def rotate_coordinate(rotation, rot_angle, coordinate):
    new_coordinate = [0, 0]  # Horizontal, Vertical
    rot_angle = rot_angle // 90
    if rot_angle == 1:
        if rotation == 'L':
            new_coordinate = [-1 * coordinate[1], +1 * coordinate[0]]
        if rotation == 'R':
            new_coordinate = [+1 * coordinate[1], -1 * coordinate[0]]
    if rot_angle == 2:
        if rotation == 'L':
            new_coordinate = [-1 * coordinate[0], -1 * coordinate[1]]
        if rotation == 'R':
            new_coordinate = [-1 * coordinate[0], -1 * coordinate[1]]
    if rot_angle == 3:
        if rotation == 'L':
            new_coordinate = [+1 * coordinate[1], -1 * coordinate[0]]
        if rotation == 'R':
            new_coordinate = [-1 * coordinate[1], +1 * coordinate[0]]
    return new_coordinate


# Main program Part 1

expanded_commands = get_extended_commands(input_commands)
part_1_answer = get_manhattan_distance(expanded_commands)
print("Part 1 Answer is :\t{0}".format(part_1_answer))

# Main program Part 2

coord = move_coordinate(input_commands)
print("Waypoint Coordinate:\t{0}\nShip Coordinate:\t\t{1}\n".format(coord[0], coord[1]))
part_2_1 = abs(coord[1][0]) + abs(coord[1][1])
part_2_2 = abs(coord[0][0] - coord[1][0]) + abs(coord[0][1] - coord[1][1])
print("Ship's Manhattan Distance:\t{0}".format(part_2_1))
print("Manhattan Distance s-w:\t\t{0}".format(part_2_2))

