import {readFileSync} from "fs";
import {range} from "lodash";

const file: string = readFileSync('./day15', 'utf-8');

const regex = /Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)/gm;

let m;
const beaconInfos = [];
while ((m = regex.exec(file)) !== null) {
    // This is necessary to avoid infinite loops with zero-width matches
    if (m.index === regex.lastIndex) {
        regex.lastIndex++;
    }

    beaconInfos.push(m.slice(1, 5).map(n => parseInt(n)));
}


let xStart = Number.MAX_SAFE_INTEGER;
let xEnd = Number.MIN_SAFE_INTEGER;

const beaconCoordinates = new Set<string>();
beaconInfos.forEach(b => {
    const sensor = b.slice(0, 2);
    const beacon = b.slice(2, 4);

    xStart = Math.min(xStart, sensor[0], beacon[0]);
    xEnd = Math.max(xEnd, sensor[0], beacon[0]);

    // beaconCoordinates.add(sensor.join('-'));
    beaconCoordinates.add(beacon.join('-'));
});

const yToCheck = 2000000;

const blockedCoordinates = new Set<number>();
beaconInfos.forEach(b => {
    const sensor = b.slice(0, 2);
    const beacon = b.slice(2, 4);

    // Manhatten distance between beacon and sensor
    const maxDistance = Math.abs(sensor[0] - beacon[0]) + Math.abs(sensor[1] - beacon[1]);
    const distanceToY = Math.abs(sensor[1] - yToCheck);
    [1, -1].forEach(factor => {
        if (distanceToY < maxDistance) {
            const remainingDistance = maxDistance - distanceToY;

            range(0, remainingDistance + 1).forEach(d => {
                const x = sensor[0] + (d * factor);
                const s = [x, yToCheck].join('-');
                if (!beaconCoordinates.has(s)) {
                    blockedCoordinates.add(x);
                }
            });
        }
    })

});

console.log('part1: ', blockedCoordinates.size);

// Idea loop x + y. Check which sensor could spot it. And if so loop how much room the sensor has left. If that space is lower than distance to right go that way or go to x = 0 and y == 2.
const maxCoordinate = 4000000;

let x = 0;
let y = 0;
let found = false;
while(!found) {
    found = beaconInfos.every(b => {
        const sensor = b.slice(0, 2);
        const beacon = b.slice(2, 4);

        // Manhatten distance between beacon and sensor
        const maxDistance = Math.abs(sensor[0] - beacon[0]) + Math.abs(sensor[1] - beacon[1]);
        const distanceToCurrentCoordinate = Math.abs(sensor[0] - x) + Math.abs(sensor[1] - y);
        const distanceLeft = maxDistance - distanceToCurrentCoordinate;
        // console.log('distance left: ', distanceLeft);

        if(distanceLeft < 0) {
            return true;
        }
        if(distanceLeft == 0) {
            x += 1;
            return false;
        }

        if(x + distanceLeft > maxCoordinate) {
            y += 1;
            x = 0;

            if(y % 100000 == 0) {
                console.log(y);
            }
        } else {
            x += distanceLeft;
        }
        return false;
    });
}

console.log('part2: ', x * maxCoordinate + y);
