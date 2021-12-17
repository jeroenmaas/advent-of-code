import json
import math

with open('day16.txt') as f:
    input = f.readline()

input_as_bytes = list(bin(int(input, 16))[2:].zfill(len(input) * 4))

def get_bytes(c, bytes):
    return "".join([bytes.pop(0) for idx in range(c)])

globals()['version_numbers_sum'] = 0
def parse_packet(binary_input: []):
    # version & type
    v = int(get_bytes(3, binary_input), 2)
    globals()['version_numbers_sum'] += v

    t = int(get_bytes(3, binary_input), 2)

    if t == 4:
        total_bytes = ""
        while True:
            b = get_bytes(5, binary_input)
            total_bytes += b[1:]
            if b[0] == '0':
                break
        total_bytes_rep = int(total_bytes, 2)
        return {'t': t, 'v': v, 'value': total_bytes_rep}
    else:
        length_type_id = get_bytes(1, binary_input)
        if length_type_id == '0':
            size_of_subpackets = int(get_bytes(15, binary_input), 2)
            bytes_of_subpacket = list(get_bytes(size_of_subpackets, binary_input))
            values = []
            packets = []
            while bytes_of_subpacket:
                packet = parse_packet(bytes_of_subpacket)
                packets.append(packet)
                values.append(packet['value'])
        else:
            count_of_subpackets = int(get_bytes(11, binary_input), 2)
            packets = []
            values = []
            for i in range(count_of_subpackets):
                packet = parse_packet(binary_input)
                packets.append(packet)
                values.append(packet['value'])

        value = None
        if t == 0:
            value = sum(values)
        elif t == 1:
            value = math.prod(values)
        elif t == 2:
            value = min(values)
        elif t == 3:
            value = max(values)
        elif t == 5:
            value = 1 if values[0] > values[1] else 0
        elif t == 6:
            value = 1 if values[0] < values[1] else 0
        elif t == 7:
            value = 1 if values[0] == values[1] else 0

        return {'t': t, 'v': v, 'packets': packets, 'value': value}

packet_result = parse_packet(input_as_bytes)
# print(json.dumps(packet_result))

print('part1: ', globals()['version_numbers_sum'])
print('part2: ', packet_result['value'])