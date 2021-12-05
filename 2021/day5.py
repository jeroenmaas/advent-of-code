def print_map(m):
    for line in m:
        print(line)

with open('day5.txt') as f:
    input = f.readlines()

def calculate_score(part: int):

    lines = []
    for txt_line in input:
        lines.append(list(map(lambda a: list(map(lambda b: int(b), a.split(','))), txt_line.split(' -> '))))

    max_y = 0
    max_x = 0

    for line in lines:
        point1 = line[0]
        point2 = line[1]

        max_x = max(max_x, point1[0], point2[0])
        max_y = max(max_y, point1[1], point2[1])

    line_map = []
    for i in range(max_y+1):
        line_map.append([0] * (max_x+1))

    for line in lines:
        point1 = line[0]
        point2 = line[1]

        # Horizontal line, not interesting for part 1 for now
        diagonal = False
        if point1[0] != point2[0] and point1[1] != point2[1]:
            diagonal = True

        x_start = min(point1[0], point2[0])
        y_start = min(point1[1], point2[1])
        x_end = max(point1[0], point2[0])
        y_end = max(point1[1], point2[1])

        # Just keeping points for reference
        points = []
        if not diagonal:
            for i in range(x_end - x_start):
                points.append([x_start+i, y_start])
            for i in range(y_end - y_start):
                points.append([x_start, y_start+i])
            points.append([x_end, y_end])
        else:
            if part == 1:
                continue

            if x_end - x_start != y_end - y_start:
                raise "I dont know"

            x_positive = point1[0] < point2[0]
            y_positive = point1[1] < point2[1]
            for i in range(y_end - y_start):
                new_x = point1[0]+i if x_positive else point1[0]-i
                new_y = point1[1]+i if y_positive else point1[1]-i
                points.append([new_x, new_y])
            points.append([point2[0], point2[1]])

        for p in points:
            line_map[p[1]][p[0]] += 1


    c = 0
    for map_line in line_map:
        for i in map_line:
            if i >= 2:
                c += 1

    print('part' + str(part) + ': ', c)

calculate_score(1)
calculate_score(2)