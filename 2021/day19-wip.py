import math

with open('day19-2021.txt') as f:
    input = f.readlines()

found_coordinates_by_becean = []
l = []

for line in input:
    if line == '' or line == '\n':
        continue
    if line.startswith('---'):
        if(len(l) > 0):
            found_coordinates_by_becean.append(l)
            l = []
        continue

    l.append(list(map(lambda a: int(a), line.split(','))))

found_coordinates_by_becean.append(l)

def get_distances(c1):
    distances_grouped = []
    for i in range(len(c1)):
        distances = []
        for j in range(len(c1)):
            if i != j:
                xdiff = c1[i][0] - c1[j][0]
                ydiff = c1[i][1] - c1[j][1]
                zdiff = c1[i][2] - c1[j][2]

                pitagoras_diff = math.sqrt(pow(xdiff, 2) + pow(ydiff, 2) + pow(zdiff, 2))
                distances.append([pitagoras_diff, c1[i], c1[j]])
        if len(distances) > 0:
            distances_grouped.append(distances)
    return distances_grouped

def find_matches(c1, c2):
    distances1 = get_distances(c1)
    distances2 = get_distances(c2)

    top_matches_count = 0
    top_matches1 = None
    top_matches2 = None
    for g1 in distances1:
        for g2 in distances2:
            d = []
            for d1 in g1:
                for d2 in g2:
                    if d1[0] == d2[0]:
                        d.append(d1[0])

            matches = []
            matches2 = []
            for d1 in g1:
                for d2 in g2:
                    if d1[0] == d2[0]:
                        if d1[1] not in matches:
                            matches.append(d1[1])
                        if d1[2] not in matches:
                            matches.append(d1[2])
                        if d2[1] not in matches2:
                            matches2.append(d2[1])
                        if d2[2] not in matches2:
                            matches2.append(d2[2])
            m = max(len(matches), len(matches2))
            if m > top_matches_count:
                top_matches_count = m
                top_matches1 = matches
                top_matches2 = matches2

    return top_matches_count, top_matches1, top_matches2

total_matches = 0
options = []
for i in range(len(found_coordinates_by_becean)):
    matches_for_item = []
    for j in range(len(found_coordinates_by_becean)):
        if i == j:
            continue

        if [i, j] in options or [j, i] in options:
            continue

        matches, m1, m2 = find_matches(found_coordinates_by_becean[i], found_coordinates_by_becean[j])

        if matches > 0:
            for m in m1:
                if m not in matches_for_item:
                    matches_for_item.append(m)

        options.append([i, j])

    print('matches for item: ', len(matches_for_item))
    total_matches += len(matches_for_item)

total_items = sum(map(lambda a: len(a), found_coordinates_by_becean))
print('total_matches', total_matches)
print('part1: ', total_items - total_matches)

# available_beacons = [i for i in range(len(found_coordinates_by_becean))]
# found_beacons = []
# searches = []
#
# total_matches = 0
# found_beacons.append(0)
# available_beacons.remove(0)
# while len(available_beacons) > 0:
#     for i in found_beacons:
#         if i in searches:
#             continue
#         # print('going to search for: ', i)
#
#         for j in available_beacons:
#             # print('searching for: ', j, ' from: ', i)
#
#             matches = find_matches(found_coordinates_by_becean[i], found_coordinates_by_becean[j])
#             if matches > 11:
#                 found_beacons.append(j)
#                 print('matches: ', matches)
#                 total_matches += matches
#         for b in found_beacons:
#             if b in available_beacons:
#                 available_beacons.remove(b)
#
#         # print('searched for: ', i)
#         searches.append(i)
#
# total_items = sum(map(lambda a: len(a), found_coordinates_by_becean))
# print(total_matches)
# print('part1: ', total_items - total_matches)


