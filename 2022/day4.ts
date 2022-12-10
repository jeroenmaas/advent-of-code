import {readFileSync} from "fs";
import {range, intersection} from "lodash";

const file: string = readFileSync('./day4', 'utf-8');

const input = file.trim().split('\r\n').map(e => e.split(',').map(l => l.split('-').map(e => parseInt(e))));

let overlaps = 0;
let overlapPairs = 0;
input.forEach(i => {
    const r1 = range(i[0][0], i[0][1]+1);
    const r2 = range(i[1][0], i[1][1]+1);
    const overlap = intersection(r1, r2);

    if(overlap.length >= Math.min(r1.length, r2.length)) {
        overlaps += 1;
    }

    if (overlap.length > 0) {
        overlapPairs += 1;
    }
})

console.log('part1: ', overlaps);
console.log('part2: ', overlapPairs);

