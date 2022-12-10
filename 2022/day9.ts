import {readFileSync} from "fs";
import {range} from "lodash";


const file: string = readFileSync('./day9', 'utf-8');

interface Action {
    direction: string;
    count: number
}

const actions = file.trim().split('\r\n').map(i => i.split(' ')).map(i => {
    return {
        direction: i[0],
        count: parseInt(i[1])
    } as Action
});


let headPos = [0, 0]
let tailPos = [0, 0]
let uniqueCoordinates = new Set<string>();
uniqueCoordinates.add([0, 0].join('_'));

actions.forEach(a => {
    let dir = [0, 0];
    if(a.direction == 'U') {
        dir[1] = 1;
    }else if (a.direction == 'D') {
        dir[1] = -1;
    }else if (a.direction == 'L') {
        dir[0] = -1;
    }else if (a.direction == 'R') {
        dir[0] = 1;
    }else {
        throw new Error("Unknown dir: " + dir);
    }

    range(0, a.count).forEach(_ => {
        headPos[0] += dir[0];
        headPos[1] += dir[1];

        // 2, 0 / -2, 0
        const dist = [headPos[0] - tailPos[0], headPos[1] - tailPos[1]];
        // No need to move. We are still touching to the head
        if(Math.abs(dist[0]) <= 1 && Math.abs(dist[1]) <= 1) {
            return;
        }else if(Math.abs(dist[0]) > 1 && Math.abs(dist[1]) == 0) {
            tailPos[0] += dist[0] > 0 ? 1 : -1;
        }else if(Math.abs(dist[1]) > 1 && Math.abs(dist[0]) == 0) {
            tailPos[1] += dist[1] > 0 ? 1 : -1;
        }else {
            tailPos[0] += dist[0] > 0 ? 1 : -1;
            tailPos[1] += dist[1] > 0 ? 1 : -1;
        }

        uniqueCoordinates.add(tailPos.join('_'))
    });
});

console.log('part1: ', uniqueCoordinates.size);

let knotsPositions = range(0, 9).map(r => [0, 0]);

headPos = [0, 0]
uniqueCoordinates = new Set<string>();
uniqueCoordinates.add([0, 0].join('_'));

actions.forEach(a => {
    let dir = [0, 0];
    if(a.direction == 'U') {
        dir[1] = -1;
    }else if (a.direction == 'D') {
        dir[1] = 1;
    }else if (a.direction == 'L') {
        dir[0] = -1;
    }else if (a.direction == 'R') {
        dir[0] = 1;
    }else {
        throw new Error("Unknown dir: " + dir);
    }

    range(0, a.count).forEach(_ => {
        headPos[0] += dir[0];
        headPos[1] += dir[1];
        let previous = headPos;

        knotsPositions.forEach(k => {
            // 2, 0 / -2, 0
            const dist = [previous[0] - k[0], previous[1] - k[1]];

            if(Math.abs(dist[0]) <= 1 && Math.abs(dist[1]) <= 1) {
                // No need to move. We are still touching to the head
            }else if(Math.abs(dist[0]) > 1 && Math.abs(dist[1]) == 0) {
                k[0] += dist[0] > 0 ? 1 : -1;
            }else if(Math.abs(dist[1]) > 1 && Math.abs(dist[0]) == 0) {
                k[1] += dist[1] > 0 ? 1 : -1;
            }else {
                k[0] += dist[0] > 0 ? 1 : -1;
                k[1] += dist[1] > 0 ? 1 : -1;
            }

            previous = k;
        });


        uniqueCoordinates.add(knotsPositions.at(-1)!.join('_'))
    });
});

console.log('part2: ', uniqueCoordinates.size);

