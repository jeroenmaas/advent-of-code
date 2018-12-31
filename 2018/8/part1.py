from utils.utils import file_get_contents

file = file_get_contents('input.txt')
line = file.splitlines()[0]

values = line.split(' ')

def parseNode(values):
    header = values[:2]
    content = values[2:]

    childNodesCount = int(header[0])
    metadataEntriesCount = int(header[1])

    childNodes = []
    metaData = []
    if childNodes != 0:
        for i in range(childNodesCount):
            childNode, leftover = parseNode(content)
            childNodes.append(childNode)
            content = leftover

    metaData = content[:metadataEntriesCount]
    leftover = content[metadataEntriesCount:]

    node = {
        "childNodes": childNodes,
        "metaData": metaData
    }
    return [node, leftover]

def getValueOfNode(node):
    count = 0
    for child in node["childNodes"]:
        count += getValueOfNode(child)

    for data in node["metaData"]:
        count += int(data)

    return count

results = parseNode(values)
print("Result of part 1: " + str(getValueOfNode(results[0])))

